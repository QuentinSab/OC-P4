from views.utils import Utils

class TournamentView:
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

    def display_tournaments(self, tournaments_list):
        Utils.clear()
        if not tournaments_list:
            print("Aucun tournoi enregistré.")
        else:
            for tournament in tournaments_list:
                print(
                    f"ID : {tournament.id} | "
                    f"Nom : {tournament.name} | "
                    f"Statut : {tournament.status} | "
                    f"Lieu : {tournament.place} | "
                )
        Utils.temporisation()

    def get_tournament_data(self):
        Utils.clear()
        name = input("Entrez le nom du tournoi: ")
        place = input("Entrez le lieu: ")
        description = input("Entrez la description: ")
        round_number = input("Entrez le nombre de tours: ")
        return name, place, description, round_number
    
    def display_tournament_data(self, tournament):
        Utils.clear()
        print("Détails du Tournoi")
        print("")
        print(f"ID: {tournament.id}")
        print(f"Nom: {tournament.name}")
        print(f"Statut: {tournament.status}")
        print(f"Lieu: {tournament.place}")
        print(f"Description: {tournament.description}")
        print(f"Date de début: {tournament.start_date}")
        print(f"Date de fin: {tournament.end_date}")
        print(f"Nombre de rounds: {tournament.round_number}")
        print(f"Round actuel: {tournament.current_round}")
        print("")
        print("Rounds")
        if tournament.rounds:
            for i, round_data in enumerate(tournament.rounds, 1):
                print(f"Round {i}: {round_data}")
        else:
            print("Aucun round enregistré.")
        print("")
        print("Participants")
        if tournament.players:
            for i, player in enumerate(tournament.players, 1):
                print(f"Joueur {i}: {player}")
        else:
            print("Aucun participant enregistré.")
        Utils.temporisation()
    
    def modify_tournament(self):
        print("")
        new_value = input("Entrez la nouvelle valeur: ")
        print("")
        return new_value

    def select_tournament_by_index(self, tournaments_list, max_index):
        Utils.clear()
        if not tournaments_list:
            print("Aucun tounoi enregistré.")
            Utils.temporisation()
        else:   
            print("Liste des tournois :")
            print("")
            for index, tournament in enumerate(tournaments_list, start=1):
                print(f"{index} : {tournament.name} ")
            print("")

            while True:
                choice = int(input(f"Sélectionnez un tournoi (1 à {max_index}) : "))
                if 1 <= choice <= max_index:
                    return choice

    def display_participant(self, participants):
        Utils.clear()
        if participants:
            print("Participants du Tournoi")
            print("")
            for index, player in enumerate(participants, start = 1):
                print(f"{index} : {player.last_name} {player.first_name}")
        else:
            print("Aucun participant inscrit.")
        Utils.temporisation()

    def remove_participant(self, tournament, participants):
        Utils.clear()
        if participants:
            print("Participants du Tournoi")
            print("")
            for index, player in enumerate(participants, start = 1):
                print(f"{index} : {player.last_name} {player.first_name}")
        else:
            print("Aucun participant inscrit.")
            Utils.temporisation()
            return None
        print("")
        while True:
            chosen_player = int(input("Entrez le numéro du participant à supprimer : ")) - 1
            if 0 <= chosen_player < len(tournament.players):
                player_id_to_remove = participants[chosen_player].id 
                tournament.players.remove(player_id_to_remove)
                break

    def launch_tournament(self):
        Utils.clear()
        print("Le tournoi commence.")
        Utils.temporisation()

    def parity_error(self):
        Utils.clear()
        print("Le tournoi ne peut pas commencer.")
        print("Le nombre de participants n'est pas pair.")
        Utils.temporisation()

    def no_participant_error(self):
        Utils.clear()
        print("Le tournoi ne peut pas commencer.")
        print("Aucun joueur ne participe au tournoi.")
        Utils.temporisation()