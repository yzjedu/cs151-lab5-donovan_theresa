# Algorithm Document
1. create a variable for balance and set it to 1000
2. output"The initial balance of your account $1000"
2. set option to A
3. while option is not E
   1. prompt user to input option "
   D - Deposit
   W - Withdraw
   V - View Balance
   E - Exit"
   2. typecast remove spaces and make uppercase
   4. If user chooses D
      1. prompt user to input money being deposited 
      2. if money is < 0
         3. output "can not input a negative"
      4. otherwise
         5. add money to balance
         5. output new balance
         4. prompt user to input an option   
   4. if user chooses W 
      1. prompt user to input money being withdrawn 
      2. if money is < 0
         3. output "can not input a negative number"
      4. otherwise
         5. subtract money from balance
         6. output new balance
         7. ask for option again
   5. if user chooses V
      6. output the balance
      7. prompt the user for their option again
   8. if the balance is less than 0
      9. output "warning you will be charged 5% interest"
   

