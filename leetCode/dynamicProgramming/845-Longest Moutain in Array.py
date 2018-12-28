class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        array_length = len(A)
        inc = [0]*array_length
        dec = [0]*array_length
        for i in range(array_length):
            if i == 0:
                continue
            else:
                if A[i] > A[i-1]:
                    inc[i] = inc[i-1] + 1
        for i in range(array_length-1, -1, -1):
            if i == array_length-1:
                continue
            else:
                if A[i] > A[i+1]:
                    dec[i] = dec[i+1] + 1 
        
        ans = 0
        for i in range(array_length):
            if (inc[i] != 0 and dec[i] != 0):
                ans = max(ans, inc[i] + dec[i] + 1)
        
        return ans
        