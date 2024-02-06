class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        min_row = 10000000000
        min_col = 10000000000
        for i in range(len(ops)):
            if ops[i][0] <= min_row:
                min_row = ops[i][0]
            if ops[i][1] <= min_col:
                min_col = ops[i][1]
        
        return min_row*min_col
