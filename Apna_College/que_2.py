class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc 

    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} is Debited\nRemaining Balance: {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is Credited\nRemaining Balance: {self.balance}")

    def get_balance(self):
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_no} Balance: {self.balance}"


acc1 = Account(10000, 1234)
print(acc1)

def bank():
    while True:
        print("\nENTER OPTION:- \n1] CREDIT \n2] DEBIT \n3] BALANCE CHECK \n4] EXIT")
        action = int(input("Enter your choice: "))
        
        match action:
            case 1:
                amt = int(input("ENTER AMOUNT TO CREDIT: "))
                acc1.credit(amt)
            case 2:
                amt = int(input("ENTER AMOUNT TO DEBIT: "))
                acc1.debit(amt)
            case 3:
                acc1.get_balance()
            case 4:
                print("Exiting... Thank you!")
                break
            case _:
                print("Invalid Option. Try again.")

bank()
