def deposit():
    account = 1000

    try:
        print(f"Starting amount: {account} baht")
        money_received = int(input("Enter the amount you wish to deposit:"))

        if money_received <= 0:
            raise ValueError("Error: The deposit amount must be greater than 0.")

        account += money_received
        print("")

        print("Deposit successful.")
        print(f"Remaining balance: {account} baht")

    except ValueError as error:
        print(f"Error as {error}")

deposit()
