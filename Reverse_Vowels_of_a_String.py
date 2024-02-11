'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-01 19:48:33
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-11 21:21:30
FilePath: /vscode_cpp_for_Mac-master/Counting_Bits.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def main():
    s = "aA"
    vowel = ""
    location = []
    ans = ""
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
            vowel += s[i]
            location.append(i)
    vowel = vowel[::-1]
    if len(location) == 0:
            return s
    j = 0
    for i in range(len(s)):
        if i == location[j]:
            ans += vowel[j]
            if j < len(location)-1:
                 j += 1
        else:
            ans += s[i]

    print(ans)
    return 0


if __name__ == "__main__":
    main()