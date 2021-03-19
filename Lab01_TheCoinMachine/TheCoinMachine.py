# prompts user
usr_inp = input("Enter a whole number from 1 to 99. The machine will determine a combination of coins:\n")

# convert user input to integer value
usr_num = int(usr_inp)

# coin values
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1

# calculate quarter amount
quarters_rem = usr_num % quarter_value
quarters_tot = (usr_num - quarters_rem)/quarter_value

# calculates dime amount from remainder of quarters
dimes_rem = quarters_rem % dime_value
dimes_tot = (quarters_rem - dimes_rem)/dime_value

# calculates nickel amount from remainder of dimes
nickels_rem = dimes_rem % nickel_value
nickels_tot = (dimes_rem - nickels_rem)/nickel_value

# calculates penny amount from remainder of nickels
pennies_rem = nickels_rem % penny_value
pennies_tot = (nickels_rem - pennies_rem)/penny_value

# displays results
print("\n" + usr_inp + " cents in coins: " +
      "\nQuarters: " + str(int(quarters_tot)) +
      "\nDimes: " + str(int(dimes_tot)) +
      "\nNickels: " + str(int(nickels_tot)) +
      "\nPennies: " + str(int(pennies_tot)))