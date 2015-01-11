# 哈希专题
tip: 要求时间O(n)，又是unsorted的，可以往hash想。

## Python 字典计数
最有效率的写法:
``` python
wdict = {}
for word in words:
    try:
        wdict[word] += 1
    except KeyError:
        wdict[word] = 1
```
## Python 字典循环
经实验，最快的访问是：
``` python
for k in dic.iterkeys():
    do_some_thing_for_key()
```
