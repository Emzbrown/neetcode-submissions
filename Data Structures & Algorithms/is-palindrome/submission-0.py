class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = s.lower()
        reversed = ''
        normal= ''
        for i in d :
            if i.isalnum():
                reversed= i + reversed 
                normal = normal+i

        if normal== reversed:
            return True 
        else:
            return False 
