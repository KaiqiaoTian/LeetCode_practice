"""
Problem
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.





"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        v = []
        for i in range(len(candies)):
            if(candies[i] + extraCandies +1 > max(candies)):
                v.append(True)
            else:
                v.append(False)
        return v
