from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.main_view import MainView

class MainController:
    def __init__(self):
        self.playerController = PlayerController()
        self.tournamentController = TournamentController()
        self.mainView = MainView()

    def display_menu(self, menu, menu_target = ""):
        self.mainView.create_menu(menu, menu_target)
        option = self.mainView.choice()
        return option

    def execution(self):
        while True:
            match self.display_menu(self.mainView.main_menu):
                case "1":
                    self.players_menu()
                case "2":
                    self.tournaments_menu()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def players_menu(self):
        while True:
            match self.display_menu(self.playerController.playerView.players_menu):
                case "1":
                    self.playerController.display_players()
                case "2":
                    self.playerController.add_player()
                case "3":
                    self.player_modification_menu()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def player_modification_menu(self):
        player = self.playerController.select_player()
        if player == None:
            return None
        while True:
            match self.display_menu(self.playerController.playerView.modification_menu, menu_target = player.first_name):
                case "1":
                    self.playerController.modify_player(player, "last_name")
                case "2":
                    self.playerController.modify_player(player, "first_name")
                case "3":
                    self.playerController.modify_player(player, "birth_date")
                case "4":
                    self.playerController.modify_player(player, "national_id")
                case "5":
                    player = self.playerController.select_player()
                case "6":
                    player.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def tournaments_menu(self):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.tournaments_menu):
                case "1":
                    self.tournamentController.display_tournaments()
                case "2":
                    self.tournamentController.add_tournament()
                case "3":
                    self.manager_tournament_menus()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def manager_tournament_menus(self):
        """Determine which menu to use according to the selected tournament status."""
        tournament = self.tournamentController.select_tournament()
        if tournament:
            match tournament.status:
                case "starting":
                    self.starting_tournament_menu(tournament)
                case "ongoing":
                    self.ongoing_tournament_menu(tournament)
                case "finished":
                    self.finished_tournament_menu(tournament)
                case _:
                    pass
 
    def starting_tournament_menu(self, tournament):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.starting_tournament_menu, menu_target = tournament.name):
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    self.tournamentController.modify_tournament(tournament, "name")
                case "3":
                    self.tournamentController.modify_tournament(tournament, "place")
                case "4":
                    self.tournamentController.modify_tournament(tournament, "description")
                case "5":
                    players_list = self.playerController.load_all_players()
                    self.tournamentController.display_participant(tournament, players_list)
                case "6":
                    player = self.playerController.select_player()
                    self.tournamentController.add_participant(tournament, player.id)
                case "7":
                    players_list = self.playerController.load_all_players()
                    self.tournamentController.remove_participant(tournament, players_list)
                case "8":
                    if self.tournamentController.launch_tournament(tournament):
                        break
                case "9":
                    tournament.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def ongoing_tournament_menu(self, tournament):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.ongoing_tournament_menu, menu_target = tournament.name):
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    players_list = self.playerController.load_all_players()
                    self.tournamentController.display_ladder(tournament, players_list)
                case "3":
                    self.tournamentController.display_round(tournament.get_rounds()[tournament.current_round])
                case "4":
                    if self.tournamentController.play_match(tournament) == True:
                        break
                case "5":
                    tournament.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def finished_tournament_menu(self, tournament):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.finished_tournament_menu, menu_target = tournament.name):
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    players_list = self.playerController.load_all_players()
                    self.tournamentController.display_ladder(tournament, players_list)
                case "3":
                    tournament.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()
