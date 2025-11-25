class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # self logic
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j < k :
                        if nums[j] - nums[i] == diff :
                            if nums[k] - nums[j] == diff :
                                count += 1
        return count

        # Referred and understanded advanced
        #  s = set(nums)
        #     count = 0
        #     for x in nums:
        #         if x + diff in s and x + 2*diff in s:
        #             count += 1
        #     return count

    
    