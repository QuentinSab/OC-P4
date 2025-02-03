import os


class MainView:
    def __init__(self):
        self.main_menu = (
            "Menu Principal",
            "Gestion des joueurs",
            "Gestion des tournois",
            "Quitter"
        )

    def choice(self):
        print ("")
        option = input("Choisissez une option : ")
        return option

    def display_error_menu(self):
        print("Sélectionnez une option en entrant son numéro.")
        print("")

    def clear_menu(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def create_menu(self, menu_line, menu_target):
        # Display menu title
        print(f"--- {menu_line[0]}{menu_target} ---")  
        print("")
        # Display menu options
        line_number = 1
        for option in menu_line[1:-1]:
            print(f"{line_number} : {option}")
            line_number += 1
        print(f"0 : {menu_line[-1]}")

class PlayersView:
    def __init__(self):
        self.players_menu = (
            "Gestion des joueurs",
            "Lister les joueurs",
            "Ajouter un joueur",
            "Modifier un joueur",
            "Retour"
        )
        self.modification_menu = (
            "Modification de ",
            "Changer le nom de famille",
            "Changer le prénom",
            "Changer la date de naissance",
            "Changer l'identifiant national",
            "Changer de joueur",
            "Supprimer le joueur",
            "Retour"
        )

class TournamentsView:
    def __init__(self):
        self.tournaments_menu = (
            "Gestion des tournois",
            "Lister les tournois",
            "Créer un tournoi",
            "Gérer un tournoi",
            "Retour"
        )

        self.starting_tournament_menu = (
            "Gestion de ",
            "Voir les informations du tournoi",
            "Changer le nom du tournoi",
            "Changer le lieu du tournoi",
            "Changer la description du tournoi",
            "Lister les participants",
            "Ajouter un participant",
            "Retirer un participant",
            "Démarrer le tournoi",
            "Annuler le tournoi",
            "Retour"
        )

        self.ongoing_tournament_menu = (
            "Gestion de ",
            "Voir les informations du tournoi",
            "Voir le classement",
            "Voir le tour en cours",
            "Jouer un match",
            "Arrêter le tournoi",
            "Retour"
        )

        self.finished_tournament_menu = (
            "Gestion de ",
            "Voir les informations du tournoi",
            "Voir le classement",
            "Effacer le tournoi",
            "Retour"
        )
