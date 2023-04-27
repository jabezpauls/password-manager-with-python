# Password-Manager-with-Python
This Password Manager is a Python program that generates personalized passwords and checks their strength against various criteria. It also checks if a password has been breached in the past using the Have I Been Pwned API.

Requirements:

Python 3.x
Requests 
library

How to Use:

Clone the repository
Install the Requests library by running pip install requests in the terminal
Run the program by running python password_manager.py in the terminal
Follow the on-screen instructions to use the Password Manager

Features:

Generate Personalized Password: This feature allows the user to enter their name, birth year, and favorite color, and generates a password based on that information. It also replaces certain characters with numbers and special characters and shuffles the characters to create a unique password.

Check Password Strength: This feature checks the strength of a given password against various criteria, such as length, presence of uppercase and lowercase letters, digits, and special characters. It returns a message indicating if the password is strong or if it needs improvement.

Check Password Breach: This feature checks if a given password has been breached in the past using the Have I Been Pwned API. It uses the SHA-1 algorithm to hash the password and then sends a request to the API to check if the password has been breached. If the password has been breached, the user is notified and advised to change their password.

Architecture and Methodology:

The program is written in Python and follows a modular architecture, with each feature implemented as a separate function. The generate_password() function takes user input, manipulates the input to create a password, and returns the password. The check_password() function checks the strength of a given password against various criteria and returns a message indicating its strength. The check_breach() function checks if a given password has been breached in the past using the Have I Been Pwned API and returns a Boolean value indicating if the password has been breached.

The program uses the Requests library to send HTTP requests to the Have I Been Pwned API and hashlib library to hash the password using SHA-1 algorithm.

Conclusion:

The Password Manager is a simple yet powerful tool for generating and checking the strength of passwords. It allows users to create strong passwords and check if their existing passwords have been breached in the past. The modular architecture and use of external libraries make the program easy to maintain and extend in the future.
