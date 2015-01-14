# 二分专题

## Median of Two Sorted Arrays
两个数组长度分别为m,n， median为中间一个数或者中间两数之平均。找中间的数就转化为找第k个数，复杂度O(log(m+n))。
举[南郭子綦博客里的例子](http://www.cnblogs.com/zuoyuan/p/3759682.html)，`A = [1,3,5,7]`, `B = [2,4,6,8,9,10]`。如果要求第7小的数，k/2=3, A的第三个数A[2]=5; k-k/2=4， B的第四个数B[3]=8。而A[2]<B[3]，则A[0],A[1],A[2]不可能出现第7小的数，因为A[2]<B[3]，比A[2]小的数最多为A[0], A[1], B[0], B[1], B[2] 这5个数，A[2]最多是第6小的意思。所以把A[0], A[1], A[2]砍了，变成求_getK(A[pa:], B, 4)， 对B同理。
``` python
    def _getKth(self, A, B, k):
        lenA, lenB = len(A), len(B)
        if lenA > lenB:
            return self._getKth(B, A, k)
        if lenA == 0:
            return B[k-1]
        # Edge case
        if k == 1:
            return min(A[0], B[0])
        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self._getKth(A[pa:], B, k-pa)
        else:
            return self._getKth(A, B[pb:], k-pb)

```

## 寻找上下边界
对于一个有序数组，找某一值的上下边界。找不到返回-1。
比如找下边界，核心是**找到最后一个大于等于key的位置**:
``` python
def low_bound(arr, key):
    def p(v): return v >= key
    low, high = 0, len(arr) - 1
    res = -1
    while low <= high:
      mid = low + (high-low)/2
      # mid = (low+high)/2 might overflow
      if p(arr[mid]):
      # we found a potential minimum x, but keep check smaller one
        res = mid
        high = mid - 1
      else:
        # predicate is false, go to right to find true val
        low = mid + 1
    res = res if arr[res] == key else -1
    return res
```
判断每次mid的值是否大于等于key，是的话说明找到一个潜在的，先存着，继续往左找。
注意，大于等于可能到循环结束找的都是大于的，所以需要在结尾加个判断。

上边界同理，核心是**找到最后一个小于等于key的位置**：
``` python

def high_bound(arr, key):
  def p(v): return v <= key
  low, high = 0, len(arr) - 1
  res = -1
  while low <= high:
      mid = low + (high-low)/2
      if p(arr[mid]):
      # we found a potential maximum x, but keep check bigger one
        res = mid
        low = mid + 1
      else:
        high = mid - 1
  res = res if arr[res] == key else -1
  return res

```
### 第一个不小于x， 第一个不大于x
### Rotated Array 找最小值
