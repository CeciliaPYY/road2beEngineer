这次面试因为面的岗位是 后端开发，所以有些问题其实根本就是不为我所了解的，从一面来说，就真的很大数据，所以......哎，凉凉也是应该的

1. 哈希表的底层实现原理？或者python中dict在C++里面是怎么实现的？
   （这个问题不在我的知识领域之内，所以暂时放一边吧）

2. 已知一棵二叉树，每个结点中存储了一个字符串，现在给定一个结点，求它对应处的字符串？
   （递归二叉树每个结点进行判断，比较简单）

3. 现在有一个房间，这个房间里面只可以待一个人，外面不断有人进来，但是房间里面一次只可以有一个人存在，问我如何设定一个机制使得每个人无论待在房间内或者离开房间的概率都是相同的？（这些人的总数不可知）
   （经典中的经典**蓄水池抽样**，面试之前我只听过名字）

4. 有一个几百万长度的数组，里面每一个位置存储的都是字符，某些连续的字符可以组成一个单词，比如 dangerror，就可以看成是danger和error组成的，现在给定一个单词，如何不用复杂度为O(n2)的方法实现将于该单词所有重合的单词返回。
   （面试官讲了一下方法，没怎么听明白，查了一下答案，打扰了）
   
   https://blog.csdn.net/qq_40840459/article/details/78572202

### 蓄水池抽样
问题：给出一个数据流，这个数据流很大或者长度未知。并且对该数据流中数据只能访问一次。请写出一个随机选择算法，使得数据流中所有数据被选中的概率相等。

解决方法：蓄水池抽样算法

具体思路：先初始化一个集合，集合中有 k 个元素，将此集合作为蓄水池。然后从 第 k+1 个元素开始遍历，并且按一定概率替换掉蓄水池里面的元素。

    Init: a reservoir with the size:k
    for i=k+1 to N:
        M = random(1,i)
        if(M < k)
            Swap the Mth value and the ith value
    end for

具体描述如下，先将 k 个数取出来放入结果集中，然后从第 k + 1 个数开始遍历。假设遍历到第 i 个数，以 k/i 的概率替换掉蓄水池中的某个元素即可。

下面我们用数学归纳法来证明上述命题成立，
1. 第一步初始化。出现在水库中的前 k 个元素，直接保存在数组 A 中，前 k 个数被选中的概率都是一样的，都为 1 / k；
2. 第二步在处理第 k + 1 个元素时，分为两种情况：

情况1：第 k + 1 个元素未被选中，因此蓄水池中没有元素要被替换掉。此时显然蓄水池中所有元素出现的概率都是一样的，概率为p = 1 - p(第 k + 1 个元素被选中) = 1 - k/(k + 1) = 1/(k + 1)；

情况2：第 k + 1 个元素被选中，因此蓄水池中的某个元素要被替换掉，这件事发生的概率为 p = p(第 k + 1 个元素被选中) * p(蓄水池中的某个元素要被替换掉) = k/(k + 1) * 1/k = 1/(k + 1)，那么它未被替换掉的概率为k/(k + 1)，因此可以看出来前 k 个元素和第 k + 1 个元素出现的概率都为k/(k + 1)；

3. 第 k + 1 之后每个元素都重复第 2 步，即第 i 个元素以 k/i 的概率决定是否将它放入蓄水池，最终所有元素出现在蓄水池的概率相等。
   

具体的代码，可以参考：
https://blog.csdn.net/bitcarmanlee/article/details/52719202


