'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-06 00:52:11
FilePath: /vscode_cpp_for_Mac-master/Perfect_Number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import numpy as np

def main():
    n = 7
    base_matrix = np.array([[1, 1], [1, 0]])
    ans = base_matrix
    if n == 1 or n == 0:
        #print(n)
        return n
    else:
        exponent = n-1
        for i in range(exponent-1):
            ans = ans @ base_matrix
            print(ans)
        
    print(ans[0][0])
    return 0


if __name__ == "__main__":
    main()

