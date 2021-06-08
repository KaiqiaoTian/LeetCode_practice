class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        return nums
