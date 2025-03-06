from models.player_model import PlayerModel
from views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.playerView = PlayerView()

    def load_all_players(self):
        """Return a list of all players"""
        return PlayerModel.load_all_players()

    def display_players(self):
        """"Displays the list of all players"""
        self.playerView.display_players(self.load_all_players())

    def add_player(self):
        """Add a player to the player file"""
        last_name, first_name, birth_date, national_id = self.playerView.get_player_data()
        player = PlayerModel(last_name, first_name, birth_date, national_id)
        player.save()

    def select_player(self):
        """Display the list of players and return the selected player"""
        players_list = self.load_all_players()
        max_index = len(players_list)

        # Display the list of numbered players and retrieve the number of the chosen player
        selected_index = self.playerView.select_player_by_index(players_list, max_index)

        if selected_index:
            # Returns the player corresponding to the number chosen
            return players_list[selected_index - 1]

    def modify_player(self, player, attribute):
        """Modify player information according to the given attribute"""
        setattr(player, attribute, self.playerView.modify_player())
        player.update()

    def delete_player(self, player, tournaments_list):
        # Check that the player is not registered in a tournament
        if not player.check_registration(tournaments_list):
            player.delete()
        else:
            self.playerView.delete_registered_error(player)
