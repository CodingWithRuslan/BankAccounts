#we import everything from bank_accounts file
from bank_accounts import *

#now we create instance of bank_accounts 

Ruslan = BankAccount(1000,"Ruslan")
Ruslan2 = BankAccount(2000,"Ruslan2")
Ruslan.getBalance()
Ruslan2.getBalance()

Ruslan2.deposite(500)

Ruslan.withdraw(10000)
Ruslan.withdraw(10)

Ruslan.transfer(10000,Ruslan2)
Ruslan.transfer(100,Ruslan2)

Ruslan3 = InterestRewardsAcct(1000,"Ruslan3")
Ruslan3.getBalance()
Ruslan3.deposite(100)
Ruslan3.transfer(100, Ruslan)

Ruslan4 = SavingsAcct(1000, "Ruslan4")

Ruslan.getBalance()

Ruslan4.deposite(100)

Ruslan4.transfer(1000, Ruslan2)
Ruslan4.transfer(100, Ruslan2)
