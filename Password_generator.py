import random

print("Password Generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_in = int(input("How many letters you want in password"))
number_in = int(input("How many numbers you want in password"))
symbol_in = int(input("How many symbols you want in password"))

letter_sel = random.sample(letters, letter_in)
number_sel = random.sample(numbers, number_in)
symbol_sel = random.sample(symbols, symbol_in)

password_list =letter_sel + symbol_sel+ number_sel
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your Password is : {password}")
