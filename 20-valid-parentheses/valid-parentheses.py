class Solution(object):
    def isValid(self, s):
        stack =[]
        map={'}':'{',')':'(',']':'['}
        for c in s:
            if c in map:
                top = stack.pop() if stack else '#'
                if map[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack
        