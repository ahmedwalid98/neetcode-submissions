class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = 0
        i = 0
        prod = 1
        result = []
        while True:
            if j == len(nums):
                break
            
            if i == j:
                i += 1
                continue
            
            if i == len(nums):
                j += 1
                result.append(prod)
                i = 0
                prod = 1
            prod = prod * nums[i]
            i +=1
        
        return result