# https://leetcode.com/problems/two-sum/
# one-pass hash table


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for idx, num in enumerate(nums):
            n = target - num
            if n not in num_set:
                num_set[num] = idx
            else:
                return [num_set[n], idx]
