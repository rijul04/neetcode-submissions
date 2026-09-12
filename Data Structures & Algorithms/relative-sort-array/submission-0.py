class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ret_arr = []
        dic = {}



        for num in arr1:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        for num in arr2:
            ret_arr += [num] * dic[num]
            arr1 = [value for value in arr1 if value != num]
        arr1.sort()
        return ret_arr + arr1