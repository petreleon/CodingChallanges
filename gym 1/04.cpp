#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main(){
    long long number, _sum;
    cin>>number>>_sum;
    string numberString = to_string(number);
    string _differnce = to_string(_sum - number);
    sort(numberString.begin(), numberString.end());
    sort(_differnce.begin(), _differnce.end());
    if (numberString == _differnce){
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}
