from collections import Counter
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        target_count = Counter(target)
        arr_count = Counter(arr)
        
        return target_count == arr_count
