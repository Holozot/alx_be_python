class BankAccount:

    def __init__(self, initial_balance=0):
        # new BankAccount instance with an argument for the account starting balance
        
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulation using __

    def deposit(self, amount):
        # deposit method, where amount has to be positive
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount

    def withdraw(self, amount):
        
        """withdraw method:  amount specified has to match sufficient
        Returns: True if the withdrawal was successful, False otherwise.
        Raises: ValueError: If the withdrawal amount is not positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${int(self.__account_balance)}")
