class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            error = 0
            str_i = str(i)
            for j in range(len(str_i)):
                if int(str_i[j]) == 0:
                    error = 1
                    break
                elif i%int(str_i[j]) != 0:
                    error = 1
                    break
            if error == 0:
                ans.append(i)
        return ans