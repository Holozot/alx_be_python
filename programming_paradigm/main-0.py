import sys
from bank_account import BankAccount

def main():
    # A new BankAccount is created with a starting balance of 100 every time the script runs.
    try:
        account = BankAccount(100)  # Example starting balance
    except ValueError as e:
        print(f"Error initializing account: {e}")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        print("Example: python main-0.py deposit:50")
        print("Example: python main-0.py withdraw:20")
        print("Example: python main-0.py display")
        sys.exit(1)

    # sys.argv[1] will be something like "deposit:50" or "display"
    parts = sys.argv[1].split(':')
    command = parts[0].lower() # Convert to lowercase for consistent matching
    amount = float(parts[1]) if len(parts) > 1 else None

    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
            except ValueError as e:
                print(f"Error during deposit: {e}")
        else:
            print("Error: Deposit command requires an amount (e.g., deposit:50).")
            sys.exit(1)
    elif command == "withdraw":
        if amount is not None:
            try:
                if not account.withdraw(amount):
                    # The withdraw method already prints "Insufficient funds."
                    pass
            except ValueError as e:
                print(f"Error during withdrawal: {e}")
        else:
            print("Error: Withdraw command requires an amount (e.g., withdraw:20).")
            sys.exit(1)
    elif command == "display":
        if amount is not None: # Check if an amount was accidentally provided for display
            print("Warning: Display command does not take an amount. Ignoring it.")
        account.display_balance()
    else:
        print(f"Invalid command: '{sys.argv[1]}'.")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

if __name__ == "__main__":
    main()
