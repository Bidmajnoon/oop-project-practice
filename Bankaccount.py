import random

class BankAccount:
    def __init__(self, name='ahmad', account_number = 123564, remaining=45630):
        self.name = name
        self.account_number = account_number
        self.remaining = remaining
        
    def deposit(self):
        money = float(input('How much do you want to deposit? '))
        self.remaining += money
        return f'{self.name}   {self.account_number}   , a{self.remaining}'
    def harvest(self):
        money = float(input('How much do you want to harvest? '))
        self.remaining -= money
        return f'{self.name}   {self.account_number}   , a{self.remaining}'
        
class Customer:
    def __init__(self, name='ahmad', account_number='655', id='6598'):
        self.name = name
        self.account_number = account_number
        self.id = id
        self.accounts = {self.name: {'name': self.name, 'accounts_number:': [], 'id:': self.id}}
        
    def add(self):
        accounts = self.accounts
        self.name = input('Enter name: ')
        if self.name in accounts:
            self.account_number = int(input('Enter new account number: '))
            accounts[self.name]['accounts_number:'].append(self.account_number)
            return accounts
        else:
            self.account_number = random.randint(963652152361, 1036569875243)
            self.id = random.randint(161158161, 9869689652)
            accounts[self.name] = {'name': self.name, 'accounts_number:': [self.account_number], 'id:': self.id}
            self.accounts = accounts
            print(accounts)
           

    def remove(self):
        rname = input('Enter name: ')
        if rname in self.accounts:
            self.delet = int(input('Enter account to be deleted: '))
            self.accounts[rname]['accounts_number:'].remove(self.delet)
            return self.accounts
        else:
            print('Account does not exist')
        


bankaccount = BankAccount()
print(bankaccount.deposit())
print(bankaccount.harvest())


customer = Customer()
print(customer.add())
print(customer.remove())