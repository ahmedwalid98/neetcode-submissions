class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start = 0
        sorted_num = sorted(nums)
        last = len(sorted_num) - 1
        mid = 1
        result = []
        if len(sorted_num) == 3:
            if sum(sorted_num) == 0:
                return [sorted_num]
            else:
                return []
        
        while start < last:
            i = start + 1
            while i < last:
                if sorted_num[start] + sorted_num[i] + sorted_num[last] == 0:
                    if [sorted_num[start], sorted_num[i], sorted_num[last]] not in result:
                        result.append([sorted_num[start], sorted_num[i], sorted_num[last]])
                    last -= 1
                if sorted_num[start] + sorted_num[i] + sorted_num[last] > 0:
                    last -= 1
                else:
                    i += 1
            start += 1
            last = len(sorted_num) - 1
       
        return result

        [-2, -1, 1, 2]