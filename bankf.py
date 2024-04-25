class Bank:
    def __init__(self):
        self.accounts = []#keep list of accounts
        self.last_account_number = 0 
    #add new account with with given name to list of accounts
    def add_account(self, name):
        self.last_account_number += 1
        acc = Account(name, self.last_account_number)
        self.accounts.append(acc) 
#give back mtch accunt with account_number else return None
    def find_account(self, number):
        for acc in self.accounts:#check all accunts 
            if acc.account_number == number:
                return acc
        return None 
#get from_account_number , to_account_number, amount subtract amount  from_account_number to_account_number
    def transfer(self, from_account_number, to_account_number, amount, password):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            if from_account.balance >= amount:
                if from_account.check_password(password):
                    from_account.balance -= amount
                    to_account.balance += amount
                    print("Transfer successful.")
                else:
                    print("Invalid password.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account number.") 

class Account:
    def __init__(self, name, number):
        self.name = name
        self.balance = 0
        self.account_number = number
        self.password = None

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

    def show_info(self, password):
        if self.check_password(password):
            print(f"Account Holder: {self.name}")
            print(f"Account Number: {self.account_number}")
            print(f"Balance: {self.balance}")
        else:
            print("Invalid password.")
#get amount add amount to balance
    def deposit(self, amount, password):
        if self.check_password(password):
            if amount > 0:
                self.balance += amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid password.")

    def withdraw(self, amount, password):
        if self.check_password(password):
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid password.")
#save final balances
    def save_final_balances(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"Account Number: {account.account_number}\n")
                file.write(f"Account Holder: {account.name}\n")
                file.write(f"Final Balance: {account.balance}\n")
                file.write("\n")

bank = Bank()
bank.save_final_balances("final_balances.txt")