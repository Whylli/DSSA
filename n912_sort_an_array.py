from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
           
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
           
            return merge(left, right)
        
        return mergeSort(nums)