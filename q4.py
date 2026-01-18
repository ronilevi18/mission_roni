class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def describe(self):
        return f"{self.name}, {self.country} (population: {self.population})"


class Marina(City):
    def __init__(self, name, country, population, docks_count):
        super().__init__(name, country, population)
        self.docks_count = docks_count

    def marina_info(self):
        return f"Marina docks: {self.docks_count}"


class Park(City):
    def __init__(self, name, country, population, area_km2):
        super().__init__(name, country, population)
        self.area_km2 = area_km2

    def park_info(self):
        return f"Park area: {self.area_km2} km^2"


class Amphitheater(City):
    def __init__(self, name, country, population, seats):
        super().__init__(name, country, population)
        self.seats = seats

    def amphitheater_info(self):
        return f"Amphitheater seats: {self.seats}"


def main():
    
    name = input("Enter city name for Marina: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    docks = int(input("Enter docks count: "))
    m = Marina(name, country, population, docks)

    print("\n--- Marina Object ---")
    print(m.describe())
    print(m.marina_info())

    name = input("\nEnter city name for Park: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    area = float(input("Enter park area (km^2): "))
    p = Park(name, country, population, area)

    print("\n--- Park Object ---")
    print(p.describe())
    print(p.park_info())

   
    name = input("\nEnter city name for Amphitheater: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    seats = int(input("Enter seats count: "))
    a = Amphitheater(name, country, population, seats)

    print("\n--- Amphitheater Object -")
    print(a.describe())
    print(a.amphitheater_info())


if __name__ == "__main__":
    main()


#שאלה 2 בתרגילים סעיף א + ב + ג 
#סעיף ד מהי מטרת הורשה 
# הורשה היא מנגנון בתכנות מונחה עצמים המאפשר למחלקה חדשה (מחלקת בת) לרשת תכונות והתנהגויות ממחלקה קיימת (מחלקת אב).
# משתמשים בה כדי לקדם קוד חוזר, לארגן את הקוד בצורה היררכית וליצור מערכות גמישות וניתנות להרחבה. תוצאות ההורשה מאפשרות למחלקות הבת להשתמש בקוד של מחלקות האב מבלי לכתוב אותו מחדש,