class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if " ".join(sorted(s)) == " ".join(sorted(t)):
            result = True
        else:
            result = False
        return result

