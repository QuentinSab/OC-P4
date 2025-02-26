from models.tournament_model import TournamentModel
from views.tournament_view import TournamentView

from views.utils import Utils###

class TournamentController:
    def __init__(self):
        self.tournamentView = TournamentView()
        
    def display_tournaments(self):
        tournaments_list = TournamentModel.load_all_tournaments()
        self.tournamentView.display_tournaments(tournaments_list)
    
    def display_tournament_data(self, tournament):
        self.tournamentView.display_tournament_data(tournament)
        
    def add_tournament(self):
        name, place, description, round_number = self.tournamentView.get_tournament_data()
        TournamentModel.add_tournament(name, place, description, round_number)
            
    def add_participant(self, tournament, player_id):
        if player_id not in tournament.players:
            tournament.players.append(player_id)
            tournament.update()

    def display_participant(self, tournament, players_list):
        self.tournamentView.display_participant(tournament.get_participants(players_list))

    def remove_participant(self, tournament, players_list):
        self.tournamentView.remove_participant(tournament, tournament.get_participants(players_list))
        tournament.update()

    def select_tournament(self):
        tournaments_list = TournamentModel.load_all_tournaments()
        max_index = len(tournaments_list)
        selected_index = self.tournamentView.select_tournament_by_index(tournaments_list, max_index)
        if selected_index != None:
            tournament = tournaments_list[selected_index - 1]
            tournament.convert_rounds()
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
    
    def display_ladder(self, tournament, players_list):
        participants = tournament.get_participants(players_list)
        ladder = tournament.get_ladder()
        named_ladder = []
        for player_id, score in ladder:
            for participant in participants:
                if participant.id == player_id:
                    name = participant.last_name + " " + participant.first_name
                    named_ladder.append((name, score))
        self.tournamentView.display_ladder(named_ladder)

    def play_match(self, tournament):
        round = tournament.rounds[tournament.current_round]
        match = round.matchs_list[round.current_match]
        player1, player2 = match[0][0], match[1][0]
        return self.tournamentView.play_match(player1, player2)

    def display_round(self, round):
        self.tournamentView.display_unique_round(round)

    def end_tournament(self, tournament):
        self.tournamentView.tournament_end(tournament)