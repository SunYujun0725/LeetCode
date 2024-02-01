class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp_number = 0
        i = 0
        while (temp_number < n):
            temp_number = 2 ** i
            if temp_number == n:
                return True
            else:
                i += 1
        return False