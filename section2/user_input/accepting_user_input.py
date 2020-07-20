__author__ = 'Apurva A Kunkulol'

name = input("Enter  your name: ")
print("Your name is: {}".format(name))

#Doing mathematics with input

sq_ft = input("Enter the area of your house(in square feet): ")
sq_ft = int(sq_ft)
sq_mt = sq_ft / 10.8

print(f"{sq_ft} square feet is {sq_mt:.5f} square metres")


