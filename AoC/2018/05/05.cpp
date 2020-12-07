#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
#include <deque>

using namespace std;

bool checkReaction(char first, char second){
    if (first != second and toupper(first) == toupper(second)){
        return true;
    }
    return false;
}

int checkResult(string string1){
    string string2;
    string2 = string1;
    string1 = "";
    deque<char> deque1;
    for (unsigned i = 0; i < string2.length(); i++){
        if (deque1.size()){
            if(checkReaction(deque1.back(), string2[i])){
                deque1.pop_back();
            }
            else {
                deque1.push_back(string2[i]);
            }
        }
        else {
            deque1.push_back(string2[i]);
        }
    }
    while(deque1.size()){
        string1 += deque1.front();
        deque1.pop_front();
    }
    // cout<< string1 << endl;
    // 5279 too high
    return string1.length();
}


int main(){
    set<char> chrSet;
    ifstream input("input.txt");
    string string1;
    input >> string1;
    int min_ = string1.length();
    for (char chr : string1){
        chrSet.insert(toupper(chr));
    }
    for (char chr : chrSet){
        string string2 = string1;
        string2.erase(std::remove(string2.begin(), string2.end(), chr), string2.end());
        string2.erase(std::remove(string2.begin(), string2.end(), tolower(chr)), string2.end());
        min_ = min(min_, checkResult(string2));
    }

    cout << min_ << endl;
    //cout << checkResult(string1) << endl;
    return 0;
}
