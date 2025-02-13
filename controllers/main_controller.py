from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

from models.json_model import JsonModel

from views.main_view import MainView

class MainController:
    def __init__(self):
        self.json_tournaments = JsonModel("tournaments.json")

        self.playerController = PlayerController()
        self.tournamentController = TournamentController(self.json_tournaments)

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
                    if player == None:
                        break
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
        match tournament.status:
            case "starting":
                self.starting_tournament_menu()
            case "ongoing":
                self.ongoing_tournament_menu()
            case "finished":
                self.finished_tournament_menu()
            case _:
                pass
 
    def starting_tournament_menu(self):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.starting_tournament_menu, menu_target = "Championnat Régional"):
                case "1":
                    pass    #Voir informations tournoi
                case "2":
                    pass    #Changer nom tounoi
                case "3":
                    pass    #Changer lieu tournoi
                case "4":
                    pass    #Changer description tournoi
                case "5":
                    pass    #Lister participants
                case "6":
                    pass    #Ajouter participant
                case "7":
                    pass    #Retirer participant
                case "8":
                    pass    #Démarrer tournoi
                case "9":
                    pass    #Annuler tournoi
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def ongoing_tournament_menu(self):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.ongoing_tournament_menu, menu_target = "Championnat Régional"):
                case "1":
                    pass    #Voir informations tournoi
                case "2":
                    pass    #Voir classement
                case "3":
                    pass    #Voir tour
                case "4":
                    pass    #Jouer match
                case "5":
                    pass    #Arrete tournoi
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def finished_tournament_menu(self):
        while True:
            match self.display_menu(self.tournamentController.tournamentView.finished_tournament_menu, menu_target = "Championnat Régional"):
                case "1":
                    pass    #Voir informations tournoi
                case "2":
                    pass    #Voir classement
                case "3":
                    pass    #Effacer tournoi
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()
