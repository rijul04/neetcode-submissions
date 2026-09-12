class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)

        # set3 = set1 >= set2
        ret = []

        for num in set1:
            if num in set2:
                ret.append(num)

        return ret