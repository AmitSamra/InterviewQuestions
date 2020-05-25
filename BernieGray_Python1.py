"""
Write a function that takes in two parameters, a dictionary and a list.
The function should return True if all of the keys in the dictionary
are present at least once in the list and otherwise return False.
"""

d1 = {1:2, 3:4}
l1 = [1,3] # True becuase 1 and 3 are in l1
l2 = [1,2] # False because 3 is not in l2

def func(dict1, list1):
    for key in dict1.keys():
        if key not in list1:
            return False
    else:
        return True

print(func(d1,l1))
print(func(d1,l2))
