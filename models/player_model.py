from models.json_model import JsonModel
from dataclasses import dataclass, asdict

@dataclass
class PlayerModel:
    last_name:str
    first_name:str
    birth_date:str
    national_id:str
    id:int
    
    def __init__(self, last_name = "last_name", first_name =  "first_name", birth_date = "birth_date", national_id = "national_id", id=None):
        self.json_players = JsonModel("players.json")
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id

        players_list = self.json_players.read_json(PlayerModel)
        
        if id==None:
            self.id = self.json_players.generate_id(players_list)
        else:
            self.id = id
        
    def save(self):
        self.json_players.append_json(self)
    
    def __dict__(self):
        return {'last_name':self.last_name}
    
    @staticmethod
    def load_all_players():
        print("test")
        json_players = JsonModel("players.json")
        return json_players.read_json(PlayerModel)

