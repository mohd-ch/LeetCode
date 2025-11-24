class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_ele = 0
        sum_dig = 0
        total = 0
        for i in nums:
            sum_ele += i
            for j in str(i):
                sum_dig += int(j)
        total = sum_ele - sum_dig
        return total

# Functional Approach
        return sum(nums) - sum(int(d) for n in nums for d in str(n) )
        