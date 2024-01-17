# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

def deposit(transactions, amount):
    print("Amount Deposited: ",amount)
    transactions.append(amount)

def withdraw(transactions, amount):
    amount = float(input("Enter amount to withdraw: "))
    balance = sum(transactions)
    if balance >= amount:
        transactions.append(-amount)
        print("You withdraw: ",amount)
    else:
        print("Insufficient balance ")

def check_balance(transactions):
    balance = sum(transactions)
    print("Available Balance=",balance)
    pass

def list(transactions):
    print(transactions)
    pass

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = int(input("Enter amount: "))
        deposit(transactions, amount)
    elif choice == '2':
        withdraw(transactions, amount)
    elif choice == '3':
        check_balance(transactions)
    elif choice == '4':
        list(transactions)
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
