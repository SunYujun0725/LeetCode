#include <stdio.h>
#include <limits.h>

// 計算最大公因數
unsigned long long gcd(unsigned long long a, unsigned long long b) {
    while (b != 0) {
        unsigned long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

unsigned long long calculate(long long start, long long end, long long less_steps) {
    if (start > end) {
        return 0;  // 输入无效，返回0
    }
    unsigned long long result = 1;
    unsigned long long count = 1;
    unsigned long long Remaining = 1;
    for (int i = start; i <= end; ++i) {
        result *= i;
        if (count <= less_steps){
            unsigned long long gcd_number = gcd(result, count);
            result /= gcd_number;
            Remaining *= (count / gcd_number);
            count += 1 ;
        }
    }
    result /= Remaining;
    return result;
}

int main() {
    long long n;
    scanf("%lld", &n);
    long long ans = 0;
    long long one_steps;
    long long total_number;

    long long most_two_steps = n / 2;
    for (long long i = most_two_steps; i >= 0; i--) {
        one_steps = n - (i * 2);
        //printf("%lld %lld\n", i, one_steps);
        total_number = i + one_steps;
        //printf("%lld + ", ans);
        // ans += (factorial(total_number)/(factorial(i)*factorial(one_steps)));
        // it will overflow, so you need to handle overflow
        if((i == 0) || (one_steps == 0)){
            //printf("1\n");
            ans += 1;
        }
        else if (i >= one_steps) {
            //printf("%lld\n", (calculate(i+1, total_number, one_steps)));
            ans += (calculate(i+1, total_number, one_steps));
        } 
        else {
            //printf("%lld\n",  (calculate(one_steps+1, total_number, i)));
            ans += (calculate(one_steps+1, total_number, i));
        }
        //printf("-----------\n");
    }

    printf("%lld\n", ans);
    return 0;
}