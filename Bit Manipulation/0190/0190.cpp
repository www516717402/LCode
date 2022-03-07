#include <iostream>
#include <cmath>

class Solution
{
private:
    /* data */
public:
    int func_0190(int data, int bits = 32);
    Solution(/* args */);
    ~Solution();
};

Solution::Solution(/* args */)
{
}

Solution::~Solution()
{
}
int Solution::func_0190(int data, int bits)
{
    int result = 0;
    for (int i = 0; i < bits; i++)
    {
        result += (data % 2) * pow(2, bits - 1 - i);
        data = data / 2;
        if (0 == data)
            break;
    }
    return result;
}

int main(int argc, char **argv)
{
    Solution ss;
    int data = 11;
    int bits = 4;
    std::cout << ss.func_0190(data, bits=bits) << std::endl;
    return 0;
}
