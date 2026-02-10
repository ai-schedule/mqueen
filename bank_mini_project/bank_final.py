import re

# ================= CLASS (UNCHANGED) =================
class bankaccount:
    def __init__(self):
        self.name=input('enter name for customer')
        self.balance=int(input('enter opening balance for account'))
        self.username=input('enter username')
        while True:
            self.password = input('Enter password: ')
            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
            if re.match(pattern, self.password):
                print("Strong password accepted")
                break
            else:
                print("Weak password!")
        self.transactions=[]
        self.transactions.append(f"Name:- {self.name}")
        self.transactions.append(f"opening balance= {self.balance}")
        print('welcome to our bank')

    def deposit(self):
        self.user=input('enter username')
        self.passw=input('enter password')
        if self.user==self.username and self.passw==self.password:
            self.amount=int(input('enter amount to deposit'))
            if self.amount >0:
                self.balance+=self.amount
                self.transactions.append(
                    f"deposit amount is {self.amount} and balance is {self.balance}"
                )
        else:
            print('wrong username')

    def withdrawl(self, amount):
        self.user=input('enter username')
        self.passw=input('enter password')
        if self.user==self.username and self.passw==self.password:
            if amount < self.balance:
                self.balance -= amount
            else:
                print('insufficient balance')
            self.transactions.append(
                f"withdraw amount:- {amount} balance= {self.balance}"
            )
        else:
            print('authentication failed')

    def viewbalance(self):
        print(f"{self.name}, {self.balance}")

    def transaction(self):
        for i in self.transactions:
            print(i)

# ================= FILE HANDLING =================

def save_to_file(obj):
    file = obj.username + ".txt"
    with open(file, "w") as f:
        f.write(obj.name + "\n")
        f.write(str(obj.balance) + "\n")
        f.write(obj.username + "\n")
        f.write(obj.password + "\n")
        for t in obj.transactions:
            f.write(t + "\n")

def load_from_file(username):
    file = username + ".txt"
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        obj = bankaccount.__new__(bankaccount)
        obj.name = lines[0].strip()
        obj.balance = int(lines[1].strip())
        obj.username = lines[2].strip()
        obj.password = lines[3].strip()
        obj.transactions = [i.strip() for i in lines[4:]]
        return obj

    except FileNotFoundError:
        return None

# ================= MAIN PROGRAM =================

print("1. New Account")
print("2. Existing Account")
choice = input("Enter choice: ")

if choice == "1":
    acc = bankaccount()
    save_to_file(acc)

elif choice == "2":
    uname = input("Enter username: ")
    acc = load_from_file(uname)

    if acc is None:
        print("Account does not exist")
        exit()

    while True:
        print("\n1 Deposit\n2 Withdraw\n3 Balance\n4 Transactions\n5 Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            acc.deposit()
            save_to_file(acc)

        elif ch == "2":
            amt = int(input("Enter amount: "))
            acc.withdrawl(amt)
            save_to_file(acc)

        elif ch == "3":
            acc.viewbalance()

        elif ch == "4":
            acc.transaction()

        elif ch == "5":
            save_to_file(acc)
            break
