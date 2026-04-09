class Solution(object):
    def frequencySort(self, s):
        d = {}

       
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

       
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)

        
        result = ""
        for ch, freq in sorted_items:
            result += ch * freq

        return result