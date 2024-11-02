from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in hash_map:
                hash_map[key].append(strs[i])
            else:
                hash_map[key] = [strs[i]]
        output = []
        for key, value in hash_map.items():
            output.append(value)
        return output

       






obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
output = obj.groupAnagrams(strs)
print(output)