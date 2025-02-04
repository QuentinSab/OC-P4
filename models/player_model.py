class PlayerModel:
    def __init__(self, last_name, first_name, birth_date, national_id, local_id):
        
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.local_id = local_id
    
    @classmethod
    def json_to_player(self, json_data):
            return self(**json_data)

class Tournament:
    pass

class Round:
    pass

class Match:
    pass