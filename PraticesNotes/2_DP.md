# DP专题
[25题](http://www.cnblogs.com/keanuyaoo/p/3253505.html)

**二元关系可以用图来建模（如矩形嵌套）**

## 01背包
### 题目
有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使价值总和最大。
### 解答
状态转移方程:
$$d[i][j] = max\{d[i-1][j], d[i-1][j-c[i]]+w[i]\}$$
其中d[i][j]前i件物品放入剩余容量为j的背包可获得的最大价值。注意i和j为0的时候也是状态，所以要保留出来。
``` python
    for i in [1..n]:
        for j in [0..V]:
            if j >= w[i]:
            d[i][j] = max(d[i-1][j], d[i-1][j-c[i]] + w[i])
```

**滚动数组优化空间**
首先，把上面伪代码中j的顺序改成[V..0], 不影响结果。 因为每次只与上一行交互（第i行与第i-1行），而目标状态是d[n][V]，所以只需要最后一行就行了。用滚动数组不断覆盖前一层。

``` python
    for i in [1..n]:
        for j in [V..0]:
            if j >= w[i]:
            f[j] = max(f[j], f[j-c[i]] + w[i])
```

f[j]更新之前，f[j]保存的是d[i-1][j]的内容，更新后是d[i][j]，由于初始化，i = 0时候本来就是0。

**Edit Distance**问题，需要左边，上边，左上，就无法用一位滚动数组了，用二维的，加上与运算来回切得到答案。

## 完全背包
和01背包不一样的是，完全背包每个物品可以选无限次。01背包中逆序是为了保证“选择第i个物品”时，依赖是没有选第i个物品的子结果d[i-1][j-c[i]]，完全背包没有这依赖，所以顺序就行了。

``` python
for i in [1..n]:
    for j in [0..V]:
        if j >= w[i]:
            f[j] = max(f[j], f[j-c[i]] + w[i])
```

## Unique Binary Search Trees
可以知道，树的问题一般都有重复子问题（always想到递归）
一个树有多少可能性，取决于左子树和右子树可能性的乘积。
d[i] 表示i个项时候的可能性数，则
$$d[n+1] = \sum_{j=0}^{n}d[j]d[n-j]$$
建树的唯一性：以i为根节点的树，左子树[0..i-1]构成，右子树[i+1..n]构成。

## Palindrome Partitioning II
参考[水中的鱼博客](http://fisherlei.blogspot.com/2013/03/leetcode-palindrome-partitioning-ii.html)
一般求最优解的问题，都是用DP。这题用了双重DP


D[i,n]表示区间[i,n]之间最小的cut数。转换成一维，D[i]表示[i,n]之间的最小cut数。D[i] = min(1+D[j+1])。同时判断[i,j]是否为回文用一个dp, P[i][j] = truw if [i,j]是回文。
`P[i][j] = (s[i]==s[j] && P[i+1][-1])` 边界情况是j-i<2
