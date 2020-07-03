friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}


# Set Difference operation
print("Set Difference Operations")
local_friends = friends.difference(abroad)
print("Local friends: ", local_friends)
local_friends = abroad.difference(friends)
print("Local friends from reverse difference: ", local_friends)


# Set Union operation
print("\n\nSet Union Operations")
local = {"Rof"}
abroad = {"Bob", "Apurva"}

friends = local.union(abroad)
print("Total friends after combining both sets: ", friends)


# Set Intersection Operations
print("\n\nSet Intersection Operations")
arts = {"Bob", "Jenn", "Rolf", "Charlie"}
science = {"Bob", "Jenn", "Adam", "Anne"}
print("Students studying both: ", arts.intersection(science))
