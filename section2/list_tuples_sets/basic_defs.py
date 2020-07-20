l = ["Lee", "Rolf", "Anne"]
t = ("Lee", "Rolf", "Anne")
s = {"Lee", "Rolf", "Anne"}


print("List: ", l[2])
print("Tuple: ", t[2])
try:
    print("Set: ", s[2])
except TypeError as typex:
    print("TypeError:Sets are not subscriptable since they do not preserve order of the elements.")
except Exception as ex:
    raise ex

s.add("Apurva")
print("After adding an element to the set: ", s)
# Since sets do not have an end they do not have an `append` method.
