from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        index = 0
        for i in range(len(nums)):
            if nums[index] < nums[i]:
                index = index + 1
                nums[index] = nums[i]
                length = length + 1
        return length

test = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = test.removeDuplicates(nums)
print(nums)
print(k)