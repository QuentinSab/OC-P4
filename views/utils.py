import os


class Utils:

    @staticmethod
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def temporisation():
        print("")
        input("Entrée pour revenir au menu...")
