import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*()+'

print("** WELCOME TO THE PASSWORD GENERATOR **")

n_letters = int(input("Enter the number of letters you want in your password: "))
n_numbers = int(input("Enter the number of numbers you want in your password: "))
n_symbols = int(input("Enter the number of symbols you want in your password: "))

password_list = (
    random.choices(letters, k=n_letters) +
    random.choices(numbers, k=n_numbers) +
    random.choices(symbols, k=n_symbols)
)

random.shuffle(password_list)

password = "".join(password_list)

print("Generated Password:", password)