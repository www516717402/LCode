#include <iostream>
#include <vector>

class Solution
{
public:
    int singleNumber(std::vector<int> &nums)
    {
        int a = 0;
        int b = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int ta = a;
            a = (a & (~b) & (~nums[i])) | (~a & b & nums[i]);
            b = ~ta & (b ^ nums[i]);
        }
        return b;
    }
};

int main(int argc, char **argv)
{
    Solution ss;
    std::vector<int> data = {1, 2, 1, 1, 2, 2, 3};
    std::cout << ss.singleNumber(data) << std::endl;
}