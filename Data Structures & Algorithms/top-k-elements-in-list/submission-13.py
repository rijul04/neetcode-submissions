class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret_arr = [None] * k
        dic = {}

        for num in nums:
            
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

            if num in ret_arr:
                continue

            smallest_frequency_index = 0
            for i in range(len(ret_arr)):
                if ret_arr[i] == None:
                    smallest_frequency_index = i
                    break
                elif dic[ret_arr[i]] < dic[ret_arr[smallest_frequency_index]]:
                    smallest_frequency_index = i
            
            if ret_arr[smallest_frequency_index] == None:
                ret_arr[smallest_frequency_index] = num
            elif dic[num] > dic[ret_arr[smallest_frequency_index]]:
                ret_arr[smallest_frequency_index] = num
            # print(ret_arr)
            # print(dic)

        return ret_arr

