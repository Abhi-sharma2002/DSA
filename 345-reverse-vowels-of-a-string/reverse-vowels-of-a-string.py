class Solution(object):
    def reverseVowels(self, s):
        a = 0
        b = len(s)-1
        s = list(s)
        v = "aeiouAEIOU"
        while a < b:

            if s[a] not in v:
                a += 1
                continue
            if s[b] not in v:
                b -=1
                continue
            # else:
            #     a += 1
            #     b -=1

            if s[a] in v and s[b] in v :
                s[a],s[b] = s[b],s[a]
                a += 1
                b -=1
        return "".join(s)
         

            
        