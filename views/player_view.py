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
        if not players_list:
            print("Aucun joueur enregistré.")
            return

        for player in players_list:
            print(
                f"ID : {player['local_id']} | "
                f"Nom : {player['last_name']} | "
                f"Prénom : {player['first_name']} | "
                f"Date de naissance : {player['birth_date']} | "
                f"ID National : {player['national_id']}"
            )
        print("")

    def get_player_data(self):
        last_name = input("Entrez le nom de famille: ")
        first_name = input("Entrez le prénom: ")
        birth_date = input("Entrez la date de naissance (JJ/MM/AAAA): ")
        national_id = input("Entrez l'ID national: ")
        return last_name, first_name, birth_date, national_id
