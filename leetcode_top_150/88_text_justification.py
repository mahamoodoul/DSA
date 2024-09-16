from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            line_len = 0

            # Pack as many words as possible into the current line
            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1
            print(line_words, line_len)

            # Determine if this is the last line
            is_last_line = i == n
            gaps = len(line_words) - 1

            # If last line or line contains only one word, left-justify
            if is_last_line or gaps == 0:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Calculate the total number of spaces to distribute
                total_spaces = maxWidth - line_len
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ''
                for j in range(gaps):
                    line += line_words[j]
                    # Distribute extra spaces to the left gaps
                    space_count = spaces_per_gap + (1 if j < extra_spaces else 0)
                    line += ' ' * space_count
                line += line_words[-1]  # Add the last word without extra space

            result.append(line)

        return result

obj = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = obj.fullJustify(words, maxWidth)
print(output)