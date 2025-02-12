from models.player_model import PlayerModel
from views.player_view import PlayerView

class PlayerController:
    def __init__(self, players_file):
        self.json_players = players_file
        self.playerView = PlayerView()

    def display_players(self):
        players_list = self.json_players.read_json(PlayerModel)
        self.playerView.display_players(players_list)

    def add_player(self):
        last_name, first_name, birth_date, national_id = self.playerView.get_player_data()
        players_list = self.json_players.read_json(PlayerModel)
        id = self.json_players.generate_id(players_list)
        new_player = PlayerModel(last_name, first_name, birth_date, national_id, id)
        self.json_players.append_json(new_player)
    
    def select_player(self):
        self.display_players()
        id = self.playerView.select_player()
        players_list = self.json_players.read_json(PlayerModel)
        player = self.json_players.get_object_by_id(id, players_list)
        if player == None:
            self.playerView.no_player_find()
        else:
            return player

    def update_player(self, updated_player):
        players_list = self.json_players.read_json(PlayerModel)
        for index, player in enumerate(players_list):
            if player.id == updated_player.id:
                players_list[index] = updated_player
        self.json_players.write_json(players_list)

    def modify_player(self, player, attribute):  
        setattr(player, attribute, self.playerView.modify_player())
        self.update_player(player)
        return player
    
    def delete_player(self, deleted_player):
        players_list = self.json_players.read_json(PlayerModel)
        for index, player in enumerate(players_list):
            if player.id == deleted_player.id:
                players_list.remove(player)
        self.json_players.write_json(players_list)
