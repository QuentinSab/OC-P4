from models.player_model import PlayerModel
from views.player_view import PlayerView

class PlayerController:
    def __init__(self, players_file):
        self.json_players = players_file
        self.playerView = PlayerView()

    def display_players(self):
        players_list = self.json_players.read_json()
        self.playerView.display_players(players_list)

    def add_player(self):
        last_name, first_name, birth_date, national_id = self.playerView.get_player_data()
        players_list = self.json_players.read_json()
        local_id = PlayerModel.generate_local_id(players_list)
        new_player = PlayerModel(last_name, first_name, birth_date, national_id, local_id)
        self.json_players.append_json(new_player)