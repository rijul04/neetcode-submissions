class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))
        print(nums)
        longest_consec = curr_consec = 0
        
        curr_num = None
        for num in nums:
            if curr_num == None:
                curr_num = num
                curr_consec += 1
                longest_consec += 1

                continue
            
            if num-1 == curr_num:
                curr_num = num
                curr_consec += 1

                if curr_consec > longest_consec:
                    longest_consec = curr_consec
            else:
                curr_num = num
                curr_consec = 1
        
        return longest_consec
            