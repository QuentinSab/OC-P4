from models.json_model import JsonModel
from models.round_model import RoundModel

from datetime import datetime
from dataclasses import dataclass, asdict
import uuid
import random

from views.utils import Utils

TOURNAMENTS_JSON = "tournaments.json"

@dataclass
class TournamentModel:
    name: str
    status: str
    place: str
    description: str
    start_date: str
    end_date: str
    id: str
    round_number: int
    current_round: int
    rounds: list
    players: list

    def __init__(
        self,
        name="name",
        status="status",
        place="place",
        description="description",
        start_date="start_date",
        end_date="end_date",
        id=None,
        round_number=4,
        current_round=0,
        rounds=[],
        players=[]
    ):
        self.json_tournaments = JsonModel(TOURNAMENTS_JSON)
        self.name = name
        self.status = status
        self.place = place
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.id = id if id else str(uuid.uuid4())
        self.round_number = round_number
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        
    def save(self):
        tournaments_list = self.load_all_tournaments()
        tournaments_list.append(self)
        self.json_tournaments.write_json(tournaments_list)

    def delete(self):
        tournaments_list = self.load_all_tournaments()
        for tournament in tournaments_list:
            if tournament.id == self.id:
                tournaments_list.remove(tournament)
        self.json_tournaments.write_json(tournaments_list)

    def update(self):
        tournaments_list = self.load_all_tournaments()
        for tournament in tournaments_list:
            if tournament.id == self.id:
                tournaments_list.remove(tournament)
                tournaments_list.append(self)
        self.json_tournaments.write_json(tournaments_list)

    def get_participants(self, players_list):
        participants = []
        for player in players_list:
            if player.id in self.players:
                participants.append(player)
        return participants

    def launch(self):
        self.status = "ongoing"
        self.start_date = datetime.now().isoformat()
        self.update()

    def get_rounds(self):
        rounds_list = []
        for round in self.rounds:
            if isinstance(round, dict):
                rounds_list.append(RoundModel(**round))
            else:
                rounds_list.append(round)
        return rounds_list

    def get_ladder(self):
        rounds_list = self.get_rounds()
        player_scores = {}
        for round in rounds_list:
            for match in round.matchs_list:
                for player in match:
                    player_id, player_score = player
                    if player_id in player_scores:
                        player_scores[player_id] += player_score
                    else:
                        player_scores[player_id] = player_score
        ladder = [(player_id, score) for player_id, score in player_scores.items()]
        ladder = sorted(ladder, key=lambda x: x[1], reverse=True)
        return ladder

    def name_ladder_ids(self, ladder, participants):
        named_ladder = []
        for player_id, score in ladder:
            for participant in participants:
                if participant.id == player_id:
                    name = participant.last_name + " " + participant.first_name
                    named_ladder.append((name, score))
        return named_ladder

    def start_round(self):
        round = RoundModel("Round " + str(self.current_round+1), datetime.now().isoformat(), "end_date", 0, [])
        pairs_list = []
        
        # Si premier round 
        if self.current_round == 0:
            players_list = self.players
            
            # Mélange aléatoirement les joueurs
            random.shuffle(players_list)
            
            # Ajoute par pair tous les joueurs à la liste
            for pair in range(0, len(players_list), 2):
                pairs_list.append((players_list[pair], players_list[pair + 1]))
                
        else:
            ladder = self.get_ladder()
            
            # Liste les adversaires disponibles
            available_players = [player[0] for player in ladder]

            while available_players:
                # Prend le premier joueur du ladder
                player1 = available_players.pop(0)
                
                # Récupère les adversaires déjà affrontés
                opponents_faced = self.get_opponents(player1)  
                
                # Trouve un adversaire qui n'a pas encore été affronté
                player2 = None
                for opponent in available_players:
                    if opponent not in opponents_faced:
                        player2 = opponent
                        break

                # Si tous les adversaires ont déjà été affrontés, prend le premier disponible
                if player2 is None:
                    player2 = available_players[0]

                available_players.remove(player2)
                pairs_list.append((player1, player2))

        # Crée un match pour chaque paire de joueur
        for pair in pairs_list:
            match = ([pair[0], 0], [pair[1], 0])
            round.matchs_list.append(match)
            
        self.rounds.append(round)
        self.update()

    def play_match(self, result):
        round = self.get_rounds()[self.current_round]
        match = round.matchs_list[round.current_match]
        match[0][1], match[1][1] = result[0], result[1]
        round.matchs_list[round.current_match] = match
        self.update()

    def progress(self):
        round = self.get_rounds()[self.current_round]
        round.current_match += 1
        self.rounds[self.current_round] = round
        if round.current_match == len(self.players)/2:
            round.end_date = datetime.now().isoformat()
            if self.current_round == int(self.round_number)-1:
                self.status = "finished"
                self.end_date = datetime.now().isoformat()
                self.update()
                return True
            else:
                self.current_round += 1
                self.start_round()           
        self.update()

    def get_opponents(self, player):
        rounds = self.get_rounds()
        opponents = []
        players_count = len(self.players)

        for round in rounds:
            for match in round.matchs_list:
                # Si le joueur est trouvé dans le match, on ajoute l'adversaire
                if match[0][0] == player:
                    opponents.append(match[1][0])
                elif match[1][0] == player:
                    opponents.append(match[0][0])

                # Si tous les joueurs ont été affronté par player
                if len(set(opponents)) == players_count - 1:
                    opponents.clear()
                    return opponents

        return opponents

    @staticmethod
    def load_all_tournaments():
        json_tournaments = JsonModel(TOURNAMENTS_JSON)
        return json_tournaments.read_json(TournamentModel)
    
    @staticmethod
    def add_tournament(name, place, description, round_number):
        tournament = TournamentModel(
            name=name,
            status="starting",
            place=place,
            description=description,
            start_date="start_date",
            end_date="end_date",
            round_number=round_number,
            current_round=0,
            rounds=[],
            players=[]
        )
        tournament.save()