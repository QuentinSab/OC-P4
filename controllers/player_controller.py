from models.player_model import PlayerModel

class PlayerController:
    def __init__(self, players_file):
        self.json_players = players_file

    def add_player(self, last_name, first_name, birth_date, national_id, local_id):
        new_player = PlayerModel(last_name, first_name, birth_date, national_id, local_id)
        self.json_players.append_json(new_player)