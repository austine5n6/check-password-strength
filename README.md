# Password Strength Checker

This Python code is a password strength checker that uses the "Have I Been Pwned" API to check if the password has been previously compromised in a data breach. It also checks if the password meets certain minimum requirements for strength.

# requests module 
The requests module is used to make a GET request to the API to retrieve the list of known compromised passwords. 

# hashlib module. 
The hashlib module is used to hash the password using SHA-1 algorithm before checking if it is in the list.

# The check_password_strength function 
This takes a password string as input and returns True if the password meets the minimum requirements for strength and has not been previously compromised, and False otherwise.

To check if the password has been previously compromised, the function makes a GET request to the API with the first 5 characters of the hashed password. If the password is in the list, the function returns False, indicating that the password is weak.
The function then checks if the password meets the minimum requirements for strength, which includes having at least 8 characters, not being entirely numeric, not being entirely alphabetical, not being entirely lowercase, and not being entirely uppercase. If the password fails any of these checks, the function returns False.

# Note 
The requests module needs to be installed separately before running the code.