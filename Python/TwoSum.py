class Solution(object):

    def twoSum(self, nums, target):
       seen = {}
       for index, num in enumerate(nums):
        num_we_lookin = target - num
        if num_we_lookin in seen:
            return [seen[num_we_lookin], index]
        else:
            seen[nums[index]] = index




# Test the function
solution = Solution()
result = solution.twoSum([5, 2, 5, 4, 3, 6, 1, 8], 9)
print(result)