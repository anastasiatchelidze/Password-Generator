import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!\n")
num_of_letters = int(input("How many letter would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))

new_list = []
for i in range(num_of_letters):
    new_list.append(random.choice(letters))
for i in range(num_of_symbols):
    new_list.append(random.choice(symbols))
for i in range(num_of_numbers):
    new_list.append(random.choice(numbers))
    
random.shuffle(new_list)

print("\nRandom password generated for you is:\t", end='')
for item in new_list:
    print(item, end='')