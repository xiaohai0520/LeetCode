# 贪心算法

## 1.总体概述
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是最好或最优的算法。

**场景**：最小生成树，哈夫曼编码。

**难点**：转移方程。


## 细节讲解

通俗来讲就是贪心算法的每一步的最优情况都建立在上一步的最有情况下，把问题分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

对于其他问题，贪心法一般不能得到我们所要求的答案。一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。

由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

**基本思路**

1.建立数学模型来描述问题。

2.把求解的问题分成若干个子问题。

3.对每一子问题求解，得到子问题的局部最优解。

4.把子问题的解局部最优解合成原来解问题的一个解。


## 举个栗子
有面值分别为25，10，5，1的硬币数无数枚，我们想用这些硬币凑出99分，找到最少需要使用多少枚硬币。

为了使用最少的硬币数，是不是该这样找呢，先看看该找多少个25分的，诶99／25＝3，好像是3个，要是4个的话，超了。

这样就还少给24，所以还得再用2个10分的和4个1分。

**代码**：
```
def findcoins():
    coins = [25,10,5,1]
    target = 99
    count = 0
    for coin in coins:
        if target >= coin:
            num,target = divmod(target,coin)
            count += num
    return count

```

## 总结
我们使用贪心算法的时候一定要非常注意，因为很多时候局部的最优解并不能得到全局的最优解。

贪心是需要每一步的最优解然后逐步的推出最终的最优解。
