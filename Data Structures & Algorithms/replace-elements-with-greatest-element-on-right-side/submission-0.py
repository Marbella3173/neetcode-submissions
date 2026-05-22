class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans  = []

        max = -1

        for i in range(len(arr)-1, -1, -1):
            ans.append(max)

            if max < arr[i]:
                max = arr[i]
        
        res = ans[::-1]

        return res