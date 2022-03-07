#include <iostream>
#include <vector>

using namespace std;

class Solution
{
private:
    /* data */
public:
    int func_136(vector<int> &data)
    {
        int r = 0;
        for (auto d : data)
        {
            r ^= d;
        }
        return r;
    }
    int func_136a(vector<int>& data){
        
        return 0;
    }
    Solution(/* args */);
    ~Solution();
};

Solution::Solution(/* args */)
{
}

Solution::~Solution()
{
}

int main(int argc, char **argv)
{
    vector<int> data = {1, 4, 1, 5, 5, 4, 10, 9990, 10};
    Solution ss;
    cout << ss.func_136(data) << endl;
}