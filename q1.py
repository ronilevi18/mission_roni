class Invoice:
    def __init__(self, number, customer, amount, tax):
        self._number = number        # protected
        self.customer = customer
        self.amount = amount
        self.date = "2026-01-14"
        self.__tax = tax             # private

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, value):
        if value < 0:
            raise ValueError("Invalid tax")
        self.__tax = value

    def total(self):
        return self.amount * (1 + self.tax)

    def show(self):
        print("Invoice:", self._number)
        print("Customer:", self.customer)
        print("Total:", self.total())


number = int(input("Invoice number: "))
customer = input("Customer name: ")
amount = float(input("Amount: "))
tax = float(input("Tax rate (e.g. 0.17): "))

invoice = Invoice(number, customer, amount, tax)
invoice.show()

#שאלה 1 בתרגילים סעיף א + ב 

# סעיף ג מהי מטרת הכימוס
# מטרת הכימוס היא להגן על הנתונים הפנימיים של האובייקט מפני גישה ישירה מחוץ למחלקה,
# וכך למנוע שינויים בלתי מבוקרים שעלולים לגרום לאובייקט למצב לא תקין.
