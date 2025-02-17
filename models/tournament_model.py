from models.json_model import JsonModel
from dataclasses import dataclass, asdict
import uuid

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
    current_round: str
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
        current_round="current_round",
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
        
    @staticmethod
    def load_all_tournaments():
        json_tournaments = JsonModel(TOURNAMENTS_JSON)
        return json_tournaments.read_json(TournamentModel)