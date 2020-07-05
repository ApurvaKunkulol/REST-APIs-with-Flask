__author__ = 'LENOVO'

numbers = list(range(6))
doubled = []

for num in numbers:
    doubled.append(num * 2)
print("Traditional way: ", doubled)
print("Using list comprehension: ", [x * 2 for x in numbers])

# Append names of all friends which start with an "S", using list comprehension of course.
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print("Friends that start with S: ", starts_s)
