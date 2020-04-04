def maxSubArray(nums):
        maximum_so_far = 0
        maximum_end  = 0
        for i in range(len(nums)):
            maximum_end = maximum_end + nums[i]
            if maximum_so_far < maximum_end:
                maximum_so_far = maximum_end
            if maximum_end < 0:
                maximum_end = 0
        return maximum_so_far
array = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(array))
