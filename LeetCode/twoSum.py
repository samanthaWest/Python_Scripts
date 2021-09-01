# Params - array of integers, and integer target
# Return - two numbers  that add up to the target
# Each input will have exactly one solution and you cant use the same element twice

# Option #1
# Sort the array smallest to largest
# Slice the array where numbers are higher then the target number
# Loop through numbers, check if the target minus your current number exists in the sliced array, make sure to not include the one 
# your looking at in the check

#         sortedList = nums.sort()

#         print(sortedList)

# Maybe only need to sort if its a large list depends on the data set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
        lookupList = nums.copy()
        lookupKey = lookupList.pop(idx)
        value = (target - lookupKey)

        if (value) in lookupList:
            return [idx, lookupList.index(value) + 1]
            break