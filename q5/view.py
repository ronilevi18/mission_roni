from .person import Person


class View:
    def show_menu(self) -> None:
        print("\n=== People Manager ===")
        print("1) Add person")
        print("2) Show all people")
        print("0) Exit")

    def read_choice(self) -> str:
        return input("Choose an option: ").strip()

    def read_person(self) -> Person:
        name = input("Name: ").strip()
        address = input("Address: ").strip()
        phone = input("Phone: ").strip()
        return Person(name=name, address=address, phone=phone)

    def show_message(self, message: str) -> None:
        print(message)

    def show_people(self, people: list) -> None:
        if not people:
            print("No people found.")
            return

        print("\n--- People List ---")
        for i, p in enumerate(people, start=1):
            print(f"{i}. Name: {p.name} | Address: {p.address} | Phone: {p.phone}")
