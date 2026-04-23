class Solution(object):
    def isValid(self, s):
        stack =[]
        map ={'}':'{',')':'(',']':'['}
        for i in s:
            if i in map:
                top = stack.pop() if stack else '#'
                if map[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack
        