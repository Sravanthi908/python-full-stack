from abc import ABC , abstractmethod

class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withDraw(self):
        pass
class SavingAccount(Account):
    __balance = 0
    def get_balance(self):
        
        
        return self.__balance
    def deposit(self , amount):
        self.__balance += amount
        file=open("./file.txt","a")
        file.write(f"deposited: {amount}\n")
        file.close()


    def withDraw(self , amount):
        if self.__balance < amount:
            print("Not Enough Balance")
           
            self.__balance -= amount
        file=open("./file.txt","a")    
        file.write(f"Amount withdrawn :  {amount}\n")
        
        file.close()


class Bank:

    owner = "Bank"
    account_number = 0
    get_balance = 0

    def __init__(self , name , number , account_type = "Saving"):
        self.owner = name
        self.account_number = number

        if account_type == "Saving":
            self.account = SavingAccount()
        
class Manager:
    def get_customer_info(self , bankAccount : Bank,get_balance):
        file=open("./file.txt","a")  
        file.write(f"Name : {bankAccount.owner}\n")
        file.write(f"AccountNumber : {bankAccount.account_number}\n")
        file.write(f"Account Type : ")
        file.write(f"balance: {get_balance}")
        if(type(bankAccount.account) == SavingAccount):
            file.write("Savings Account\n")
        file.close()
sam=Bank("sam",1,"Saving")
sam.account.deposit(100)
sam.account.withDraw(10)
sam.account.get_balance()