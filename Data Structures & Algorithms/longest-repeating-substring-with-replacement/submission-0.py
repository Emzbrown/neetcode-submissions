class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        counts = {}  # Renamed from 'dict' to avoid shadowing built-in dict
        mat = 0
        emzy = 0
        
        while r < len(s):
            # 1. Always update character frequency and max frequency (mat)
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            mat = max(mat, counts[s[r]])
            
            # 2. Shrink window from the left if replacements needed > k
            while (r - l + 1 - mat) > k:
                counts[s[l]] -= 1
                l += 1
            
            # 3. Update maximum valid window size and move right pointer forward once
            emzy = max(emzy, r - l + 1)
            r += 1
            
        return emzy