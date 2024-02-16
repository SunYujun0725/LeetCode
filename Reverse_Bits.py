class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = bin(n)[:]
        str_n = str_n[::-1]
        ans = 0
        j = 31
        for i in range(len(str_n)):
            if str_n[i] == '1':
                ans += 2**j
            j -= 1
        return ans