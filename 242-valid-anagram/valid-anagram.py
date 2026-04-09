class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for ch in s:
            if ch in d:
                d[ch] +=1
            else:
                d[ch] =1
        for ch in t:
            if ch not in d:
                return False
            d[ch] -=1
            if d[ch] < 0:
                return False
        return True
                
        