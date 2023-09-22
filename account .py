def__init__(self, account_number,account_holder_name,initial_balance=0.0)
self.__account_number=account_number
self.__account_holder_name=account_holder_name
self.__account_balance=initial_balance

def deposit(self,amounts):
  if amount >0:
    self.__account_balance+=amount 
    #self.__account_balance=self.__account_balance+amount
    psrint("deposited ₹{}.new balance:₹{}".format (amount,                             self.__account_balance))
  else:
    print("invalid deposit amount. ")

def withdraw (self, amount) :
  if amount >0and amount <=self.__account_balance:
    self.__account_balance-=amount
    self.__account_balance=self.__account_balance-amount
print("withdraw ₹{},new balance :₹{}."format(amount,
                                              self.__account_balance))
else:
print("invalid withdrawal amount or insufficient balance .")

def display_balance(self):
print("account balance for {} (account #{}: ₹{}".format[
  self.__acconut_holder_name,self.__account_number,
      self.__account_balance])


#create an instance of the bank account class 
account =bankaccount(acconut_number="123456789",
            account_holder_name="hari prabhu",
  initial_balance=5000.0)

#test deposit and withdrawal functionality 
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()