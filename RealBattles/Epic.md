### http://www.mitbbs.com/article_t/JobHunting/32208743.html

机考分为两个部分，前60分钟是给你一个叫MIIS的编造出来的新的语言，有详细的语法
讲解，然后做20道题。题不难，可能有2-3题有一点tricky。接下来给160分钟做4道编
程题，允许用主流的Java c++ c＃Python Ruby以及非主流的VB语言。题目如下：

1. 一个叫bulls and cows的游戏：给两个单词来match字符，如果wordA[i] == wordB[
j] && i == j 则算作一个bull，如果wordA[i] == wordB[j] && i!=j 则算作一个cow
，求bulls和cows的数量。eg: dusts Vs. studs 返回 1 bulls, 4 cows

  + 利用对称性排除，加上random的效率也很好。


2. 一个N*N的棋盘，格子里的数字如果是1表示自己棋子，2表示对方棋子，0表示空。
如果放一个Rook到棋盘的空格中，怎么放才能使得放下去之后的那一时刻，抓到的对方
棋子的数量最多。
  + 没看懂

3. 用0-9数字生成一个长度为N的电话号码，(1) 号码不能用某三个数字 {a1, a2, a3}
(2) 号码当中4只能出现在首位 （3）号码当中不能有任意两个连续的数字相同。求
print出所有可能的号码。
  + dfs + 剪枝

3. 给一个0-9的手机键盘每个数字代表着某几个字母，比如1代表a,b,c; 2代表d, e, f
等等。按键盘N次，求print所有可能生成的string。

### http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=115252&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311

### http://blog.csdn.net/lsdtc1225/article/details/39949367 （题比较全，答案不一定好）
