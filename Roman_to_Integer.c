/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-01-31 14:18:58
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-01-31 14:19:12
 * @FilePath: /vscode_cpp_for_Mac-master/Roman_to_Integer.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
int romanToInt(char* s) {
    int len = strlen(s);
    int sum = 0;
    for (int i = 0; i < len; i++) {
        printf("%d\n", i);
        if (s[i] == 'I') {
            if (s[i + 1] == 'V') {
                sum += 4;
                i += 1;
            } else if (s[i + 1] == 'X') {
                sum += 9;
                i += 1;
            } else {
                sum += 1;
            }
        } else if (s[i] == 'V') {
            sum += 5;
        } else if (s[i] == 'X') {
            if (s[i + 1] == 'L') {
                sum += 40;
                i += 1;
            } else if (s[i + 1] == 'C') {
                sum += 90;
                i += 1;
            } else {
                sum += 10;
            }
        } else if (s[i] == 'L') {
            sum += 50;
        } else if (s[i] == 'C') {
            if (s[i + 1] == 'D') {
                sum += 400;
                i += 1;
            } else if (s[i + 1] == 'M') {
                sum += 900;
                i += 1;
            } else {
                sum += 100;
            }
        } else if (s[i] == 'D') {
            sum += 500;
        } else if (s[i] == 'M') {
            sum += 1000;
        }
    }
    return sum;
}