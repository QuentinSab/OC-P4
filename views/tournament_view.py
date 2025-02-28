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
            "Voir les participants",
            "Voir le tour en cours",
            "Jouer les matchs",
            "Arrêter le tournoi",
            "Retour"
        )

        self.finished_tournament_menu = (
            "Gestion de ",
            "Voir les informations du tournoi",
            "Voir le classement",
            "Voir les participants",
            "Voir le tour en cours",
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
                    f"Lieu : {tournament.place}"
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
        print(f"Round actuel: {tournament.current_round + 1}")
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
                print(f"{index} : {tournament.name} - {tournament.status}")
            print("")

            while True:
                choice = int(input(f"Sélectionnez un tournoi (1 à {max_index}) : "))
                if 1 <= choice <= max_index:
                    return choice

    def display_participant(self, tournament):
        Utils.clear()
        if tournament.players:
            print("Participants du Tournoi")
            print("")
            for index, player in enumerate(tournament.players, start = 1):
                print(f"{index} : {player.last_name} {player.first_name}")
        else:
            print("Aucun participant inscrit.")
        Utils.temporisation()

    def remove_participant(self, tournament):
        Utils.clear()
        if tournament.players:
            print("Participants du Tournoi")
            print("")
            for index, player in enumerate(tournament.players, start = 1):
                print(f"{index} : {player.last_name} {player.first_name}")
        else:
            print("Aucun participant inscrit.")
            Utils.temporisation()
            return None
        print("")
        while True:
            chosen_player = int(input("Entrez le numéro du participant à supprimer : ")) - 1
            if 0 <= chosen_player < len(tournament.players):
                player_to_remove = tournament.players[chosen_player]
                tournament.players.remove(player_to_remove)
                break

    def display_round(self, rounds):
        Utils.clear()
        for round in rounds:
            print(round[0])
            for i, match in enumerate(round[1], start=1):
                (player1, score1), (player2, score2) = match
                print(f"  Match {i}: {player1.last_name} {player1.first_name} ({score1}) - {player2.last_name} {player2.first_name} ({score2})")
            print("")
        Utils.temporisation()
        
    def play_match(self, player1, player2):
        Utils.clear()
        print(f" {player1.last_name} {player1.first_name} affronte {player2.last_name} {player2.first_name}")
        print("")
        print(f"1 : Victoire de {player1.last_name} {player1.first_name}")
        print(f"2 : Victoire de {player2.last_name} {player2.first_name}")
        print(f"3 : Égalité")
        print(f"0 : Retour")
        print("")
        print("Choississez le résultat du match : ")
        return input()

    def display_ladder(self, ladder):
        Utils.clear()
        print("Classement")
        print("")
        print(f"{'Rang':<8} {'Joueur':<30} {'Score'}")
        print("")
        for i in range(0, len(ladder), 1):
            print(f"{i+1:<8} {ladder[i][0].last_name:<15} {ladder[i][0].first_name:<15} {ladder[i][1]}")
        Utils.temporisation()

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
    
    def tournament_end(self, tournament):
        Utils.clear()
        print(f"Le tournoi \"{tournament.name}\" est terminé.")
        Utils.temporisation()