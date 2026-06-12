class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_s = ''.join(filter(str.isalnum, s))
        return clean_s == clean_s[::-1]