#include <iostream>
#include <vector>
using namespace std;
int main(){
    size_t eaten_carrots = 0;
    size_t carrotsCount;
    cin>>carrotsCount;
    vector<int> carrots(carrotsCount);
    for (size_t iterator = 0; iterator < carrots.size(); iterator++)
    {
        cin >> carrots[iterator];
    }
    int lastCarrot = 1;
    for (size_t iterator = 0; iterator < carrots.size() && carrots[iterator] >= lastCarrot; iterator++)
    {
        eaten_carrots ++;
        lastCarrot = carrots[iterator];
        carrots[iterator] = 0;
    }
    
    lastCarrot = 1;
    for (size_t iterator = carrots.size(); iterator > 0 && carrots[iterator -1] >= lastCarrot; iterator--)
    {
        eaten_carrots ++;
        lastCarrot = carrots[iterator - 1];
        carrots[iterator - 1] = 0;
    }
    cout<<eaten_carrots;
}
