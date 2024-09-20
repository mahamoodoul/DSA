
from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge case: if no words or string is empty
        if not s or not words:
            return []
        
        word_len = len(words[0])           # Length of a single word
        num_words = len(words)             # Total number of words
        total_len = word_len * num_words   # Total length of the concatenated string
        word_count = Counter(words)        # Frequency of each word in words
        print(word_count)
        result = []                        # To store the starting indices of valid substrings
        # Iterate over each starting point
        for i in range(word_len):
            left = i                       # Left pointer for the sliding window
            right = i                      # Right pointer for the sliding window
            current_count = Counter()
                 # Count the words we encounter in the current window
            
            # Move the right pointer to slide over the string `s`
            while right + word_len <= len(s):
                # Extract a word from the string starting at `right`
                word = s[right:right + word_len]
                right += word_len
                
                # If the word is in the list of words
                if word in word_count:
                    current_count[word] += 1
                    
                    # If the word count exceeds the expected count, shrink the window
                    while current_count[word] > word_count[word]:
                        print("when")
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    # If the window contains exactly the right number of words, record the index
                    if right - left == total_len:
                        result.append(left)
                
                # If the word is not in the list, reset the window
                else:

                    current_count.clear()
                    left = right
        
        return result

# Example 1
obj = Solution()
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
output1 = obj.findSubstring(s1, words1)
print(output1)
# Output: [0, 9]





