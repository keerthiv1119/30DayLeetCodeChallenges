'''
Author : Keerthi Vutukuri
Date : 01- 04-2020
Name : Single Number
'''
#Using Iterations it will took O(n^^2) Time Complexity with O(1) Space Complexity
def single(ar):
    for i in range(len(ar)):
        count = 1
        for j in range(i+1,len(ar)):
            if ar[j] == ar[i]:
                count += 1
        if count == 1:
            return ar[i]
#Using Dictionaries/Hash to Optimize the Time Complexity to O(n).Here Space Complexity is O(n)
def single1(ar):
    h = {}
    for i in range(len(ar)):
        count = 1
        if ar[i] not in h:
            h[ar[i]] = count
        else:
            h[ar[i]] = count + 1
    min_ = min(h, key=h.get)
    return min_
#optimal solutions with O(n) time complexity and O(1) space Complexity using XOR operations.
def single3(ar):
    from functools import reduce
    return reduce(lambda x , y : x ^ y , ar,0)#Easy Notation
def single4(ar):
    result = ar[0]
    for i in range(1,len(ar)):
        result = result ^ ar[i]
    return result
array = [4,2,2,1,1]
print(single4(array))
