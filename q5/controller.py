
from .view import View
from .model import Model


class Controller:
    def __init__(self, model: Model):
        self.model = model

    def run(self) -> None:
        view = View()  

        while True:
            view.show_menu()
            choice = view.read_choice()

            if choice == "1":
                person = view.read_person()
                self.model.add(person)
                view.show_message("Person avoided successfully.")  
            elif choice == "2":
                people = self.model.get_all()
                view.show_people(people)
            elif choice == "0":
                view.show_message("Goodbye!")
                break
            else:
                view.show_message("Invalid choice. Try again.")
