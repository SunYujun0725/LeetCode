class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = num**0.5
        if ans.is_integer():
            return True
        else:
            return False