import random
import requests
import hashlib
import re
import time
import os
def generate_password():
    name = input("Enter your name: ")
    birth_year = input("Enter your birth year: ")
    favorite_color = input("Enter your favorite color: ")
    #add all of the input
    password_string = name + birth_year + favorite_color
    #replace the given text with random stuff
    password_string = password_string.replace("a", "@")
    password_string = password_string.replace("e", "3")
    password_string = password_string.replace("i", "1")
    password_string = password_string.replace("o", "0")
    password_string = password_string.lower()
    #shuffle all of the charecters...
    password_list = list(password_string)
    random.shuffle(password_list)
    password = "".join(password_list)
    
    return password
def check_breach(password):
    # Hash the password using SHA-1 algorithm
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Use the first 5 characters of the hash as the prefix and the remaining characters as the suffix
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Send a request to the Have I Been Pwned API to check if the password has been breached
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)

    # Check if the password's suffix appears in the response
    return suffix in response.text.upper()
def check_password(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short"

    # Check if password contains uppercase letters
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter"

    # Check if password contains lowercase letters
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter"

    # Check if password contains digits
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit"

    # Check if password contains special characters
    if not re.search("[!@#$%^&*()_+-={};:'\"<>,.?/|\\]", password):
        return "Password must contain at least one special character"

    # Password is strong
    return "Password is strong"
while (1):
    print("WELCOME PASSWORD MANAGER")
    print("--------------------------------------")
    print("What would you like to do?")
    print("1.Generate personalised password")
    print("2.Check the Strenght of a password")
    print("3.Check for password breaches")
    print("0.End the program")
    print("--------------------------------------")
    menu = int(input("Choose the menu number: "))
    if menu == 1:
        #call the function generate_password()
        password = generate_password()
        #print dah output.......
        print("Your password is:", password)
    elif menu == 2:
        inchoice = input("Do you want to check the password for generated password ? (yes/no)")
        if inchoice == 'yes':
            if len(password)!=0:
                print(check_password(password))
            else:
                print("No password generated")
        elif inchoice == 'no':
            password = input("Enter a password")
            print(check_password(password))
    elif menu == 3:
    
         if check_breach(password) == False:
            print("Your Password is safe")
         else:
            print("Your Password is Breached")
    elif menu == 0:
        break
    else:
        print("Thank you for using the manager")
    time.sleep(2)
    #system('clear')
