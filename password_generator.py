import random
import string

# alphabets = string.ascii_letters
# numbers = string.digits
length = int(input("Enter the length of password you want : "))
ask_user = int(input("Enter the type of password you want : \n 1. Number Password (Only random numbers) \n 2. Mixed Password (Random Characters, Digits and Symbols ) \n 3. Alphanumeric Passwords (Alphabets and Numbers) : " ))

if ask_user == 1:
    number = string.digits
    number_passwords = ''.join(random.choice(number) for _ in range(length))
    print("Generated Number Password : " + number_passwords)

elif ask_user == 2:
    mix_characters = string.printable
    mix_password = ''.join(random.choice(mix_characters) for _ in range (length))
    print("Generated Mixed Password : " + mix_password)

elif ask_user == 3:
    alpha_numeric = string.ascii_uppercase + string.digits
    alpha_numeric_pw = ''.join(random.choice(alpha_numeric) for _ in range(length))
    print("Generated Mixed Password : " + alpha_numeric_pw)

