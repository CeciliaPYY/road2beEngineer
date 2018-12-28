class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = [0 for _ in range(len(S))]
        r = [0 for _ in range(len(S))]
        for i in range(len(S)):
            if i == 0:
                l[i] = int(S[i] == '1')
            else:
                l[i] = l[i-1] + int(S[i] == '1')
        
        for i in range(len(S)-1, -1, -1):
            if i+1 == len(S):
                r[i] = int(S[i] == '0')
            else:
                r[i] = r[i+1] + int(S[i] == '0')
        
        ans = []
        for i in range(1, len(S)):
            ans.append(min(l[i-1]+r[i], l[len(S)-1], r[0]))
        
        return min(ans)

if __name__ == "__main__":
    S = "100000001010000"
    print(Solution().minFlipsMonoIncr(S))