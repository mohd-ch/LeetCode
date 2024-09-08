class Solution:
    def maxDepth(self, s: str) -> int:
        current = 0
        maxDepth = 0
        for char in s:
            if char == '(':
                current += 1
                maxDepth = max(maxDepth, current)
            elif char == ')':
                current -= 1
        return maxDepth