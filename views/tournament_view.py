from views.utils import Utils


class TournamentView:
    def display_tournaments(self, tournaments_list):
        """Displays the list of tournaments"""
        Utils.clear()

        if not tournaments_list:
            print("Aucun tournoi enregistré.")
        else:
            for tournament in tournaments_list:
                print(
                    f"Nom : {tournament.name:<30} | "
                    f"Statut : {tournament.status:<12} | "
                    f"Lieu : {tournament.place}"
                )

        Utils.temporisation()

    def get_tournament_data(self):
        """Prompt the user to enter tournament informations and return them"""
        Utils.clear()

        name = input("Entrez le nom du tournoi: ")
        place = input("Entrez le lieu: ")
        description = input("Entrez la description: ")

        # Ensure a valid round number is entered
        while True:
            round_number = input("Entrez le nombre de tours: ")

            if round_number.isdigit() and round_number != "0":
                round_number = int(round_number)
                break
            else:
                Utils.clear()
                print("Entrez un nombre valide.")
                print("")

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

    def display_tournament_date(self, tournament):
        Utils.clear()

        print(f"Date de {tournament.name}")
        print("")

        if tournament.start_date:
            print(f"Date de début: {tournament.start_date}")

            if tournament.end_date:
                print(f"Date de fin: {tournament.end_date}")
            else:
                print("Le tournoi n'est pas terminé.")

        else:
            print("Le tournoi n'a pas commencé.")
        Utils.temporisation()

    def modify_tournament(self):
        """Prompt the user to enter a new value for a tournament's attribute and return it"""
        print("")
        new_value = input("Entrez la nouvelle valeur: ")
        print("")
        return new_value

    def select_tournament_by_index(self, tournaments_list, max_index):
        """Displays a numbered list of tournaments and returns the user choice"""
        Utils.clear()

        if not tournaments_list:
            print("Aucun tounoi enregistré.")
            Utils.temporisation()

        # Display a numbered list of tournaments
        else:
            print("Liste des tournois :")
            print("")

            for index, tournament in enumerate(tournaments_list, start=1):
                print(f"{index} : {tournament.name} - {tournament.status}")

            print("")
            # Loop to ensure a valid selection
            while True:
                choice = input(f"Sélectionnez un tournoi (1 à {max_index}) : ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= max_index:
                        return choice

    def display_participant(self, tournament):
        """Display the numbered list of tournament participants"""
        Utils.clear()

        if tournament.players:
            print(f"Participants de {tournament.name}")
            print("")

            for index, player in enumerate(tournament.players, start=1):
                print(f"{index} : {player.last_name} {player.first_name}")

        else:
            print("Aucun participant inscrit.")
        Utils.temporisation()

    def remove_participant(self, tournament):
        """Display the numbered list of participants and return the number of the selected player"""
        Utils.clear()

        # Display the numbered list of participants
        if tournament.players:
            print(f"Participants de {tournament.name}")
            print("")

            for index, player in enumerate(tournament.players, start=1):
                print(f"{index} : {player.last_name} {player.first_name}")

        else:
            print("Aucun participant inscrit.")
            Utils.temporisation()
            return None

        print("")
        # Loop to ensure a valid selection
        while True:
            chosen_player = input("Entrez le numéro du participant à supprimer : ")

            if chosen_player.isdigit():
                chosen_player = int(chosen_player) - 1
                if 0 <= chosen_player < len(tournament.players):
                    player_to_remove = tournament.players[chosen_player]
                    return player_to_remove

    def display_round(self, rounds):
        """Displays each round of the list"""
        Utils.clear()

        for round in rounds:
            print(round[0])

            for i, match in enumerate(round[1], start=1):
                (player1, score1), (player2, score2) = match

                print(
                    f"  Match {i}: {player1.last_name} {player1.first_name} ({score1}) - "
                    f"{player2.last_name} {player2.first_name} ({score2})"
                )

            print("")
        Utils.temporisation()

    def play_match(self, player1, player2):
        """Display a menu to select a match result and return the choice"""
        Utils.clear()

        print(f" {player1.last_name} {player1.first_name} affronte {player2.last_name} {player2.first_name}")
        print("")
        print(f"1 : Victoire de {player1.last_name} {player1.first_name}")
        print(f"2 : Victoire de {player2.last_name} {player2.first_name}")
        print("3 : Égalité")
        print("0 : Retour")
        print("")
        print("Choississez le résultat du match : ")
        return input()

    def display_ladder(self, ladder):
        """Display the numbered ranking"""
        Utils.clear()

        print("Classement")
        print("")
        print(f"{'Rang':<8} {'Joueur':<30} {'Score'}")
        print("")

        for i in range(0, len(ladder), 1):
            print(f"{i+1:<8} {ladder[i][0].last_name:<15} {ladder[i][0].first_name:<15} {ladder[i][1]}")
        Utils.temporisation()

    def launch_tournament(self):
        """Displays a message to inform the user that the tournament is starting"""
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
        """Displays a message to inform the user that the tournament is ending"""
        Utils.clear()
        print(f'Le tournoi "{tournament.name}" est terminé.')
        Utils.temporisation()
