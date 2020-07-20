__author__ = 'LENOVO'

# Most basic form of a function.

def hello():
    print("hello")


def user_age_in_seconds():
    age = int(input("Please enter your age(in years): "))
    print("Age in seconds: ", age * 365 * 24 *3600)
    print("Good Bye!!")

user_age_in_seconds()
