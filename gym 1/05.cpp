#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
    string string_,substring; // string_ is string to search, substring is the substring to search for
    size_t stringSize;
    cin >> stringSize;
    cin >> string_>>substring;
    size_t substringSize = substring.length();
    size_t string_Size = string_.length();
    
    vector<long long> positions; // holds all the positions that substring occurs within string_
    long long count = 0;
    size_t positon = string_.find(substring, 0);
    while(positon != string::npos)
    {
        positions.push_back(positon);
        positon = string_.find(substring,positon+1);
    }
    positions.insert(positions.begin(),-1);
    for (size_t iterator = 1; iterator < positions.size(); iterator++)
    {
        size_t first_countable_position = positions[iterator - 1] + 1;
        size_t first_distance = positions[iterator] - first_countable_position ;
        size_t last_char_position = positions[iterator] + substringSize;
        size_t last_distance = string_Size - last_char_position;
        count += (first_distance+1)*(last_distance+1);
    }
    cout << count;
    return 0;
}
