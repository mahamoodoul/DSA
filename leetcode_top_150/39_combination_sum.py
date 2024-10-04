from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(remaining_target, start, current_combination):
            if remaining_target == 0:
                res.append(list(current_combination))
                return
            if remaining_target < 0:
                return
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(remaining_target - candidates[i], i, current_combination)
                current_combination.pop()
        backtrack(target, 0, [])
        return res


obj = Solution()
candidates = [2,3,5]
target = 8
output = obj.combinationSum(candidates, target)
print(output)