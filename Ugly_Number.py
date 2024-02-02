class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n = n // 2

        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if (i==2 or i==3 or i==5):
                    factors.append(i)
                    n = n // i
                else:
                    return False

        if n > 2:
            if (n==2 or n==3 or n==5):
                factors.append(n)
            else:
                return False
        
        return True
