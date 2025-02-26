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
        """Add self to tournaments file"""
        tournaments_list = self.load_all_tournaments()
        tournaments_list.append(self)
        self.json_tournaments.write_json(tournaments_list)

    def delete(self):
        """Remove self from tournaments file"""
        tournaments_list = self.load_all_tournaments()
        for tournament in tournaments_list:
            if tournament.id == self.id:
                tournaments_list.remove(tournament)
        self.json_tournaments.write_json(tournaments_list)

    def update(self):
        """Update self in tournaments file"""
        tournaments_list = self.load_all_tournaments()
        for tournament in tournaments_list:
            if tournament.id == self.id:
                tournaments_list.remove(tournament)
                tournaments_list.append(self)
        self.json_tournaments.write_json(tournaments_list)

    def launch(self):
        """Start the tournament"""
        self.status = "ongoing"
        self.start_date = datetime.now().isoformat()
        self.update()

    def progress(self):
        "Advance tournament progress by one match"
        round = self.rounds[self.current_round]
        round.current_match += 1
        self.rounds[self.current_round] = round
        
        # If all matches in the round have been played
        if round.current_match == len(self.players)/2:
            round.end_date = datetime.now().isoformat()
            # If current round was the last
            if self.current_round == int(self.round_number)-1:
                return self.end()
            else:
                self.current_round += 1
                self.start_round()
        self.update()

    def end(self):
        """End the tournament"""
        self.status = "finished"
        self.end_date = datetime.now().isoformat()
        self.update()
        return True

    def convert_rounds(self):
        """Convert tournament rounds into objects"""
        rounds_list = []
        for round in self.rounds:
            if isinstance(round, dict):
                rounds_list.append(RoundModel(**round))
            else:
                rounds_list.append(round)
        self.rounds = rounds_list

    def get_participants(self, players_list):
        participants = []
        for player in players_list:
            if player.id in self.players:
                participants.append(player)
        return participants

    def get_opponents(self, player):
        """Return a list of last opponents that player has faced"""
        opponents = []
        players_count = len(self.players)

        for round in self.rounds:
            for match in round.matchs_list:
                # If player is found in the match, the opponent is added.
                if match[0][0] == player:
                    opponents.append(match[1][0])
                elif match[1][0] == player:
                    opponents.append(match[0][0])

                # If all the opponents have faced player
                if len(set(opponents)) == players_count - 1:
                    opponents.clear()
                    return opponents
        return opponents

    def get_pairs(self):
        pairs_list = []

        # If first round
        if self.current_round == 0:
            players_list = self.players
            random.shuffle(players_list)
            
            # Adds all players to the list by pair
            for pair in range(0, len(players_list), 2):
                pairs_list.append((players_list[pair], players_list[pair + 1]))
                
        else:
            ladder = self.get_ladder()
            # List available players by descending score
            available_players = [player[0] for player in ladder]
            
            while available_players:
                player1 = available_players.pop(0)
                opponents_faced = self.get_opponents(player1)  
                player2 = None
                
                # If an opponent has not been faced, he is added
                for opponent in available_players:
                    if opponent not in opponents_faced:
                        player2 = opponent
                        break

                # If all the opponents have already been faced, take the first one available
                if player2 is None:
                    player2 = available_players[0]

                available_players.remove(player2)
                pairs_list.append((player1, player2))
        return pairs_list

    def get_ladder(self):
        """Return the tournament ranking"""
        ranking = []

        # For each player in each match in each round
        for round in self.rounds:
            for match in round.matchs_list:
                for player in match:
                    player_id, player_score = player
                    found = False
                    
                    # Browse ranking
                    for i in range(len(ranking)):
                        ranked_player = ranking[i]
                        
                        # If player is found, add up his score
                        if ranked_player[0] == player_id:
                            ranking[i] = (ranking[i][0], ranking[i][1] + player_score)
                            found = True
                            break
                    
                    # If player is not in ranking, he is added
                    if not found:
                        ranking.append((player_id, player_score))

        # Sort ranking by descending score
        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking

    def start_round(self):
        """Create the next round"""
        round = RoundModel("Round " + str(self.current_round+1), datetime.now().isoformat(), "end_date", 0, [])
        
        # Create a match for each pair of players
        for pair in self.get_pairs():
            match = ([pair[0], 0], [pair[1], 0])
            round.matchs_list.append(match)
            
        self.rounds.append(round)
        self.update()

    def play_match(self, result):
        """Assign result to the current match"""
        round = self.rounds[self.current_round]
        match = round.matchs_list[round.current_match]
        match[0][1], match[1][1] = result[0], result[1]
        round.matchs_list[round.current_match] = match
        self.update()

    @staticmethod
    def load_all_tournaments():
        """Return a list of all tournaments"""
        json_tournaments = JsonModel(TOURNAMENTS_JSON)
        return json_tournaments.read_json(TournamentModel)
    
    @staticmethod
    def add_tournament(name, place, description, round_number):
        """Create a tournament in the tournament file"""
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