class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []

        for i, num in enumerate(nums):
            if num != val:
                ans.append(num)
        
        nums[:len(ans)] = ans

        return len(ans)