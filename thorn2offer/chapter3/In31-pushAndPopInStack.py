# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or popV == []:
            return
        else:
            stack = []
            length = len(pushV)
            equal = sum([True for i in popV if i in pushV])
            if equal == length:
                for i in range(pushV.index(popV[0])+1):
                    stack.append(pushV[i])

                pushV = [p for p in pushV if not p in stack]
                while popV:
                    if stack[-1] == popV[0]:
                        popV.pop(0)
                        stack.pop()
                    else:
                        if pushV:
                            stack.append(pushV[0])
                            pushV.pop(0)
                        else:
                            break
                if popV == []:
                    return True
                else:
                    return False
            else:
                return False

print(Solution().IsPopOrder([1,2,3,4,5], [4,5,3,2,1]))
print(Solution().IsPopOrder(1], [2]))