def is_multiple(x, y):
    return x % y == 0 or y % x == 0

def main():
    while True:
        num1 = int(input("Enter first number"))
        if num1 == -1:
            break

        num2 = int(input("Enter second number"))
        if num2 == -1:
            break

        if is_multiple(num1, num2):
            print("One number is a multiple of the other")
        else:
            print("No number is a multiple of the other")

if __name__ == "__main__":
    main()

#שאלה 4 בתרגילים סעיף ב 