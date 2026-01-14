def is_multiple(x, y):
    if x == 0 or y == 0:
        return True
    return x % y == 0 or y % x == 0

def main():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))

    if is_multiple(num1, num2):
        print("One number is a multiple of the other")
    else:
        print("No number is a multiple of the other")

if __name__ == "__main__":
    main()
#שאלה 4 בתרגילים סעיף א 
