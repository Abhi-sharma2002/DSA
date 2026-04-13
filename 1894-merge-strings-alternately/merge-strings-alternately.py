class Solution(object):
    def mergeAlternately(self, word1, word2):
            # s = ""
            # s =[]
            # word1 = list(word1)
            # word2 = list(word2)
            # i = 0
            # j = o
            # while i<len(word1) and j <len(word2):
            #     s.append(word1[i])
            #     s.append(word2[j])
            #     i+=1
            #     j-=1
            # while i<len(word1):
            #     s.append(word1[i])
            # i+=1

            # while j<len(word2):
            #      s.append(word[j])
            # j-=1

            # return "".join(s)
            i = 0
            word1 = list(word1)
            word2 = list(word2)
            k = ""
            m = max(len(word1) , len(word2))
            while i < m:
                if i < len(word1):
                    k += word1[i]
                if i < len(word2):
                    k += word2[i]
                i +=1


            # if len(word1) > i :
            #     k.append(word1[i:len(word1)])
            # elif len(word2) > i :
            #     k.append(word2[i:len(word2)])

            return "".join(k)



        