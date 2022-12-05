from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict = {}
        for i in range(len(arr)):
            if arr[i] in dict:
                return True
            double = arr[i] * 2
            dict[double] = i
            if arr[i] % 2 == 0:
                div = arr[i] / 2
                dict[div] = i
        
        return False
        
test = Solution()
arr = [3,1,7,11]
result = test.checkIfExist(arr)
print(result)