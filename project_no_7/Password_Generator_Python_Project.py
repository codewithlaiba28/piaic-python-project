import random
print("Welcom to your password generator!")
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()?"
number=int(input("Amount of password to generate: "))
length=int(input("Enter your password length: "))
print("\nHere are your passwords: ")
for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(char)
    print(password)    