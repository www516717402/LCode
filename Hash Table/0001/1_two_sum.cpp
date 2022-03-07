#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> twoSum_a(vector<int> &numbers, int target)
    {
        unordered_map<int, int> m;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++)
        {
            unordered_map<int, int>::const_iterator cur_find = m.find(numbers[i]);
            // not found the second one
            if (cur_find == m.end())
            {
                // store the first one position into the second one's key
                m[target - numbers[i]] = i + 1;
            }
            else
            {
                // found the second one
                result.push_back(cur_find->first);
                result.push_back(i + 1);
                return result;
            }
        }
        return result;
    }
};

int main(int argc, char **argv)
{
    Solution two_sum;
    vector<int> s_data = {1, 3, 5, 7, 8};
    vector<int> a = two_sum.twoSum_a(s_data, 15);
    std::cout << a[0] << a[1] << std::endl;
}