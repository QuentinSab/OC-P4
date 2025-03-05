from models.tournament_model import TournamentModel
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournamentView = TournamentView()

    def load_all_tournaments(self):
        """Return a list of all tournaments"""
        return TournamentModel.load_all_tournaments()

    def display_tournaments(self):
        """"Displays the list of all tournaments"""
        tournaments_list = TournamentModel.load_all_tournaments()
        self.tournamentView.display_tournaments(tournaments_list)

    def display_tournament_data(self, tournament):
        self.tournamentView.display_tournament_data(tournament)

    def add_tournament(self):
        """Add a tournament to the tournament file"""
        name, place, description, round_number = self.tournamentView.get_tournament_data()
        TournamentModel.add_tournament(name, place, description, round_number)

    def add_participant(self, tournament, player):
        if player not in tournament.players:
            tournament.players.append(player)
            tournament.update()

    def display_participant(self, tournament):
        self.tournamentView.display_participant(tournament)

    def remove_participant(self, tournament):
        player_to_remove = self.tournamentView.remove_participant(tournament)
        if player_to_remove:
            tournament.players.remove(player_to_remove)
            tournament.update()

    def select_tournament(self, players_list):
        """Display the list of tournaments and return the selected tournament"""
        tournaments_list = TournamentModel.load_all_tournaments()
        max_index = len(tournaments_list)

        # Display the list of numbered tournaments and retrieve the number of the chosen tournament
        selected_index = self.tournamentView.select_tournament_by_index(tournaments_list, max_index)

        if selected_index:
            # Retrieve the tournament corresponding to the number chosen
            tournament = tournaments_list[selected_index - 1]
            tournament.convert_rounds_to_objects()
            tournament.convert_ids_to_players(players_list)
            return tournament

    def modify_tournament(self, tournament, attribute):
        """Modify tournament information according to the given attribute"""
        setattr(tournament, attribute, self.tournamentView.modify_tournament())
        tournament.update()

    def launch_tournament(self, tournament):
        """Start the tournament"""
        nombre_participants = len(tournament.players)

        # Check that the number of participants is valid
        if nombre_participants == 0:
            self.tournamentView.no_participant_error()

        elif nombre_participants % 2:
            self.tournamentView.parity_error()

        else:
            tournament.launch()
            self.tournamentView.launch_tournament()
            tournament.start_round()
            return True

    def display_ladder(self, tournament):
        """Display the ranking and score of tournament participants"""
        # Retrieve the ranking in a list of tuples (player_id, score)
        ladder = tournament.get_ladder()
        player_ladder = []

        # Add to the list each player object corresponding players ids in ladder with its score
        for ranked_player in ladder:
            for player in tournament.players:
                if ranked_player[0] == player.id:
                    ranked_player = (player, ranked_player[1])
                    player_ladder.append(ranked_player)

        self.tournamentView.display_ladder(player_ladder)

    def display_tournament_date(self, tournament):
        self.tournamentView.display_tournament_date(tournament)

    def play_match(self, tournament):
        """Display the match to be played and return the selected result"""
        # Retrieve the match to be played
        round = tournament.rounds[tournament.current_round]
        match = round.matchs_list[round.current_match]

        # Retrieve players objects of players id playing the match
        player1, player2 = match[0][0], match[1][0]
        for player in tournament.players:
            if player.id == player1:
                player1 = player
            if player.id == player2:
                player2 = player

        return self.tournamentView.play_match(player1, player2)

    def display_round(self, tournament):
        """Display all matches from rounds played and from the current round of the tournament"""
        self.tournamentView.display_round(tournament.get_named_rounds())

    def end_tournament(self, tournament):
        self.tournamentView.tournament_end(tournament)
