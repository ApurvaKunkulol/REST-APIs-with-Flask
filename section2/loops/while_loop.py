__author__ = 'LENOVO'

number = 7


while True:
    user_input = input("Would you like to play(Y/n):").lower()
    if user_input == 'n':
        break
    user_number = int(input("Please guess the number: "))
    if user_number == number:
        print("You guessed correctly!!")
    elif number - user_number in(1, -1):
        print("You were off by one!")
    else:
        print("Sorry! Better luck next time.")
