from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from views.main_view import MainView
from views.menus import menus


class MainController:
    def __init__(self):
        self.playerController = PlayerController()
        self.tournamentController = TournamentController()
        self.mainView = MainView()

    def execution(self):
        while True:
            self.mainView.display_menu(menus["main"])
            match self.mainView.choice():
                case "1":
                    self.players_menu()
                case "2":
                    self.tournaments_menu()
                case "3":
                    self.report_menu()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def players_menu(self):
        while True:
            self.mainView.display_menu(menus["players"])
            match self.mainView.choice():
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
        if not player:
            return None
        while True:
            target = player.last_name + " " + player.first_name
            self.mainView.display_menu(menus["player_modification"], target=target)
            match self.mainView.choice():
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
                    tournaments_list = self.tournamentController.load_all_tournaments()
                    self.playerController.delete_player(player, tournaments_list)
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def tournaments_menu(self):
        while True:
            self.mainView.display_menu(menus["tournaments"])
            match self.mainView.choice():
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
        players_list = self.playerController.load_all_players()
        tournament = self.tournamentController.select_tournament(players_list)
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
            self.mainView.display_menu(menus["starting_tournament"], target=tournament.name)
            match self.mainView.choice():
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    self.tournamentController.modify_tournament(tournament, "name")
                case "3":
                    self.tournamentController.modify_tournament(tournament, "place")
                case "4":
                    self.tournamentController.modify_tournament(tournament, "description")
                case "5":
                    self.tournamentController.display_participant(tournament)
                case "6":
                    player = self.playerController.select_player()
                    self.tournamentController.add_participant(tournament, player)
                case "7":
                    self.tournamentController.remove_participant(tournament)
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
            self.mainView.display_menu(menus["ongoing_tournament"], target=tournament.name)
            match self.mainView.choice():
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    self.tournamentController.display_ladder(tournament)
                case "3":
                    self.tournamentController.display_participant(tournament)
                case "4":
                    self.tournamentController.display_round(tournament)
                case "5":
                    if self.match_result_menu(tournament):
                        break
                case "6":
                    tournament.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def finished_tournament_menu(self, tournament):
        while True:
            self.mainView.display_menu(menus["finished_tournament"], target=tournament.name)
            match self.mainView.choice():
                case "1":
                    self.tournamentController.display_tournament_data(tournament)
                case "2":
                    self.tournamentController.display_ladder(tournament)
                case "3":
                    self.tournamentController.display_participant(tournament)
                case "4":
                    self.tournamentController.display_round(tournament)
                case "5":
                    tournament.delete()
                    break
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def match_result_menu(self, tournament):
        while True:
            match self.tournamentController.play_match(tournament):
                case "1":
                    tournament.play_match([1, 0])
                case "2":
                    tournament.play_match([0, 1])
                case "3":
                    tournament.play_match([0.5, 0.5])
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()
            if tournament.progress():
                self.tournamentController.end_tournament(tournament)
                return True

    def report_menu(self):
        while True:
            self.mainView.display_menu(menus["report"])
            match self.mainView.choice():
                case "1":
                    self.playerController.display_players()
                case "2":
                    self.tournamentController.display_tournaments()
                case "3":
                    players_list = self.playerController.load_all_players()
                    tournament = self.tournamentController.select_tournament(players_list)
                    if tournament:
                        self.tournamentController.display_tournament_date(tournament)
                case "4":
                    players_list = self.playerController.load_all_players()
                    tournament = self.tournamentController.select_tournament(players_list)
                    if tournament:
                        self.tournamentController.display_participant(tournament)
                case "5":
                    players_list = self.playerController.load_all_players()
                    tournament = self.tournamentController.select_tournament(players_list)
                    if tournament:
                        self.tournamentController.display_round(tournament)
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()
