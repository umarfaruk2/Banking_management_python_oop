class CreateAccount:
    def __init__(self, email, password, user_type):
        self.email = email
        self.password = password
        self.user_type = user_type

    @property 
    def user_info(self):
        return self.email, self.password, self.user_type

class Admin:
    def __init__(self, initial_balance):
        self.bank_balance = initial_balance
        self.loan_balance = 0
        self.loan_feature = True
    
    def total_bank_balance(self):
        print('total bank balance: ', self.bank_balance)
    
    def check_load_amount(self):
        print('total load amount: ', self.loan_balance)
    
    def give_load(self, user_account, user_amount):
        given_amount = user_amount + user_amount
        if self.loan_feature and self.bank_balance >= given_amount:
            self.loan_balance += given_amount
            self.bank_balance -= given_amount
            user_account.take_loan_from_bank(given_amount)
        
        else:
            print("You don't have enough balance to give loan or load given off")
    
    def loan_feature_on_off(self, toggle):
        if toggle == 'off':
            self.loan_feature = False
        elif toggle == 'on':
            self.loan_feature = True

class User:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Your withdraw money: ', amount)
        else:
            print('Sir, you don\'t have enough money to withdraw')

    def check_balance(self):
        print('your current balance: ', self.balance) 
    
    def transfer_money(self, user_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            user_account.deposit(amount)
            self.transaction_history.append(f'last transaction is: {amount}')
        else:
            print("don't have enough money to transaction")
        
    def check_transaction_history(self):
        for history in self.transaction_history:
            print(history)

    def take_loan_from_bank(self, amount):
        self.balance += amount



admin_account = CreateAccount('admin@gmail.com', 'admin11', 'admin')
admin = Admin(1000)
admin.total_bank_balance()
admin.check_load_amount()

print('\n')           
user_account_1 = CreateAccount('user_1@gmail.com', 'user11', 'user')
user_1 = User()
user_1.deposit(500)
user_1.withdraw(200)
user_1.check_balance()
admin.give_load(user_1, 300)
user_1.check_balance()
admin.total_bank_balance()
admin.check_load_amount()
admin.loan_feature_on_off('off')
admin.give_load(user_1, 200)
admin.loan_feature_on_off('on')
admin.give_load(user_1, 100)
user_1.check_balance()

print('\n')
user_account_2 = CreateAccount('user_2@gmail.com', 'user11', 'user')
user_2 = User()
user_2.deposit(400)
user_2.check_balance()
user_2.withdraw(100)
user_2.check_balance()
user_1.transfer_money(user_2, 100)
user_1.check_transaction_history()
user_2.withdraw(800)
user_1.check_balance()
user_2.check_balance()
