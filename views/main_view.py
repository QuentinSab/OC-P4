import os

class MainView:
    def __init__(self):
        self.main_menu = (
            "Menu Principal",
            "Gestion des joueurs",
            "Gestion des tournois",
            "Quitter"
        )

    def choice(self):
        print ("")
        option = input("Choisissez une option : ")
        return option

    def display_error_menu(self):
        print("Sélectionnez une option en entrant son numéro.")
        print("")

    def clear_menu(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def create_menu(self, menu_line, menu_target):
        # Display menu title
        print(f"--- {menu_line[0]}{menu_target} ---")  
        print("")
        # Display menu options
        line_number = 1
        for option in menu_line[1:-1]:
            print(f"{line_number} : {option}")
            line_number += 1
        print(f"0 : {menu_line[-1]}")