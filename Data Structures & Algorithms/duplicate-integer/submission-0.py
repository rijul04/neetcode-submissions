class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        nums_set = set(nums)

        if len(nums_set) != len(nums):
            return True

        return False


        