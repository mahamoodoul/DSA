from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1: return 1 if (citations[0] > 0) else 0
        citations.sort(reverse=True)
        h_index = 0
        for i in range(0, len(citations)):
            if citations[i] >= i+1:
                h_index += 1 
        return h_index




obj = Solution()
citations = [3,0,6,1,5]
output = obj.hIndex(citations)
print(output)  # Output will be the sorted merged list