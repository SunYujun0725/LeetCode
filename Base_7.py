class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        if num < 0:
            ans += "-"
            num = abs(num)

        str_len = 1
        while num >= 7**str_len:
            str_len += 1

        for i in range(str_len-1, -1, -1):
            bit_num = 0
            while num >= bit_num*(7**i):
                bit_num += 1
                if bit_num-1 == 7:
                    break
            if bit_num-1 < 7:
                ans += str(bit_num-1)
                num -= (bit_num-1)*(7**i)
            bit_num = 0
        #print(ans)
        return ans
