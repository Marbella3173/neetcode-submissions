class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []

        for n in nums:
            if n != val:
                ans.append(n)
        
        nums[:len(ans)] = ans
        
        return len(ans)