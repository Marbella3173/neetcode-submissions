class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for n in operations:
            if n == '+':
                ans.append(ans[-1] + ans[-2])
            elif n == 'D':
                ans.append(ans[-1] * 2)
            elif n =='C':
                ans.pop()
            else:
                ans.append(int(n))
        
        score = sum(ans)

        return score