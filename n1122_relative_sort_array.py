from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        
        result = []
        
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]
        
        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)
        
        return result