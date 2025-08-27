class Solution(object):
    def TwoSum(self, nums, target):
        heatmap = {}  # store num:index
        for i, num in enumerate(nums):  # loop with index & value
            complement = target - num   # needed number
            if complement in heatmap:   # check if it exists
                return [heatmap[complement], i]  # return indices heatmap[complement] → complement ka index deta hai.   i → current number ka index hai.
            heatmap[num] = i  # save current num:index
        return []  # no pair found


# Input values (must be OUTSIDE the class)
nums = [2, 5, 7, 9]
target = 7

# Create object of Solution class
result = Solution()

# Call method and print
print("Indices:", result.TwoSum(nums, target))  # expected: [0, 1]