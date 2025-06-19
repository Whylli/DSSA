from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        nums_with_indices.sort()
       
        i, j = 0, len(nums) - 1
        
        while i < j:
            current_sum = nums_with_indices[i][0] + nums_with_indices[j][0]
            
            if current_sum == target:
                return [nums_with_indices[i][1], nums_with_indices[j][1]]
            elif current_sum < target:
                i += 1
            else:
                j -= 1
 
        return []