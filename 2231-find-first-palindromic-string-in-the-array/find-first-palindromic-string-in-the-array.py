class Solution(object):
    def firstPalindrome(self, words):
       
        for ch in words:
            i =0
            j = len(ch) -1
            while i < j:
                wo = list(ch)
                if  wo[i] != wo[j]:
                    break
                i+=1
                j-=1
                
            if i >= j:

                return ch
        return ""
       
        