class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        ans = ""
        if x >= 0:
            str_x = str(x)
        else:
            ans += "-"
            str_x = str(abs(x))

        reverse_x = str_x[::-1]
        for i in range(len(reverse_x)):
            if reverse_x[i] != "0":
                ans += reverse_x[i:]
                break
        if int(ans) <= -2**31 or int(ans) >= 2**31 - 1:
            return 0
        else:
            return int(ans)
        