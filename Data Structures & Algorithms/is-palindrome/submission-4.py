class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(filter(str.isalnum, s))
        print(clean_s[::-1])
        print(clean_s)
        return clean_s.lower() == clean_s[::-1].lower()   



