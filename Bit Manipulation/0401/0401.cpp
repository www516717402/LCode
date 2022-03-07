#include <numeric>
#include <iostream>
#include <vector>
#include <string>

int cal_bits(int inter)
{
    int c = 0;
    while (inter > 0)
    {
        inter &= inter - 1;
        c += 1;
    }
    return c;
}

std::vector<std::string> func(int data)
{
    std::vector<std::string> result;
    for (int h = 0; h < 12; h++)
        for (int m = 0; m < 60; m++)
            if (cal_bits(h) + cal_bits(m) == data)
            {
                std::string hour = std::to_string(h);
                std::string minute = m < 10 ? "0" + std::to_string(m) : std::to_string(m);
                result.emplace_back(hour+":"+minute);
            }
    return result;
}

int main(int argc, char **argv)
{
    int data = 1;
    std::vector<std::string> result = func(data);
    for(const auto &c:result)
        std::cout << c << std::endl;
    return 0;
}