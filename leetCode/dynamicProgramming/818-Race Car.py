import math
class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        # recursion with memorization
        
        # 最多只会走到比 target 多一步，
        position = [0] * (target + 1)
        position[1] = 1
        return self.recursion_with_mem(target, position)
        
    def recursion_with_mem(self, t, position):
        
        if position[t] > 0:
            return position[t]
        
        # n 是大于 target 的第一个可达点的位置
        n = math.ceil(math.log(t + 1, 2))
        
        # 接下来是三种判断情况
        
        # 第一种，一次正好到达
        if (t + 1 ==  (1 << n)):
            position[t] = n
            return position[t]
        
        # 第二种，先到达大于 target 的第一个可达点的位置，再回头
        # AA...AR (nA + 1R) + dp(left)
        position[t] = n + 1 + self.recursion_with_mem((1 << n) - 1 - t, position)
        
        #第三种，先到达小于 target 的最后一个可达点的位置，回头，加速，再回头
        # A...ARA...AR ((n-1)A + 1R + (m)A + 1R) + dp(left)
        for m in range(0, n - 1):
            cur_loc = ((1 << (n-1)) - 1) - ((1 << m) - 1)
            position[t] = min(position[t], n + m + 1 + self.recursion_with_mem(t - cur_loc, position))
        
        return position[t]

if __name__ == "__main__":
    t = 6
    print(Solution().racecar(t))