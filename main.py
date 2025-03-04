from controllers.main_controller import MainController

if __name__ == "__main__":
    try:
        menu = MainController()
        menu.execution()
    except KeyboardInterrupt:
        print("Interruption de l'application")
