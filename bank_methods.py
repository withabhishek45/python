class Bank:
    #
    def __init__(self, initial_balance=0):
        self.balance = initial_balance  
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")   
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        return self.balance
    
#user freindly interface
account = Bank()
while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        print(f"Current Balance: ${account.get_balance():.2f}")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose again.")
    

