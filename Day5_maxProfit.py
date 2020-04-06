'''
Author : Keerthi Vutukuri
Date : 02- 04-2020
Name : Best Time to Buy and Sell Stock II
'''
def maxProfit(prices):
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit
array = [7,1,5,3,6,4]
print(maxProfit(array))
