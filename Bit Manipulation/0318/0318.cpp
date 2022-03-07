#include <iostream>
#include <vector>

int func318(std::vector<std::string>& words)
{
    if(words.size()<2)
        return 0;
    int max_length = 0;
    std::vector<int> encode_int(words.size(),0);
    for(int i=0; i<words.size(); i++)
    {
        for (const auto& c : words[i]) {
                encode_int[i] |= (1 << (c - 'a'));
            }
    }
    for(int i=0; i<words.size(); i++)
    {
        for(int j=i+1; j<words.size(); j++)
        {
            if((encode_int[i] & encode_int[j])==1)
                continue;
            if(words[i].length()*words[j].length()>max_length)
                max_length = words[i].length() * words[j].length();
        }
    }
    return max_length;
}

int main(int arc, char **argv)
{
    std::vector<std::string> data{"a","uy","re","spd"};
    std::cout << func318(data) << std::endl;
    return 0;
}