__author__ = 'LENOVO'

number = 7
user_input = input("Enter 'y' if you would like to play:").lower()

if user_input == 'y':
    user_number = int(input("Please guess the number: "))
    if user_number == number:
        print("You guessed correctly!!")
    elif number - user_number in(1, -1):
        print("You were off by one!")
    else:
        print("Sorry! Better luck next time.")
else:
    print("Bye!!")