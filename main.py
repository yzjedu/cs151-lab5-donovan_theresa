# Programmers: Theresa and Donovan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine), where users can view their balance,
#deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).
# Data In: Letter of the function chosen by user
# Data Out:  Operation of chosen function
# Credits: In Class

key = int(input('Enter passkey'))

while key != 12345:
   print('Incorrect passkey')
   key = int(input('Enter passkey'))


from optparse import AmbiguousOptionError
balance = 1000
print('The initial balance in your account is 1000')
option = 'A'

while option != 'sentinel':
    option = input('What would you like to do with your account today?\n'
                   'D - Deposit\n'
                   'W - withdraw\n'
                   'V - View balance\n'
                   'E - Exit\n')
    option = option.upper().strip()

# D-Deposit
    if option == 'D':
        money = float(input('how much money would you like to deposit? '))
        if money < 0:
            print('Sorry, you cannot output a negative')
        else:
            balance += money
            print('Your balance is', balance, 'dollars' '\n')


#W=Withdraw
    elif option == 'W':
        money = float(input('how much money would you like to withdraw? '))
        if money < 0:
            print('Sorry, you cannot input a negative')
        else:
            balance -= money
            print('Your balance is', balance, 'dollars \n')

#V=View Balance
    elif option == 'V':
        print('Your balance is', balance,'dollars')

#E=Exit
    elif option == 'E':
        print('Thank You for using this program')
        option = 'sentinel'

    if balance < 0:
        print('Warning your balance is negative, you will be charged 5% interest\n')





