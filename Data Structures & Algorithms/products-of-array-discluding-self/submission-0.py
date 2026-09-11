class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_amount = 0
        product_no_0 = 1
        for num in nums:

            if num != 0:
                product_no_0 *= num
            elif num == 0:
                zero_amount += 1
                if zero_amount > 1:
                    product_no_0 = 0

            product *= num

            


        ret = []

        for num in nums:
            if num == 0:
                ret.append(product_no_0)
                continue
            ret.append(int(product/num))

        return ret