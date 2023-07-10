import random
import string

print("Welcome to the PyPassword Generator!")

p_lenght = int(input("What should be the length of your password?"))

nr_letters = random.randint(1,p_lenght)
nr_numbers = random.randint(1,p_lenght-nr_letters)
nr_symbols = p_lenght - nr_numbers -  nr_letters



letters = random.sample(string.ascii_letters, k = nr_letters)
numbers = random.sample(string.digits, k = nr_numbers)
symbols = random.sample(string.punctuation , k = nr_symbols)
all_char = letters + numbers + symbols

print(all_char)
random.shuffle(all_char)
print(all_char)
password = ""
counter = 0

for i in all_char:
    password += i
    counter += 1
    if counter % 4 == 0:
        password += "-"    
password.split("-",4)

print(password) 