from typing import Optional

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dic[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if dic[crs] == []:
                return True
            visit.add(crs)
            # We recursively call dfs on all the prerequisites of crs. If any of these calls returns False, we return False because one of the prerequisites cannot be satisfied.
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            # After visiting all prerequisites and their sub-prerequisites, we remove crs from the visit set and mark it as completed by setting its prerequisites list to empty.
            visit.remove(crs)
            dic[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True