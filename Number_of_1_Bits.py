
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        str_n = bin(n)[:]  #bin()方法返回的字符串包含前缀'0b'
        for i in range(len(str_n)):
            if str_n[i] == '1':
                ans += 1
        return ans