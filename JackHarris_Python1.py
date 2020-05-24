"""
Given: an array of numbers but stored as strings.

Task: Sort them in ascending order

Example: instead of {9, 8, 3} you have {“9”, “8”, “3”},
and your output should be {“3”, “8”, “9”}

Rules:
1. You are not allowed to make them anything other than strings.
You can’t turn them into numbers and then back to strings.
2. Your code should work for any set of numbers, not just the ones above
"""

a = ['8','10','16','1','100','101','200','1000']

def string_num(x):
    
    sorted_list = sorted(x)
    sorted_list_len = []
    for i in sorted_list:
        sorted_list_len.append(len(i))
        
    # sorted_list = ['1', '10', '100', '1000', '101', '16', '200', '8']
    # sorted_list_len = [1, 2, 3, 4, 3, 2, 3, 1]
    
    dict1 = {}
    for i in sorted_list_len:
        dict1[i] = []
    for i,j in zip(sorted_list_len, sorted_list):
        dict1[i].append(j)
    
    list1 = []
    for i,j in dict1.items():
        for k in j:
            list1.append(k)
    
    return list1
    
string_num(a)

