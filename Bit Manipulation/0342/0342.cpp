#include <stdio.h>
#include <iostream>

bool func_342(int data)
{
    return data > 0 && (data & (data - 1)) == 0 &&
               ((data & 0b01010101010101010101010101010101) == data);
}

int main(int argc, char **argcv)
{
    int data = 4;
    bool result = func_342(data);
    std::cout<<result<<std::endl;
    //printf("%d",result);
    return 0;
}