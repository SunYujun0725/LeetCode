'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2025-02-11 21:54:49
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2025-02-12 12:33:29
FilePath: /vscode_cpp_for_Mac-master/single_number.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
3 steps:
1. 計算正確答案：
    依照 先乘除後加減，從左到右計算，得到正確的答案。
    模擬錯誤運算順序的可能答案：
2. 使用 動態規劃 (DP) 來生成所有可能的結果。
    由於數字是單位數 (0-9)，我們可以用 dp[i][j] 來表示從 s[i:j+1] 這段區間內可能得到的計算結果。
3. 計算總分：
    如果答案正確，給 5 分。
    如果答案是錯誤的但在 可能的錯誤答案集合 內，給 2 分。
    否則給 0 分。
"""
def scoreOfStudents(s, answers):
    """
    :type s: str
    :type answers: List[int]
    :rtype: int
    """
    from itertools import product

    # 計算正確答案
    def evaluate_correct(s):
        stack = []
        num = 0
        op = "+"
        for c in s + "+":  # 加入一個 '+' 來確保最後一個數字被處理
            if c.isdigit():
                num = int(c)
            else:
                if op == "+":
                    stack.append(num)
                elif op == "*":
                    stack[-1] *= num
                op = c
                num = 0
        return sum(stack)

    correct_answer = evaluate_correct(s)

    # 計算所有可能的錯誤運算結果（使用 DP）
    n = len(s)
    dp = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(0, n, 2):  # 只考慮數字部分
        dp[i][i].add(int(s[i]))

    for length in range(3, n + 1, 2):  # 每次擴展長度為奇數 (數字+運算子+數字)
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):  # 遍歷所有可能的運算子
                left, right = dp[i][k - 1], dp[k + 1][j]
                for l, r in product(left, right):
                    if s[k] == "+":
                        if l + r <= 1000:
                            dp[i][j].add(l + r)
                    elif s[k] == "*":
                        if l * r <= 1000:
                            dp[i][j].add(l * r)

    valid_answers = dp[0][n - 1]  # 學生可能的錯誤計算結果

    # 計算得分
    total_score = 0
    for ans in answers:
        if ans == correct_answer:
            total_score += 5
        elif ans in valid_answers:
            total_score += 2

    return total_score

def main():
    print(scoreOfStudents("2+5*3", [17, 0, 10, 17, 17, 21, 26, 17, 17, 17])) # 2+5*3=13
    return 0 

if __name__ == "__main__":
    main()