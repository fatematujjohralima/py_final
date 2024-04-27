class User:
    def __init__(self,name, email, address, account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type= account_type
        self.balance=0
        self.transaction=[]
        self.loan=0
    
    def deposite(self,amount):
        self.balance+=amount
        self.transaction.append(f"deposite:{amount}")
        print(f"successfully deposite {amount}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.transaction.append(f"withdrow:{amount}")
            print(f"successfully withdraw {amount}")
        else:
            print(f"Withdrawal amount exceeded")
    def available_balance(self):
        print(f"available balance: {self.balance}")
    def transactions(self):
        for t in self.transaction:
            print(t)
        # return self.transaction
    def Loan(self,amount):
        if self.loan<2:
            self.balance+=amount
            self.loan+=1
            print("Successfully loan taken")
            self.transaction.append(f"loan:{amount}")
        else:
            print("you can take 2 times loan")
    def transfer(self,amount,receiver):
        if self.balance>=amount:
            self.balance-=amount
            receiver.balance+=amount
            self.transaction.append(f"transfer {amount} to {receiver}")
            print(f"successfully transfer {amount} to {receiver}")
        else:
            print(f"you have not enough money in your account")
    

class Admin:
    def __init__(self,name,password) -> None:
        self.name=name
        self.password=password
        self.users=[]
    def create_account(self,name,email,address,account_type):
        user=User(name,email,address,account_type)
        self.users.append(user)
    def delete_account(self,email):
        for user in self.users:
            if user.email==email:
                self.users.remove(user)
                print(f"{email} delete successfully")
               
    def list(self):
        for user in self.users:
            print(f"name: {user.name},email: {user.email},address: {user.address},account type: {user.account_type}")
    def available_balance(self):
        available=sum(user.balance for user in self.users)
        print(f"{available}")
    def total_loan(self):
        available=sum(user.loan for user in self.users)
        print(f"{available}")

admin=Admin("admin",123)

run = True
while run:
    print("Options: \n")
    print("1: Login as admin")
    print("2: Login as user")
    print("3: Exit")
    ch =input("\nEnter Option: ")
    if ch == '1':
        print("1: create an account")
        print("2: delete any user account")
        print("3: see all user accounts list")
        print("4: check the total available balance of the bank.")
        print("5: check the total loan amount")
        print("6: exit")
        ch =input("\nEnter Option: ")
        if ch == '1':
            name=input("Enter name: ")
            email=input("Enter email: ")
            address=input("Enter address: ")
            account_type=input("Enter account type(savings/current): ")
            admin.create_account(name,email,address,account_type)
            print("Account created")
        elif ch == '2':
            email=input("Email: ")
            admin.delete_account(email)
        elif ch == '3':
            admin.list()
        elif ch == '4':
            admin.available_balance()
        elif ch == '5':
            admin.total_loan()
            user.transactions()
        elif ch == '6':
            run=False
    elif ch=='2':
        print("1: Deposite")
        print("2: Withdraw")
        print("3: check balance.")
        print("4: take loan")
        print("5: money transfer")
        print("6: exit")
        ch =input("\nEnter Option: ")
        if ch == '1':
            email=input("Enter email: ")
            amount=int(input("Enter amount: "))
            for user in admin.users:
                if user.email==email:
                    user.deposite(amount)
        elif ch == '2':
            email=input("Enter email: ")
            amount=int(input("Enter amount: "))
            for user in admin.users:
                if user.email==email:
                    user.withdraw(amount)
        elif ch == '3':
            email=input("Enter email: ")
            for user in admin.users:
                if user.email==email:
                    user.available_balance()
        elif ch == '4':
            amount=int(input("Enter amount: "))
            email=input("Enter email: ")
            for user in admin.users:
                if user.email==email:
                    user.Loan(amount)
        elif ch == '5':
            sender_email=input("Enter sender email: ")
            receiver_email=input("Enter receiver email: ")
            amount=int(input("Enter amount: "))
            sender=None
            receiver=None

            for user in admin.users:
                if user.email==sender_email:
                    sender=user
                if user.email==receiver_email:
                    receiver=user
            if sender and receiver:
                sender.transfer(amount,receiver)
            else:
                print("user does not exist")
                
        elif ch == '6':run=False
    elif ch=='3':
        run=False 