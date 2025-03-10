from views.utils import Utils


class PlayerView:
    def display_players(self, players_list):
        """Display data for each player in the list"""
        Utils.clear()

        if not players_list:
            print("Aucun joueur enregistré.")
        else:
            for player in players_list:
                print(
                    f"Nom : {player.last_name:<15} | "
                    f"Prénom : {player.first_name:<15} | "
                    f"Date de naissance : {player.birth_date:<12} | "
                    f"ID National : {player.national_id}"
                )
        Utils.temporisation()

    def get_player_data(self):
        """Prompt the user to enter player informations and return them"""
        Utils.clear()

        last_name = input("Entrez le nom de famille: ")
        first_name = input("Entrez le prénom: ")
        birth_date = input("Entrez la date de naissance (JJ/MM/AAAA): ")
        national_id = input("Entrez l'ID national: ")

        return last_name, first_name, birth_date, national_id

    def modify_player(self):
        """Prompt the user to enter a new value for a player's attribute and return it"""
        print("")
        new_value = input("Entrez la nouvelle valeur: ")
        print("")
        return new_value

    def select_player_by_index(self, players_list, max_index):
        """Displays a numbered list of players and returns the user choice"""
        Utils.clear()

        if not players_list:
            print("Aucun joueur enregistré.")
            Utils.temporisation()

        # Display a numbered list of players
        else:
            print("Liste des joueurs :")
            print("")
            for index, player in enumerate(players_list, start=1):
                print(f"{index:<4}: {player.last_name:<15} {player.first_name}")
            print("")

            # Loop to ensure a valid selection
            while True:
                choice = input(f"Sélectionnez un joueur (1 à {max_index}) : ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= max_index:
                        return choice

    def delete_registered_error(self, player):
        Utils.clear()
        print(f"{player.last_name} {player.first_name} joue dans un tournoi.")
        print("La suppression est impossible.")
        Utils.temporisation()
