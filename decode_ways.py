from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        # dp ={len(s): 1}
        
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
        #     res = dfs(i+1)
        #     if(i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
        #         res += dfs (i+2)
        #     dp[i] = res
        #     return res
        # return dfs(0)
        memo = {}
        def dp(i):
            if i >= len(s): return 1
            if s[i] == '0': return 0
            if i in memo: return memo[i]

            res = dp(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += dp(i+2)
            memo[i] = res
            return res
        
        return dp(0)

            


nums_str = "22612323123421221112222232"
obj = Solution()
print(obj.numDecodings(nums_str))