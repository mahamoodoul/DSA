class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n !=1 and n not in seen:
            seen.add(n)
            total = 0
            for digit in (str(n)):
                square = int(digit) ** 2
                total = total + square
            n = total
        return n == 1

n = 19
obj = Solution()
output = obj.isHappy(n)
print(output)
