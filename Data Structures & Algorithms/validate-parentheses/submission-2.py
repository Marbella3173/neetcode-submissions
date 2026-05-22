class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        for n in s:
            if n == '(' or n == '{' or n == '[':
                ans.append(n)
            elif ans and ans[-1] == '(' and n == ')':
                ans.pop()
            elif ans and ans[-1] == '{' and n == '}':
                ans.pop()
            elif ans and ans[-1] == '[' and n == ']':
                ans.pop()
            else:
                return False
        
        return True if not ans else False