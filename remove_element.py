from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int
        length = len(nums)

        for i in range(len(nums)):
            while nums[i] == val and i < length:
                j = i
                length = length - 1
                while j < len(nums) - 1:
                    nums[j] = nums[j + 1]
                    j = j + 1
        print(nums)
        return length

print("Starting solution")
test = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print("Running test")
k = test.removeElement(nums, val)
print(k)