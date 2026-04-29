# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy

# Approach 1: Brute force using two loops to check all pairs
# Time Complexity: O(n²)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]


# Approach 2: Hashmap (optimal)
# Time Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in hashmap:
                return [hashmap[needed], i]
            
            hashmap[nums[i]] = i