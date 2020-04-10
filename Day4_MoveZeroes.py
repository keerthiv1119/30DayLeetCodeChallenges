'''
Author : Keerthi Vutukuri
Date : 04- 04-2020
Name :Move Zeroes
'''
nums = [0,1,0,3,12]
count = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[count] = nums[i]
        count += 1
while(count < len(nums)):
    nums[count] = 0
    count += 1
print(nums)
