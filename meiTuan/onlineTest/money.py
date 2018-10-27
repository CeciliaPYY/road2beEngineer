# 给你六种面额 1、5、10、20、50、100 元的纸币，
# 假设每种币值的数量都足够多，编写程序求组成N元
# （N为0~10000的非负整数）的不同组合的个数。 

moneyBank = [1,5,10,20,50,100]
class Solution():
    def numOfCombination(self, n):
        if n <= 0:
            return 0
        else:
            count1 = count5 = count10 = count20 = count50 = count100 = 0
            n1 = n5 = n10 = n20 = n50 = n100 = n
            while(n1):
                count1 += 1
                n1 /= 1
            while(n5):


        
