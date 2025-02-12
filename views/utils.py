import os

class Utils:
    
    @staticmethod
    def clear_menu():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    @staticmethod
    def temporisation():
        input("Entrer pour revenir au menu...")