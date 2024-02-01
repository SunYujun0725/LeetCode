class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while (len(str(ans)) >= 2):
            str_ans = str(ans)
            ans = 0
            for i in range(len(str_ans)):
                ans += int(str_ans[i])
        return ans