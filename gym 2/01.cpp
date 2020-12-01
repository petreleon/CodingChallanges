#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

long long power(long long element, long long exponent, long long modulo){
    if( exponent == 0 ){
        return 1;
    }
    if( element == 0 ){
        return 0;
    }
    else {
        long long result = 1;
        while (exponent --){
            result *= element;
            result = result % modulo;
        }
        return result;
    }
}

int main(){
    //
    long long elementsCount, commandCount, command, inferior_limit, superior_limit, constant, modulo;
    cin >> elementsCount >> modulo;
    vector<long long> elements(elementsCount);
    for(auto &element:elements ){
        cin>>element;
    }
    cin >> commandCount;
    long long sum_, product_;
    while (commandCount--){
        cin >> command >> inferior_limit >> superior_limit >> constant;
        switch (command)
        {
        case 1:
            for (size_t iterator = inferior_limit - 1; iterator < superior_limit; iterator++)
            {
                elements[iterator] += constant % modulo;
                elements[iterator] = elements[iterator] % modulo;
            }
            
            break;
        
        case 2:
            for (size_t iterator = inferior_limit - 1; iterator < superior_limit; iterator++)
            {
                elements[iterator] *= constant % modulo;
                
                elements[iterator] = elements[iterator] % modulo;
            }
            
            break;
        
        case 3:
            for (size_t iterator = inferior_limit - 1; iterator < superior_limit; iterator++)
            {
                elements[iterator] =  power(elements[iterator], constant % modulo, modulo);
                elements[iterator] = elements[iterator] % modulo;
            }
            
            break;
        
        case 4:
            sum_ = 0;
            for (size_t iterator = inferior_limit - 1; iterator < superior_limit; iterator++)
            {
                sum_ += power(elements[iterator], constant % modulo, modulo);
                sum_ = sum_ % modulo;
            } 
            cout << sum_ << endl;
            break;
        
        case 5:
            product_ = 1;
            for (size_t iterator = inferior_limit - 1; iterator < superior_limit; iterator++)
            {
                product_ *= elements[iterator] % modulo;
                product_ = product_ % modulo;
            }
            cout << product_ << endl; 
            break;
        }
    }
}