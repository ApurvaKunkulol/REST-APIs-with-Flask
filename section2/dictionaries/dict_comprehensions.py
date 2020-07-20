__author__ = 'LENOVO'

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

from pprint import pprint
username_mapping = {user[1]: user for user in users}
print("Username mapping:\n")
pprint(username_mapping)


username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")

_, username, password = username_mapping.get(username_input, (None, None, None))

if password == password_input:
    print("Your Credentials are correct. Taking you to the landing page.")
else:
    print("Incorrect credentials.")
