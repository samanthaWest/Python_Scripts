class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        
        # Keep looking at numbers while left pointer is stil lless then right pointer
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]


# left and right 2 ends of list
# until left equals right look for a sum
# add sum 
# chec kif sum is greater then or less then to know to decreas
# return index of pairs wit hthe sum of target

