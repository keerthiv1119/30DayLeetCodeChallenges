'''
Author : Keerthi Vutukuri
Date : 02- 04-2020
Name : Happy Number
'''
def Happy(n):
    def Squares_sum(n):
        squaresum = 0
        while(n):
            squaresum = (n % 10) * (n % 10)
            n = n // 10
        return squaresum
    slow = n
    fast = n
    while(True):
        slow = Squares_sum(n)
        fast = Squares_sum(Squares_sum(n))
        if slow != fast:
            continue
        else:
            break
    return slow == 1
n = 19
print(Happy(n))
