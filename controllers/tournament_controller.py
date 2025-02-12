from models.tournament_model import TournamentModel
from views.tournament_view import TournamentView

class TournamentController:
    def __init__(self, tournament_file):
        self.json_tournaments = tournament_file
        self.tournamentView = TournamentView()
        
    def display_tournaments(self):
        tournaments_list = self.json_tournaments.read_json(TournamentModel)
        self.tournamentView.display_tournaments(tournaments_list)
        
    def add_tournament(self):
        name, place, description, round_number = self.tournamentView.get_tournament_data()
        tournaments_list = self.json_tournaments.read_json(TournamentModel)
        id = self.json_tournaments.generate_id(tournaments_list)
        new_tournament = TournamentModel(name, "status", place, description, "start_date", "end_date", id, int(round_number))
        self.json_tournaments.append_json(new_tournament)
        
    def select_tournament(self):
        self.display_tournaments()
        id = self.tournamentView.select_tournament()
        tournaments_list = self.json_tournaments.read_json(TournamentModel)
        tournament = self.json_tournaments.get_object_by_id(id, tournaments_list)
        if tournament == None:
            self.tournamentView.no_tournament_find()
        else:
            return tournament