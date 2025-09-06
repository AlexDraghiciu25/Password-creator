import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lenght_letters = len(letters)
lenght_numbers = len(numbers)
lenght_symbols = len(symbols)

password = []
for i in range(0, nr_letters):
    var = random.randint(0, lenght_letters - 1)
    password.append(str(letters[var]))

for i in range(0, nr_numbers):
    var = random.randint(0, lenght_numbers - 1)
    password.append(str(numbers[var]))

for i in range(0, nr_symbols):
    var = random.randint(0, lenght_symbols - 1)
    password.append(str(symbols[var]))

print(password)

for i in range(0, len(password) - 1, 1):
    var = random.randint(0, len(password) - 1)
    aux = password[i]
    password[i] = password[var]
    password[var] = aux

print(password)
# print(''.join(password)) or i can make that

final_password = ""
for char in password:
    final_password += char

print(f"Your cripted password is: {final_password}")