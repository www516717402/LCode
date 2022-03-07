#include <stdio.h>

int func(int a, int b)
{
    while (b > 0)
    {
        int c = a ^ b;
        b = (a & b) << 1;
        a = c;
    }
    return a;
}

int main(int argc, char **argv)
{
    int a = 3, b = 11;
    int result = func(a, b);
    printf("%d", result);
    return 0;
}