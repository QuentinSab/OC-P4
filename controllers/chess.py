from models.data_objects import Player
from models.chess import PlayersModel
from views.chess import MainView, TournamentsView, PlayersView

class MainController:
    def __init__(self):
        self.mainView = MainView()
        self.playerView = PlayersView()
        self.tournamentView = TournamentsView()
    
    def execution(self):
        self.mainView.clear_menu()
        while True:
            match self.create_menu(self.mainView.main_menu):
                case "1":
                    self.players_menu()
                case "2":
                    self.tournaments_menu()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def create_menu(self, menu, menu_target = ""):
        self.mainView.create_menu(menu, menu_target)
        option = self.mainView.choice()
        self.mainView.clear_menu()
        return option

    def players_menu(self):
        while True:
            match self.create_menu(self.playerView.players_menu):
                case "1":
                    pass    #Lister joueurs
                case "2":
                    pass    #Ajouter joueur
                case "3":
                    self.player_modification_menu()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def player_modification_menu(self):
        #player = self.view.select_player()
        while True:
            match self.create_menu(self.playerView.modification_menu, menu_target = "Obelix"):
                case "1":
                    pass    #Changer nom de famille
                case "2":
                    pass    #Changer prénom
                case "3":
                    pass    #Changer date de naissance
                case "4":
                    pass    #Changer identifiant national
                case "5":
                    pass    #player = self.view.select_player()
                case "6":
                    pass    #Supprimer joueur
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def tournaments_menu(self):
        while True:
            match self.create_menu(self.tournamentView.tournaments_menu):
                case "1":
                    pass    #Lister tournois
                case "2":
                    pass    #Créer tournoi
                case "3":
                    self.manager_tournament_menus()
                case "0":
                    break
                case _:
                    self.mainView.display_error_menu()

    def manager_tournament_menus(self):
        """Determine which menu use according to the selected tournament status."""
        #tournament = self.view.select_tournament()
        match "finished": #tournament.status
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
            match self.create_menu(self.tournamentView.starting_tournament_menu, menu_target = "Championnat Régional"):
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
            match self.create_menu(self.tournamentView.ongoing_tournament_menu, menu_target = "Championnat Régional"):
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
            match self.create_menu(self.tournamentView.finished_tournament_menu, menu_target = "Championnat Régional"):
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

class PlayersController:
    pass

class Rapport:
    pass

class Tournoi:
    pass