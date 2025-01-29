class MainView:  
    def main_menu(self):
        print("")
        print("--- Menu Principal ---")
        print("1 : Gestion des joueurs")
        print("2 : Gestion des tournois")
        print("0 : Quitter")

    def choice(self):
        print ("")
        option = input("Choisissez une option : ")
        return option

    def display_error_menu(self):
        print("Sélectionnez une option en entrant son numéro.")


class PlayersView:
    def players_menu(self):
        print("")
        print("--+ Gestion des joueurs +--")
        print("1 : Lister les joueurs")
        print("2 : Ajouter un joueur")
        print("3 : Modifier un joueur")
        print("0 : Retour")

    def player_modification_menu(self, player_firstname, player_lastname):
        print("")
        print(f"-++ Modification de {player_firstname} {player_lastname} ++-")
        print("1 : Changer le nom de famille")
        print("2 : Changer le prénom")
        print("3 : Changer la date de naissance")
        print("4 : Changer l'identifiant national")
        print("5 : Changer de joueur")
        print("6 : Supprimer le joueur")
        print("0 : Retour")

class TournamentsView:
    def tournaments_menu(self):
        print("")
        print("--+ Gestion des tournois +--")
        print("1 : Lister les tournois")
        print("2 : Créer un tournoi")
        print("3 : Gérer un tournoi")
        print("0 : Retour")

    def starting_tournament_menu(self, tournament_name):
        print("")
        print(f"-++ Gestion de {tournament_name} ++-")
        print("1 : Voir les informations du tournoi")
        print("2 : Changer le nom du tournoi")
        print("3 : Changer le lieu du tournoi")
        print("4 : Changer la description du tournoi")
        print("5 : Lister les participants")
        print("6 : Ajouter un participant")
        print("7 : Retirer un participant")
        print("8 : Démarrer le tournoi")
        print("9 : Annuler le tournoi")
        print("0 : Retour")

    def ongoing_tournament_menu(self, tournament_name):
        print("")
        print(f"-++ Gestion de {tournament_name} ++-")
        print("1 : Voir les informations du tournoi")
        print("2 : Voir le classement")
        print("3 : Voir le tour en cours")
        print("4 : Jouer un match")
        print("5 : Arrêter le tournoi")
        print("0 : Retour")
    
    def finished_tournament_menu(self, tournament_name):
        print("")
        print(f"-++ Gestion de {tournament_name} ++-")
        print("1 : Voir les informations du tournoi")
        print("2 : Voir le classement")
        print("3 : Effacer le tournoi")
        print("0 : Retour")