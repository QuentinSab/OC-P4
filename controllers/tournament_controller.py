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
        tournament = TournamentModel(
            name=name,
            status="starting",
            place=place,
            description=description,
            start_date="start_date",
            end_date="end_date",
            round_number=round_number,
            current_round=0,
            rounds=[],
            players=[]
        )
        tournament.save()

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
            return tournaments_list[selected_index - 1]

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
        ladder = tournament.name_ladder_ids(tournament.get_ladder(), participants)
        self.tournamentView.display_ladder(ladder)

    def play_match(self, tournament):
        tournament.play_match()
        if tournament.progress() == True:
            self.tournamentView.tournament_end(tournament)
            return True

    def display_round(self, round):
        self.tournamentView.display_round(round)