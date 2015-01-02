# 编程原则

## 先想好测试
用`unittest`的TestCase

## 函数加注释
``` python
def func(val1, val2):
    # @param val1: int, blabla....
    # @param val2: list, blabla....
    # @return res: boolean, blabla
```
#### Comment VS Docstring
在编程过程中，如果直接表述思想,用三个单引号的comment，如果是doc说明，用三个双引号。
```python
'''
This is comment
'''
"""
This is docstring
"""
```

编写函数的时候，先写函数名，注释，和pass，防止编译器报错

### 分析复杂度
在代码注释中说明时间复杂度，空间复杂度

### 添加attr
给某一object设置attr。`node.visited = True`, then `hasattr(node, 'visited') == True`.

### Call by value and call by reference
Python中采取混合，mutable的是call by reference（比如dict，list），immutable的是call by value（比如int，string）。注意，比如list是个完整的Object，如果参数传的是list的一部分，就不是call by reference了，因为Object新建了。
所以特别要注意的是，当函数中定义函数，内嵌函数的时候，不要用同一个mutable对象做参数！！！

### private function
只是给别的函数提供帮助的私有函数，可以如下
``` python
class Solution:
    def __private(self):
        print '1',

    def public(self):
        self.__private()
        print '2'

so = Solution()
so.__private() # 报错
so.public() # 1 2
```

### static variable in Class
类似全局变量
``` python
Class Test:
    a = 1
    def func():
        self.a = blahblah
```
每次直接修改self.a，就相当于直接改类中的static a
但是！！慎用，最好不要用。Leetcode多个测试只create one instance，如果多个测试，static变量会污染。

### 短路表达式
python 的短路表达式和C/C++差不多，`statement1 and statement2`，如果statement1 False了，2不合法也没事，因为跑不到。

### mutable object无法hash问题
有时候我们要把list存在set里，会出现错误`TypeError: unhashable type: 'list'`。解决方法是把list转成 immutable的tuple， `tuple(mylist)`就ok了，需要转回来再`list(mytuple)`即可。

### 善用Generator
所谓generator，可以想象成一个存放结果的buff（只能由函数返回），每次算出一个东西，存进去。
要用的时候，循环从buff里读东西，每次一个，读一个消失一个，而且每次只能访问当前的。

###  循环n次的任务
这时候，循环变量i不重要，所以，为了readbility, 用 `_`
``` python
for _ in xrange(len(lt)):
    do_work()
```

## Profile and debug
需要的profile的函数前加修饰器`@profile`，然后`kernprof -l -v Myscript.py`. 需要之前装`pip install line_profile`
### ipython
用ipython debug和测函数运行时间就蛮好。在文件所在目录下运行ipython，
``` python
>>> import myscript
>>> so = myscript.Solution()
>>> timeit so.solve(XXX)
```



## Performance的坑
``` python
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    15                                                   #@profile
    16                                                   def bfs(x, y):
    17        80           55      0.7      0.0              if board[x][y] == 'O':
    18        18           11      0.6      0.0                  board[x][y] = 'U'
    19        18           20      1.1      0.0                  queue.append((x,y))
    20                                                       else:
    21        62           34      0.5      0.0                  return
    22                                                       # queue = collections.deque((x,y)) This will not insert as tuple
    23  13368476      9312078      0.7      4.2              while queue:
    24  13368458     12097235      0.9      5.4                  e = queue.popleft()
    25  66842290     45758003      0.7     20.5                  for d in DIRS:
    26  53473832     53172182      1.0     23.9                      nx, ny = e[0]+d[0], e[1]+d[1]
    27                                                               #if nx < H and nx >=0 and ny < W and ny >= 0 and board[nx][ny] == 'O':
    28  53473832     55052477      1.0     24.7                      if nx >= H or nx < 0 or ny >= W or ny < 0 or board[nx][ny] != 'O':
    29  32304208     20012341      0.6      9.0                          continue
    30  13368440     13311806      1.0      6.0                      queue.append((nx, ny))
    31  13368440     14016306      1.0      6.3                      board[e[0]][e[1]] = 'U'
```
赋值和 for ... in ...是性能的坑，用 map(), reduce(), list comprehension 会快一点
