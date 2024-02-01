class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reversed_a = a[::-1]
        reversed_b = b[::-1]
        ans = ""
        len_a = len(a)
        len_b = len(b)
        i = 0
        carry_in = 0
        if len_a >= len_b:
            while(i < len_b):
                if (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 3):
                    ans = ans + "1"
                    carry_in = 1
                elif (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 2):
                    ans = ans + "0"
                    carry_in = 1
                elif (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 1):
                    ans = ans + "1"
                    carry_in = 0
                else:
                    ans = ans + "0"
                    carry_in = 0
                i += 1

            while (i < len_a):
                if (int(reversed_a[i]) + carry_in == 2):
                    ans = ans + "0"
                    carry_in = 1
                elif(int(reversed_a[i]) + carry_in == 1):
                    ans = ans + "1"
                    carry_in = 0
                else:
                    ans = ans + "0"
                    carry_in = 0
                i += 1

            if carry_in ==  1:
                ans = ans + "1"
                carry_in = 0

        else:
            while(i < len_a):
                if (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 3):
                    ans = ans + "1"
                    carry_in = 1
                elif (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 2):
                    ans = ans + "0"
                    carry_in = 1
                elif (int(reversed_a[i]) + int(reversed_b[i]) + carry_in == 1):
                    ans = ans + "1"
                    carry_in = 0
                else:
                    ans = ans + "0"
                    carry_in = 0
                i += 1

            while (i < len_b):
                if (int(reversed_b[i]) + carry_in == 2):
                    ans = ans + "0"
                    carry_in = 1
                elif(int(reversed_b[i]) + carry_in == 1):
                    ans = ans + "1"
                    carry_in = 0
                else:
                    ans = ans + "0"
                    carry_in = 0
                i += 1

            if carry_in ==  1:
                ans = ans + "1"
                carry_in = 0
        ans = ans[::-1]
        return ans
        