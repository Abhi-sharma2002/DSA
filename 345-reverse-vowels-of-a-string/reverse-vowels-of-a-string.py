class Solution:
    def reverseVowels(self, s: str) -> str:
        v='aeiouAEIOU'
        i=0
        j=len(s)-1
        s=list(s)
        while i <j:
            if s[i] not in v:
                i+=1
                continue
            elif s[j]   not in v:
                j-=1
                continue
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return "".join(s)