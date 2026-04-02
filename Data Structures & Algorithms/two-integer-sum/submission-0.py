class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i, num in enumerate(nums):
            
            complement = target - num

            if complement in memory:
                return [memory[complement], i]

            memory[num] = i