from models.json_model import JsonModel
from dataclasses import dataclass, asdict
import uuid

PLAYERS_JSON = "players.json"

@dataclass
class PlayerModel:
    last_name:str
    first_name:str
    birth_date:str
    national_id:str
    id:str

    def __init__(self, last_name = "last_name", first_name =  "first_name", birth_date = "birth_date", national_id = "national_id", id=None):
        self.json_players = JsonModel(PLAYERS_JSON)
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.id = id if id else str(uuid.uuid4())

    def save(self):
        players_list = self.load_all_players()
        players_list.append(self)
        self.json_players.write_json(players_list)

    def delete(self):
        players_list = self.load_all_players()
        for player in players_list:
            if player.id == self.id:
                players_list.remove(player)
        self.json_players.write_json(players_list)

    @staticmethod
    def load_all_players():
        json_players = JsonModel(PLAYERS_JSON)
        return json_players.read_json(PlayerModel)
