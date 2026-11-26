"Using Encapsulation method for bank application in oops"

class Bank_Applications:
    def __init__(self,acc_name,acc_no,bal):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.__bal=bal

    def display_details(self):
        print("Account Holder Name :",self.acc_name,"\n","Account Balance :",self.__bal)

    def withdraw(self,amount):
        if amount<0:
            print("Invalid Amount")
        elif self.__bal<amount:
            print("Insufficient Balance")
        else:
            self.__bal=self.__bal-amount
            print("Withraw Successfull")
    def balance_check(self):
        print("Availabale Balance :",self.__bal)
user1=Bank_Applications("Giri",123456789,5000)
user1.display_details()
user1.withdraw(600)
user1.balance_check()
user1.withdraw(1500)
user1.balance_check()