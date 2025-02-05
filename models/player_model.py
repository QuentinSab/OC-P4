class PlayerModel:
    def __init__(
        self,
        last_name = "last_name",
        first_name =  "first_name",
        birth_date = "birth_date",
        national_id = "national_id",
        local_id = "local_id"
        ):
        
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.local_id = local_id
    
    @classmethod
    def json_to_player(self, json_data):
            return self(**json_data)

    def generate_local_id(json_data):
        used_ids = set()
        for player in json_data:
            used_ids.add(player["local_id"])
        local_id = 1
        while local_id in used_ids:
            local_id += 1
        return local_id

    def get_player_by_id(local_id, json_data):
        for player in json_data:
            if player["local_id"] == local_id:
                return player
        

class Tournament:
    pass

class Round:
    pass

class Match:
    pass