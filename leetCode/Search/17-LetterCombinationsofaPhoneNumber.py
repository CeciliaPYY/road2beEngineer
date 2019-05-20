# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number 
# could represent.

# A mapping of digit to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.

import matplotlib.pyplot as plt 
plt.imshow("./telephone.png")
plt.show()

# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []
        
        d = dict.fromkeys([i for i in range(0,10)])

        d[0] = [' ']
        d[1] = []
        d[2] = ['a', 'b', 'c']
        d[3] = ['d', 'e', 'f']
        d[4] = ['g', 'h', 'i']
        d[5] = ['j', 'k', 'l']
        d[6] = ['m', 'n', 'o']
        d[7] = ['p', 'q', 'r', 's']
        d[8] = ['t', 'u', 'v']
        d[9] = ['w', 'x', 'y', 'z']

        cur = ""
        ans = []
        l = 0
        self.dfs(digits, d, cur, l, ans)
        return ans

    def dfs(self, digits, d, cur, l, ans):
        
        if (l == len(digits)):
            ans.append(cur)
            return
        
        for i in range(len(d[int(digits[l])])):
            cur += d[int(digits[l])][i]
            self.dfs(digits, d, cur, l+1, ans)
            cur.pop()

if __name__ == "__main__":
    digits1 = "23"
    print(Solution().letterCombinations(digits1))
    digits2 = "2"
    print(Solution().letterCombinations(digits2))