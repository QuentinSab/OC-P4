from models.json_model import JsonModel
from dataclasses import dataclass
import uuid

PLAYERS_JSON = "players.json"


@dataclass
class PlayerModel:
    last_name: str
    first_name: str
    birth_date: str
    national_id: str
    id: str

    def __init__(
        self,
        last_name="last_name",
        first_name="first_name",
        birth_date="birth_date",
        national_id="national_id",
        id=None,
    ):
        self.json_players = JsonModel(PLAYERS_JSON)
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.id = id if id else str(uuid.uuid4())

    def save(self):
        """Add the current player to the players file"""
        players_list = self.load_all_players()
        players_list.append(self)
        self.json_players.write_json(players_list)

    def delete(self):
        """Remove the current player from the players file"""
        players_list = self.load_all_players()

        for player in players_list:
            if player.id == self.id:
                players_list.remove(player)

        self.json_players.write_json(players_list)

    def update(self):
        """Based on id, replace the corresponding player in players file by the current player"""
        players_list = self.load_all_players()

        for player in players_list:
            if player.id == self.id:
                players_list.remove(player)
                players_list.append(self)

        self.json_players.write_json(players_list)

    def check_registration(self, tournaments_list):
        """Check if the player is registered in any ongoing or starting tournament"""
        for tournament in tournaments_list:
            if tournament.status != "finished":

                for participant in tournament.players:
                    if participant == self.id:
                        return True

    @staticmethod
    def load_all_players():
        """Load all players from the players file and sort them by last name and first name"""
        json_players = JsonModel(PLAYERS_JSON)
        players_list = json_players.read_json(PlayerModel)
        players_list = sorted(players_list, key=lambda player: (player.last_name.lower(), player.first_name.lower()))
        return players_list
