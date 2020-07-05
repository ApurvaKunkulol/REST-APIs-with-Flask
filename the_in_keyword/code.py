__author__ = 'LENOVO'

friends = ["Mayuresh", "Apurva", "Suhas"]
print("Is Barbara a friend: ", "Barbara" in friends)


movies = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter the movie you most recently watched: ")
if user_movie in movies:
    print("You've just watched one of the big three!!")
else:
    print("Hope you watch one of the big three next time!!")
