# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function
# Credits: In Class
from optparse import AmbiguousOptionError

balance = 1000
print('The initial balance in your account is 1000')
option = 'A'

while option != sentinel:
    option = input('What would you like to do with your account today?\n'
                   'D - deposit\n'
                   'W - withdraw\n'
                   'V - view balance\n'
                   'E - exit\n')
    option = option.upper()

#D=Deposit
#W=Withdraw
#V=View Balance
#E=Exit
