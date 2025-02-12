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
            if not tournaments_list:
                print("Aucun tournoi enregistré.")
                print("")
                return

            for tournament in tournaments_list:
                print(
                    f"ID : {tournament.id} | "
                    f"Nom : {tournament.name} | "
                    f"Statut : {tournament.status} | "
                    f"Lieu : {tournament.place} | "
                )
            print("")

    def get_tournament_data(self):
        name = input("Entrez le nom du tournoi: ")
        place = input("Entrez le lieu: ")
        description = input("Entrez la description: ")
        round_number = input("Entrez le nombre de tours: ")
        return name, place, description, round_number