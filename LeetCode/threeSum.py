# Bad Solution kept going 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print("method")
        # Params : Integer array
        # Return : All triplets
        # Requirement for triples -
        #   - i != j, i !=k, j != k (none of the numbers can be the same)
        #   - nums sum === 0
        
        # Hash Table Solution aka Dictionary in Python
        # Store the occurances of certain numbers in the dicrioary in a list containing those same numbers
        # The key would have to be relevent to the problem
        
        hashtable = {}
        triplets = []
        
        if len(nums) >= 3:
        # Create Hash Table
            for n in nums:
                if n not in hashtable:
                    occurances = nums.count(n)
                    hashtable[n] = [n] * occurances

            # Doesn't have to use all numbers, just has to create the triplets === 0 and not re-using any
            # Check 2 numbers at a time and see if the different between those two numbers added and 0 exists in the list

            # n_1 number being pivoted with all other numbers
            # n_2 second loop number being used with the pivot number

            # Cycle through the keys first set for the pivit key
            for pivit_key in hashtable.keys():
                pivit_key_count = len(hashtable[pivit_key])

                # Cycle through the keys on the pivot key
                for key in hashtable.keys():

                    if (pivit_key + key) > 0:
                         missing_val = 0 - (pivit_key + key)
                    else:
                         missing_val = abs(pivit_key + key)

                    key_count = len(hashtable[key])
                    print((key == pivit_key and pivit_key_count == 1))
                    print((key == missing_val and key_count == 1))
                    print((missing_val == pivit_key and pivit_key_count == 1))
                    if not (key == pivit_key and pivit_key_count == 1) and\
                        not (key == missing_val and key_count == 1) and\
                        not (missing_val == pivit_key and pivit_key_count == 1):
                            newTriplet = [ pivit_key, key, missing_val ]
                            newTriplet.sort()
                            if missing_val in hashtable and newTriplet not in triplets:
                                triplets.append(newTriplet)
                                break

        
        return triplets   

# Good Solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 3 Elements to sum to 0
        # We cant use duplicates in the solution
        
        # Sort input array
        result = []
        sortedArray = nums.sort() 
        
        print(sortedArray)
        
        for i, a in enumerate(nums):
            
            # Contniue to next interation if previous has already been used
            if i > 0 and a == nums[i-1]:
                continue
            
            # left will be start of the list
            # right will be end of the list
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # Decrease end right pointer
                    r -= 1
                elif threeSum < 0:
                    # shift left pointer
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    
                    # Update Our Pointers
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return result