#include <iostream>

int func_201(int a, int b)
{
    int bit_shift = 0;
    while (a < b)
    {
        a = a >> 1;
        b = b >> 1;
        bit_shift += 1;
    }
    return a << bit_shift;
}

int main(int argc, char **argv)
{
    std::cout << func_201(9, 10) << std::endl;
    return 0;
}