#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    size_t elementsCount;
    cin >> elementsCount;
    vector<size_t> elements(elementsCount);
    for (size_t iterator = 0; iterator < elementsCount; iterator++)
    {
        cin >> elements[iterator];
    }
    sort(elements.begin(), elements.end());
    size_t idealArray = elements[elementsCount / 2];
    long long sumOfEffort = 0;
    for (size_t iterator = 0; iterator < elementsCount; iterator++)
    {
        sumOfEffort += abs((long)elements[iterator] - (long)idealArray);
    }
    cout << sumOfEffort;
    return 0;
}
