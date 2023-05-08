import requests
import hashlib

def check_password_strength(password):
    response = requests.get('https://api.pwnedpasswords.com/range/' + hashlib.sha1(password.encode('utf-8')).hexdigest()[:5])
    if response.status_code != 200:
        raise RuntimeError('Error fetching data')
    hashes = (line.split(':') for line in response.text.splitlines())
    count = sum(int(count) for _, count in hashes if password.endswith(_))
    if count:
        return False

    # Check if password meets minimum requirements for strength
    if len(password) < 8:
        return print(f' {password} is less than 8 characters')
    if password.isnumeric():
        return False
    if password.isalpha():
        return False
    if password.islower():
        return False
    if password.isupper():
        return False

    return True

# Test the function with some example passwords
# passwords = ['EpJ2*7np9!', '123456', 'iloveyou', '3Gu^f6Z4DZ#Y', 'i@20cryMetoSleep']
# for password in passwords:
#     if check_password_strength(password):
#         print(f'{password} is a strong password')
#     else:
#         print(f'{password} is a weak password')
