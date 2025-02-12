class TournamentModel:
    def __init__(
        self,
        name = "name",
        status = "status",
        place = "place",
        description =  "description",
        start_date = "start_date",
        end_date = "end_date",
        id = "id",
        round_number = 4,
        current_round = "current_round",
        rounds = None,
        players = None
        
        ):
    
        self.name = name
        self.status = status
        self.place = place
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.id = id
        self.round_number = round_number
        self.current_round = current_round
        self.rounds = []
        self.players = []