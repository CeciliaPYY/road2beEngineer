# 题目:Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, and there exists 
# one unique longest palindromic substring.

# 思路一：就要以每一个字符为中心，像两边扩散来寻找回文串，这个算法的时间复杂度是O(n*n)，
# 可以通过OJ，就是要注意奇偶情况，由于回文串的长度可奇可偶，两种形式的回文串都要搜索

string = 'abdccdef'

# class Solution(object):
#     def longestPalindromicSubstring(self, string):

# -*- coding:utf-8 -*-
class Palindrome:
    def getLongestPalindrome(self, A, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1 
        else:
            maxLength = 1
            for i in range(1, n-1):
                j = 1
                while i-j>0 and i+j<n-1:
                    if A[i-j] == A[i]:
                        print(maxLength)
                        maxLength += 1
                    elif A[i+j] == A[i]:
                        print(maxLength)
                        maxLength += 1
                    elif A[i-j] == A[i+j]:
                        maxLength += 2
                if maxLength <= 1:
                    continue
            return maxLength

# 思路二：我们维护一个二维数组dp，其中dp[i][j]表示字符串区间[i,j]是否为回文串，
# 当 i=j 时，字符串长度为1，则肯定是回文串；而当 j-i = 1 时，说明 s[i] 和 s[j]
# 是相邻字符串，此时若s[i] = s[j],则是回文串，否则不是回文串；而当 j-i > 1 时，
# 除了判断 s[i] 和 s[j] 是否相等，还需要判断 dp[i+1][j-1]是否为真，如果是，则为
# 回文串。
# 得到的状态转移方程如下：
# dp[i][j] = 1 if i=j
# dp[i][j] = 1 if j-i=1 and s[i]=s[j]
# dp[i][j] = 1 if j-i>1 and s[i]=s[j] and dp[i+1][j-1] = 1


string = 'abdccdef'
n = len(string)
dp = [[0 for _ in range(n)] for _ in range(n)]
longestLength = 0

for i in range(n):
    dp[i][i] = 1

for i in range(0,n-1):
    if string[i] == string[i+1]:
        dp[i][i+1] = 1
    if longestLength < 2 and dp[i][i+1]:
        longestLength = 2

for l in range(2, n):
    for i in range(n-l):
        if string[i] == string[i+l]:
            dp[i][i+l] == dp[i+1][i+l-1]
            if longestLength < l+1 and dp[i][i+l]:
                longestLength = l+1
        else:
            dp[i][i+l] = 0

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    start = 0
    maxsize = 1
    length = len(s)
    c = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
    	c[i][i] =1
    for i in range(length-1):
    	if s[i]==s[i+1]:
    		c[i][i+1] = 1
    		if 2>maxsize and c[i][i+1] :
    			maxsize =2

    for l in range(2,length):
    	for i in range(length-l):
    		if s[i]==s[i+l]:
    			c[i][i+l] = c[i+1][i+l-1]
    			if l+1>maxsize and c[i][i+l]:
    				maxsize = l+1
    		else:
    			c[i][i+l] = 0
    return maxsize

class Palindrome(object):
    def getLongestPalindrome(self, A, n):
        # write code here
        dp = [[0 for _ in range(n)] for _ in range(n)]
        longestLength = 0
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n-1):
            if A[i] == A[i+1]:
                dp[i][i+1] = 1
                if longestLength <2 and dp[i][i+1]:
                    longestLength = 2
                
        for l in range(2, n):
            for i in range(n-l):
                if A[i] == A[i+l]:
                    dp[i][i+l] = dp[i+1][i+l-1]
                    if dp[i][i+l]:
                        longestLength = max(longestLength, l+1)
        
print(Palindrome().getLongestPalindrome("baabccc",7))

