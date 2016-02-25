Title: Pascal's Triangle 
Category: 算法
Tags: 算法,leetcode,python
Date: 2015-04-13 19:30

## 问题
from [leetcode](https://leetcode.com/problems/pascals-triangle/)
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

##  思路
简单递归问题，当然不用递归也可以完成

## python代码

```
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <=0:
            return []

        rs = [[1]]
        row = [1]

        while numRows > 1:
            new_row = [1]
            for i in range(0,len(row) - 1):
                print i
                new_row.append(row[i] + row[i+1])
            new_row.append(1)
            rs.append(new_row)
            numRows -= 1
            row = new_row
        return rs
```
