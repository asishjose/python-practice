class CustomException(Exception):
    def __init__(self, message="Custom exception occurred"):
        super().__init__(message)


def menu():
    print("Menu:")
    print("1. Raise Custom Exception")
    print("2. Exit")


def handle_choice(choice):
    if choice == "1":
        raise CustomException("You selected option 1, which raised a custom exception.")
    elif choice == "2":
        return "Exiting the program. Goodbye!"
    else:
        return "Invalid choice. Please try again."


def main():
    while True:
        menu()
        try:
            choice = input("Enter your choice: ")  # Accepting manual input
            result = handle_choice(choice)
            if result:
                print(result)
                if choice == "2":
                    break
        except CustomException as ce:
            print(f"CustomException caught: {ce}")


if __name__ == "__main__":
    main()
