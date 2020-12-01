#include <iostream>
#include <vector>
using namespace std;

int main(){
    int counter, size;
    cin >> counter;
    while(counter --){
        cin >> size;
        if (size % 2 == 1){
            cout << "Bob";
        }
        else if ((size / 2) % 2 == 0){
            cout << "Draw";
        }
        else {
            cout << "Alice";
        }
        cout << endl;
    }
    return 0;
}