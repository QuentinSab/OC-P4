from models.tournament_model import TournamentModel
from views.tournament_view import TournamentView

class TournamentController:
    def __init__(self):
        self.tournamentView = TournamentView()

    def load_all_tournaments(self):
        return TournamentModel.load_all_tournaments()

    def display_tournaments(self):
        tournaments_list = TournamentModel.load_all_tournaments()
        self.tournamentView.display_tournaments(tournaments_list)
    
    def display_tournament_data(self, tournament):
        self.tournamentView.display_tournament_data(tournament)
        
    def add_tournament(self):
        name, place, description, round_number = self.tournamentView.get_tournament_data()
        TournamentModel.add_tournament(name, place, description, round_number)
            
    def add_participant(self, tournament, player):
        if player not in tournament.players:
            tournament.players.append(player)
            tournament.update()

    def display_participant(self, tournament):
        self.tournamentView.display_participant(tournament)

    def remove_participant(self, tournament):
        self.tournamentView.remove_participant(tournament)
        tournament.update()

    def select_tournament(self, players_list):
        tournaments_list = TournamentModel.load_all_tournaments()
        max_index = len(tournaments_list)
        selected_index = self.tournamentView.select_tournament_by_index(tournaments_list, max_index)
        if selected_index != None:
            tournament = tournaments_list[selected_index - 1]
            tournament.convert_rounds_to_objects()
            tournament.convert_ids_to_players(players_list)
            return tournament

    def modify_tournament(self, tournament, attribute):  
        setattr(tournament, attribute, self.tournamentView.modify_tournament())
        tournament.update()
    
    def launch_tournament(self, tournament):
        nombre_participants = len(tournament.players)
        if nombre_participants == 0:
            self.tournamentView.no_participant_error()
        elif nombre_participants %2:
            self.tournamentView.parity_error()
        else:
            tournament.launch()   
            self.tournamentView.launch_tournament()
            tournament.start_round()
            return True
    
    def display_ladder(self, tournament):
        ladder = tournament.get_ladder()
        player_ladder = []
        for ranked_player in ladder:
            for player in tournament.players:
                if ranked_player[0] == player.id:
                    ranked_player = (player, ranked_player[1])
                    player_ladder.append(ranked_player)
        self.tournamentView.display_ladder(player_ladder)

    def display_tournament_date(self, tournament):
        self.tournamentView.display_tournament_date(tournament)

    def play_match(self, tournament):
        round = tournament.rounds[tournament.current_round]
        match = round.matchs_list[round.current_match]
        player1, player2 = match[0][0], match[1][0]
        for player in tournament.players:
            if player.id == player1:
                player1 = player
            if player.id == player2:
                player2 = player

        return self.tournamentView.play_match(player1, player2)

    def display_round(self, tournament):
        self.tournamentView.display_round(tournament.get_named_rounds())

    def end_tournament(self, tournament):
        self.tournamentView.tournament_end(tournament)