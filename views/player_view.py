from views.utils import Utils

class PlayerView:
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

    def display_players(self, players_list):
        Utils.clear()
        if not players_list:
            print("Aucun joueur enregistré.")
        else:
            for player in players_list:
                print(
                    f"ID : {player.id:<40} | "
                    f"Nom : {player.last_name:<15} | "
                    f"Prénom : {player.first_name:<15} | "
                    f"Date de naissance : {player.birth_date:<12} | "
                    f"ID National : {player.national_id}"
                )
        Utils.temporisation()

    def get_player_data(self):
        Utils.clear()
        last_name = input("Entrez le nom de famille: ")
        first_name = input("Entrez le prénom: ")
        birth_date = input("Entrez la date de naissance (JJ/MM/AAAA): ")
        national_id = input("Entrez l'ID national: ")
        return last_name, first_name, birth_date, national_id

    def modify_player(self):
        print("")
        new_value = input("Entrez la nouvelle valeur: ")
        print("")
        return new_value

    def select_player_by_index(self, players_list, max_index):
        Utils.clear()
        if not players_list:
            print("Aucun joueur enregistré.")
            Utils.temporisation()
        else:   
            print("Liste des joueurs :")
            print("")
            for index, player in enumerate(players_list, start=1):
                print(f"{index:<4}: {player.last_name:<15} {player.first_name}")
            print("")

            while True:
                choice = int(input(f"Sélectionnez un joueur (1 à {max_index}) : "))
                if 1 <= choice <= max_index:
                    return choice
