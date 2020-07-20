__author__ = 'LENOVO'

movies = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter the movie you most recently watched: ")
if user_movie in movies:
    print(f"I've watched the {user_movie} too!")
else:
    print("Hope you watch one of the big three next time!!")
