#include <iostream>

bool func_231(int data)
{
    if (data < 1)
        return true;
    int r = 1;
    while (r <= data)
    {
        if (r == data)
            return true;
        r = r << 1;
    }
    return false;
}

int main(int argc, char **argv)
{
    int data = 4;
    std::cout << func_231(data) << std::endl;
    return 0;
}