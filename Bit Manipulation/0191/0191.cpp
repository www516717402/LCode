#include <iostream>

class Solution
{
private:
    /* data */
public:
    int func_191(int data, int bits=4);
    Solution(/* args */);
    ~Solution();
};

Solution::Solution(/* args */)
{
}

Solution::~Solution()
{
}

int Solution::func_191(int data, int bits)
{
    int result = 0;
    int mask = 1;
    for(int i=0; i<32; i++){
        if ((mask & data) != 0)
            result += 1; // / mask;
        mask = mask << 1;
    }
    return result;
}

int main(int argc, char** argv){
    int data = 11;
    Solution ss;
    std::cout << ss.func_191(data) << std::endl;    
    return 0;
}