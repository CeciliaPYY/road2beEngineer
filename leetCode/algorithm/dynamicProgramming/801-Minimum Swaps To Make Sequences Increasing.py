class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length = len(A)
        swap = [length]*length
        keep = [length]*length
        
        keep[0] = 0
        swap[0] = 1
        for i in range(1, length):
            # 不交换之前就已经严格递增的情况
            if (A[i] > A[i-1] and B[i] > B[i-1]):
                # A[i] B[i] 和 A[i-1] B[i-1] 都不交换
                keep[i] = keep[i-1]
                # A[i] B[i] 和 A[i-1] B[i-1] 都交换
                swap[i] = swap[i-1] + 1
            # 交换之后才严格递增的情况
            if (B[i] > A[i-1] and A[i] > B[i-1]):
                # 交换 A[i-1] B[i-1]，不交换 A[i] B[i]
                keep[i] = min(keep[i], swap[i-1])
                # 交换 A[i] B[i]，不交换 A[i-1] B[i-1]
                swap[i] = min(swap[i], keep[i-1] + 1)
        return swap, keep
        
        

if __name__ == "__main__":
    A = [1,3,5,4]
    B = [1,2,3,7]
    print(Solution().minSwap(A, B))