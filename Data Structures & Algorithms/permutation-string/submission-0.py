class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s1's permutation cannot be a substring of s2
        if len1 > len2:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        # Count frequency of characters in s1 and the first window of s2
        for i in range(len1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        # Count how many characters match out of 26 English letters
        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
                
        # Slide the window across s2
        for i in range(len2 - len1):
            if matches == 26:
                return True
            
            # Character entering the right side of the window
            r = ord(s2[i + len1]) - ord('a')
            s2_counts[r] += 1
            if s1_counts[r] == s2_counts[r]:
                matches += 1
            elif s1_counts[r] + 1 == s2_counts[r]:
                matches -= 1
                
            # Character leaving the left side of the window
            l = ord(s2[i]) - ord('a')
            s2_counts[l] -= 1
            if s1_counts[l] == s2_counts[l]:
                matches += 1
            elif s1_counts[l] - 1 == s2_counts[l]:
                matches -= 1
                
        return matches == 26