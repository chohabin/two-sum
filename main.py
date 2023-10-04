from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    end = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (target == nums[i] + nums[j]):
                result = [i, j]
                end = 1
                break
        if (end == 1):
            break
    return result