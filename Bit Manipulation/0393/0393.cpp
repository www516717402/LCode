#include <numeric>
#include <iostream>
#include <vector>

bool func(std::vector<int> data)
{
    int ct = 0;
    for (const auto d : data)
    {
        if (ct == 0)
            if ((d >> 5) == 6)
                ct = 1;
            else if ((d >> 4) == 14)
                ct = 2;
            else if ((d >> 3) == 30)
                ct = 3;
            else if ((d >> 7) == 1)
                return false;
            else
            {
                if ((d >> 6) != 2)
                    return false;
                ct -= 1;
            }
    }
}

int main(int argc, char **argv)
{
    std::vector<int> data{235, 140, 4};
    bool result = func(data);
    std::cout << result;
    return 0;
}