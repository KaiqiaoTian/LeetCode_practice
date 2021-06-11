"""
Problem
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.



"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        max_value = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            if max_value < sum:
                max_value = sum
            sum = 0
        return max_value




class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
	rich = []
	for wealth in account:
	    rich.append(sum(wealth))
	return max(rich)
