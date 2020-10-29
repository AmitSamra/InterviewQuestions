"""
Jack Harris

Given: an array of numbers but stored as strings.
Task: Sort them in ascending order

Example: instead of {9, 8, 3} you have {“9”, “8”, “3”},
and your output should be {“3”, “8”, “9”}

Rules:
1. You are not allowed to make them anything other than strings.
You can’t turn them into numbers and then back to strings.
2. Your code should work for any set of numbers, not just the ones above
"""

def string_num(x):
    
    d_pos = {}
    d_neg = {}
    
    # create empty lists in d_pos & d_neg
    for i in x:
        if i[0] != '-':
            d_pos[len(i)] = []
        else:
            d_neg[len(i)-1] = []

    # add positive items to d_pos
    for i in x:
        if i[0] != '-':
            d_pos[len(i)].append(i)
    for i,j in d_pos.items():
        j.sort()
    
    # add negative items to d_neg
    for i in x:
        if i[0] == '-':
            d_neg[len(i)-1].append(i)
    for i,j in d_neg.items():
        j.sort(reverse = True)
    
    pos_list = []
    neg_list = []
    
    # add positive items to pos_list
    for i,j in d_pos.items():
        for item in j:
            pos_list.append(item)
    
    # add negative items to neg_list
    for i,j in d_neg.items():
        for item in j[::-1]:
            neg_list.append(item)
    
    final_list = []
    
    # add neg_list items to final_list
    for i in neg_list[::-1]:
        final_list.append(i)
    
    # add pos_list items to final list
    for i in pos_list:
        final_list.append(i)
    
    return final_list

a = ['8','10','16','1','100','101','200','1000']
print(string_num(a))

b = ['-50', '-10','-100','-80','8','10','16','1','100','101','200','1000']
print(string_num(b))