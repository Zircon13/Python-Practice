def produc_sum():
    while True:
        try:
            numOne = int(input("Enter a number: "))
            numTwo = int(input("Enter a number: "))
            result = numOne * numTwo
            length = len(str(result))
            print(f"Product: {result}")
            print(f'Length: {length}')
            continue_choice = input("Do you want to continue? (y/n): ").lower()
            if continue_choice != 'y':
                break
        except ValueError:
            print("Please enter valid integers.")


def divisible_by_7():
    try:
        number = int(input("Enter a number: "))
        for num in range(1, number + 1):
            if num % 7 == 0:
                print(num)
    except ValueError:
        print("Please enter a valid integer.")


def hourglass():
        row = int(input("Enter a row: "))

        if row % 2 == 0:
            print("Try again")
            print(row)
        else:

            for i in range(row, 0, -1):
                print(" " * (row - i) + "*" * (2 * i - 1))
            for i in range(2, row + 1):
                print(" " * (row - i) + "*" * (2 * i - 1))



def ecounter():
    def counter_for_number(n):
        match n:
            case 50:
                return "fifty"
            case 51:
                return "fifty-one"
            case 53:
                return "fifty-three"
            case 54:
                return "fifty-four"
            case 55:
                return "fifty-five"
            case 56:
                return "fifty-six"
            case 57:
                return "fifty-seven"
            case 58:
                return "fifty-eight"
            case 59:
                return "fifty-nine"
            case 60:
                return "sixty"
            case 61:
                return "sixty-one"
            case 62:
                return "sixty-two"
            case 63:
                return "sixty-three"
            case 64:
                return "sixty-four"
            case 65:
                return "sixty-five"
            case 66:
                return "sixty-six"
            case 67:
                return "sixty-seven"
            case 68:
                return "sixty-eight"
            case 69:
                return "sixty-nine"
            case 70:
                return "seventy"
            case _:
                return "Unknown"  # Default case

    for i in range(50, 71):
        word = counter_for_number(i)
        counter = word.count("e")
        print(f"Number {i} ({word}): {counter} 'e' letters")


def main():
    while True:
        print("\n-----------------------------------------------------------------")
        print("Choose an option:")
        print("1. Product and Length")
        print("2. Divisible by 7")
        print("3. Hourglass Pattern")
        print("4. E-letter Counter")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            produc_sum()
        elif choice == '2':
            divisible_by_7()
        elif choice == '3':
            hourglass()
        elif choice == '4':
            ecounter()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
