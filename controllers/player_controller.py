from models.player_model import PlayerModel
from views.player_view import PlayerView

class PlayerController:
    def __init__(self):
        self.playerView = PlayerView()

    def load_all_players(self):
        return PlayerModel.load_all_players()

    def display_players(self):
        self.playerView.display_players(self.load_all_players())

    def add_player(self):
        last_name, first_name, birth_date, national_id = self.playerView.get_player_data()
        player = PlayerModel(last_name, first_name, birth_date, national_id)
        player.save()

    def select_player(self):
        players_list = self.load_all_players()
        max_index = len(players_list)
        selected_index = self.playerView.select_player_by_index(players_list, max_index)
        if selected_index != None:
            return players_list[selected_index - 1]

    def modify_player(self, player, attribute):  
        setattr(player, attribute, self.playerView.modify_player())
        player.update()

