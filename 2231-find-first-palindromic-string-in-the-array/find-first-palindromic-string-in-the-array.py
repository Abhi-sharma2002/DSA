class Solution(object):
    def firstPalindrome(self, words):
       
        for ch in words:
            if ch == ch[::-1]:
                return ch
        return ""
       
        