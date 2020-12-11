#include<algorithm>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
ifstream fin("sortare_divizori.in");
ofstream fout("sortare_divizori.out");

void read(int& iterated){
    fin>>iterated;
}
struct number {
    int nr, nrFactori;
};


vector<number> numbers;
bool compare(const number& number1, const number& number2){
    if (number1.nrFactori-number2.nrFactori) {
        return number1.nrFactori > number2.nrFactori;
    }
    return number1.nr < number2.nr;
}

void putToNumbers(int iterated){
    int number = iterated;
    int initVariant = 1;
    int step = 2;
    while(iterated >= step){
        if(step*step>iterated){
            initVariant *= 2;
            break;
        }
        if(iterated % step == 0){
            int divisionCount = 1;
            while(iterated % step == 0){
                divisionCount++;
                iterated = iterated / step;
            }
            initVariant *= divisionCount;
        }
        step++;
    }
    numbers.push_back({number, initVariant});
}
int main(){
    int count;
    fin>>count;
    vector<int> integers(count);
    for_each(integers.begin(), integers.end(), read);
    for_each(integers.begin(), integers.end(), putToNumbers);
    
    sort(numbers.begin(), numbers.end(), compare);
    for (auto number:numbers){
        fout << number.nr << ' ';
    }

}