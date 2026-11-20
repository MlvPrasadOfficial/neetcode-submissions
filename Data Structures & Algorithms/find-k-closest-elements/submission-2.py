class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k # bcz this is last k elements possible


        while l < r :
            m = (l+r)//2

            if x - arr[m] > arr[m+k] - x:
                # if left starting part of the window is far away
                # last element in the window 
                l = m + 1
            else :
                r = m 

        return arr[l : l + k] 