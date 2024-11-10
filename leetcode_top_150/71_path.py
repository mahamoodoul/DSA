from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or part == "":
                continue
            else:
                stack.append(part)
        return "/" + "/".join(stack)



path = "/home//foo/"
obj = Solution()
output = obj.simplifyPath(path)
print(output)