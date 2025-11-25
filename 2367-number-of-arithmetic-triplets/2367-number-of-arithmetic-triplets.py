class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in nums:
            for j in nums:
                for k in nums:
                    if(i < j < k ):
                        if(j - i) == diff :
                            if(k - j) == diff :
                                count += 1
        return count

        