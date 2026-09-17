class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)

        left_pointer = 0
        right_pointer = len(nums)-1

        # if left_pointer == right_pointer and nums:
        #     nums[left_pointer] = "_"
        #     return 0

        while left_pointer <= right_pointer:
            while left_pointer <= right_pointer and nums[right_pointer] == val:
                nums[right_pointer] = "_"
                right_pointer -= 1
                count -= 1
            while left_pointer < right_pointer and nums[left_pointer] != val:
                left_pointer += 1

            if left_pointer >= right_pointer:
                break
            
            count -= 1

            nums[left_pointer] = nums[right_pointer]
            nums[right_pointer] = "_"
            left_pointer += 1
            right_pointer -= 1

        print(nums)

        return count
