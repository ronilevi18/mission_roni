from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.speak())
        else:
            print("Not an Animal")

if __name__ == "__main__":
    main()

#סעיף ג שאלה 3 בתרגילים
#מטרת הרב צורתיות היא לאפשר לאובייקטים מסוגים שונים להגיב לאותן קריאות מתודות בצורה שונה,
# מה שמאפשר גמישות רבה יותר בקוד ושימוש חוזר באלגוריתמים.