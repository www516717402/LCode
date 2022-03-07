#include <numeric>
#include <iostream>

char func(std::string a, std::string b)
{
    return std::accumulate(a.begin(), a.end(), 0, std::bit_xor<int>()) ^ std::accumulate(b.begin(), b.end(), 0, std::bit_xor<int>());
}

int main(int argc, char **argv)
{
    std::string a = "cba", b = "gacb";
    char result = func(a, b);
    printf("%c", result);
    return 0;
}