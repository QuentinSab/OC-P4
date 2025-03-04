from views.utils import Utils

class MainView:
    def choice(self):
        print("")
        option = input("Choisissez une option : ")
        return option

    def display_error_menu(self):
        print("")
        print("Entrée invalide.")
        print("Sélectionnez une option en entrant son numéro.")
        Utils.temporisation()

    def display_menu(self, menu, **kwargs):
        target = kwargs.get("target")
        Utils.clear()
        
        if target:
            print(f"--- {menu['title']}{target}---")
        else:
            print(f"--- {menu['title']} ---")
            
        print("")
        for key, option in menu["options"].items():
            print(f"{key} : {option}")
