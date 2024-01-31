/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-01-31 14:23:07
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-01-31 14:23:23
 * @FilePath: /vscode_cpp_for_Mac-master/Valid_Parentheses.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
bool isValid(char* s) {
    int len = strlen(s);
    if (len % 2 != 0) {
        return false;
    }
    char ss[len + 1];
    for (int i = 0; i < len; i++) {
        ss[i] = s[i];
    }
    ss[len] = '\0';
    int c = 0;
    for (int k = 0; (k < len / 2); k++) {
        c = 0;
        for (int i = 0; i < len - 1; i++) {
            if (s[i] == '(') {
                for (int j = i + 1; j < len; j++) {
                    if (ss[j] == '0') {
                    } else if (ss[j] == ')') {
                        ss[i] = '0';
                        ss[j] = '0';
                        c = 1;
                        break;
                    } else {
                        break;
                    }
                }
            }
            if (s[i] == '[') {
                for (int j = i + 1; j < len; j++) {
                    if (ss[j] == '0') {
                    } else if (ss[j] == ']') {
                        ss[i] = '0';
                        ss[j] = '0';
                        c = 1;
                        break;
                    } else {
                        break;
                    }
                }
            }
            if (s[i] == '{') {
                for (int j = i + 1; j < len; j++) {
                    if (ss[j] == '0') {
                    } else if (ss[j] == '}') {
                        ss[i] = '0';
                        ss[j] = '0';
                        c = 1;
                        break;
                    } else {
                        break;
                    }
                }
            }
            if (c == 1) {
                break;
            }
        }
        // printf("%s\n", ss);
    }
    for (int i = 0; i < len; i++) {
        if (ss[i] != '0') {
            return false;
        }
    }
    return true;
}