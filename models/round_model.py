from dataclasses import dataclass

@dataclass
class RoundModel:
    name: str
    start_date: str
    end_date: str
    current_match: int
    matchs_list: list

    def __init__(
        self,
        name="name",
        start_date="start_date",
        end_date="end_date",
        current_match=0,
        matchs_list=[]
    ):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.current_match = current_match
        self.matchs_list = matchs_list