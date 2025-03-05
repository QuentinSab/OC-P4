from views.utils import Utils


class MainView:
    def choice(self):
        """Prompt the user to select an option and return the input"""
        print("")
        option = input("Choisissez une option : ")
        return option

    def display_error_menu(self):
        """Display an error message for invalid input"""
        print("")
        print("Entrée invalide.")
        print("Sélectionnez une option en entrant son numéro.")
        Utils.temporisation()

    def display_menu(self, menu, **kwargs):
        """Display a menu with a title and options"""
        target = kwargs.get("target")
        Utils.clear()

        # Display the menu title, with a target if specified
        if target:
            print(f"--- {menu['title']}{target} ---")
        else:
            print(f"--- {menu['title']} ---")

        print("")
        # Print each option in the menu
        for key, option in menu["options"].items():
            print(f"{key} : {option}")
