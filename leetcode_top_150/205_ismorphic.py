    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    # To store character mappings from s to t and t to s
        map_s_to_t = {}
        map_t_to_s = {}
        
        # Iterate over both strings simultaneously
        for char_s, char_t in zip(s, t):
            # Check if the character from s is already mapped to a character in t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            # Check if the character from t is already mapped to a character in s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            
            # Establish the mapping in both dictionaries
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
        
        return True