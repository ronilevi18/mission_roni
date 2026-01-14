class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def main():
    animals = [Dog(), Cat()]

    for animal in animals:
        print(animal.speak())

if __name__ == "__main__":
    main()

#סעיף א שאלה 3 בתרגילים
#סעיף ב המשך שאלה מילולית 
#“אם זה נראה כמו ברווז…” – למה הכוונה?
# הכוונה היא שאם אובייקט מתנהג כמו סוג מסוים של אובייקט (למשל, ברווז),
# אז ניתן להשתמש בו באותו אופן, גם אם הוא לא ממש שייך לאותו סוג.
# כלומר, ההתנהגות חשובה יותר מהסוג המפורש של האובייקט.