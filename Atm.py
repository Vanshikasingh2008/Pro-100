class ATM(object):
    def _init_(self, object):
        self.object = object
    def pin_card(self):
        pin = input("Enter your pin number: ")
        card = input("Enetr your card no.: ")
    def CashWithdrawl(self):
         cash = input("Enter the amount of csh to be withdrawn: ")
         print("Your cash has been withdrawn.")

person = ATM("card")
person.pin_card()
person.CashWithdrawl()