# Define the function without 'self'
def TwoSum(nums, target):
    heatmap = {}  # Dictionary to store number and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in heatmap:
            return [heatmap[complement], i]
        heatmap[num] = i
    return []

# Input values
nums = [2, 5, 7, 9]
target = 7

# Call the function and print result
result = TwoSum(nums, target)
print("Indices:", result)
