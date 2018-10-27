# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"及"-1E-16"都表示
# 数值，但"12e","1a3.14","1.2.3","+-5"及"12e5.4""都不是

# 表示数值的字符串遵循模式A[.[B]][e|EC]或者.B[e|EC]，其中A为数值的整数部分
# B为紧跟着小数点为数值的小数部分，C紧跟着'e'或'E'为数值的指数部分。在小数里
# 可能没有数值的整数部分。比如.123等于0.123，因此 A 部分不是必须的。如果一个数
# 没有整数部分，那么它的小数部分不能为空。

# A 和 C都是可能以 '+' 或者 '-' 开头的 0~9 的数位串；B也是 0~9 的数位穿，但
# 前面不能有正负号。

def scanNum(ss):
    if ss == False:
        return True
    elif len(ss) == 0:
        return True 
    else:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        isAllNumeric = [False for _ in range(len(ss))]
        for i in range(len(ss)):
            if ss[i] in nums:
                isAllNumeric[i] = True
        if sum(isAllNumeric) == len(ss):
            return True
        else:
            return False

def isNumeric(s):
    if len(s) == 0:
        return 
    partA = False
    partB = False
    partC = False
    if "." in s:
        partA = s.split(".")[0]
        if "e" in s or "E" in s:
            if "e" in s:
                partB = s.split(".")[1].split("e")[0]
                partC = s.split(".")[1].split("e")[1]
            else:
                partB = s.split(".")[1].split("E")[0]
                partC = s.split(".")[1].split("E")[1]
        else:
            partB = s.split(".")[1]
    else:
        if "e" in s or "E" in s:
            if "e" in s:
                partA = s.split("e")[0]
                partC = s.split("e")[1]
            else:
                partA = s.split("E")[0]
                partC = s.split("E")[1]
        else:
            partA = s
    if partA.startswith("+"):
        partA = partA.lstrip("+")
    elif partA.startswith("-"):
        partA = partA.lstrip("-")
    else:
        partA = partA
    if partC.startswith("+"):
        partC = partC.lstrip("+")
    elif partC.startswith("-"):
        partC = partC.lstrip("-")
    else:
        partC = partC
    print(partA, partB, partC)
    if partA and scanNum(partA) and scanNum(partB) and scanNum(partC):
        return True
    else:
        return False


print(isNumeric("+100"))
print(isNumeric("5e2"))
print(isNumeric("-123"))
print(isNumeric("3.1416"))
print(isNumeric("-1E-16"))

print(isNumeric("12e")) # 通不过
print(isNumeric("1a3.14"))
print(isNumeric("1.2.3")) # 通不过
print(isNumeric("+-5"))

# 上书写法存在很多问题，一个是判断条件太多还有就是 split 方法不能在此处使用，例如
# "1.2.3"并不代表一个数值，但是split之后变为[1,2,3]则满足输出条件，放弃...

# -*- coding:utf-8 -*-
class Solution1:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False
        
        numeric = Solution1().scanInteger(s)

        # 如果出现"."，接下来是数字的小数部分
        if s[0] == ".":
            # 1.小数可以没有整数部分；2.小数点后可以没有数字；3.小数点前后都有数字
            numeric = Solution1().scanUnsignedInteger(s[1:]) or numeric
        if s[0] == "e" or s[0] == "E":
            # 1.当e或E前面没有数字时，整个字符串不能表示数字；2.当e或E后面没有数字时，整个字符串不能表示数字；
            numeric = Solution1().scanInteger(s[1:]) and numeric

    def scanUnsignedInteger(self, ss):
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        isAllNumeric = [False for _ in range(len(ss))]
        for i in range(len(ss)):
            if ss[i] in nums:
                isAllNumeric[i] = True
        if sum(isAllNumeric) == len(ss):
            return True
        else:
            return False

    def scanInteger(self, ss):
        if ss.startswith("+") or ss.startswith("-"):
            ss = ss[1:]
        return Solution1().scanUnsignedInteger(ss)

print(Solution1().isNumeric())
print(Solution1().isNumeric("+100"))
# print(isNumeric("5e2"))
# print(isNumeric("-123"))
# print(isNumeric("3.1416"))
# print(isNumeric("-1E-16"))

# print(isNumeric("12e")) # 通不过
# print(isNumeric("1a3.14"))
# print(isNumeric("1.2.3")) # 通不过
# print(isNumeric("+-5"))

# -*- coding:utf-8 -*-
class Solution1:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False

        numeric = Solution1().scanInteger(s)
        print(s)
        # 如果出现"."，接下来是数字的小数部分
        if s[0] == ".":
            # 1.小数可以没有整数部分；2.小数点后可以没有数字；3.小数点前后都有数字
            numeric = Solution1().scanUnsignedInteger(s[1:]) or numeric
        if s[0] == "e" or s[0] == "E":
            # 1.当e或E前面没有数字时，整个字符串不能表示数字；2.当e或E后面没有数字时，整个字符串不能表示数字；
            numeric = Solution1().scanInteger(s[1:]) and numeric
    
    def scanUnsignedInteger(self, ss):
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        isAllNumeric = [False for _ in range(len(ss))]
        for i in range(len(ss)):
            if ss[i] in nums:
                isAllNumeric[i] = True
        if sum(isAllNumeric) == len(ss):
            return True
        else:
            return False

    def scanInteger(self, ss):
        if ss.startswith("+") or ss.startswith("-"):
            ss = ss[1:]
        return Solution1().scanUnsignedInteger(ss)

print(Solution1().isNumeric("+100"))
print(Solution1().isNumeric("5e2"))
print(Solution1().isNumeric("-123"))
print(Solution1().isNumeric("3.1416"))
print(Solution1().isNumeric("-1E-16"))

# 算了，心累还是正则表达式吧
import re
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False
        else:
            return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\-\+]?[0-9]+)?$", s)