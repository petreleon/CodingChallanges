#include<iostream>
#include<fstream>
#include<string>
#include<list>
#include<regex>
#include<deque>
#include<set>
#include<sstream>
#include<algorithm>

void print_forward(std::deque<int> const& deque_)
{
    for (auto it = deque_.cbegin(); it != deque_.cend(); ++it)
        std::cout << *it <<  ' ';
    std::cout << '\n';
}
 

using namespace std;
#define First 0
#define Second 1
ifstream input("input");
list<deque<int>> list_;
set<pair<deque<int>, deque<int>>> set_deep_10;
pair<int, deque<int>> recursivePlaying(deque<int> first, deque<int> second, int deep){
    int winner = First;
    cout << *max_element(first.begin(), first.end()) << " "<< *max_element(second.begin(), second.end())<<endl;
    if( *max_element(first.begin(), first.end()) > *max_element(second.begin(), second.end()) and deep >0)
        return pair<int, deque<int>>(First, first);
    set<pair<deque<int>, deque<int>>> set_;
    while(first.size() > 0 and second.size() > 0){
        pair<deque<int>, deque<int>> pair_(first, second);
        if (set_.find(pair_) != set_.end()){
            return pair<int, deque<int>>(First, first);
        }
        int value_from_first = first.front();
        first.pop_front();
        int value_from_second = second.front();
        second.pop_front();

        set_.insert(pair_);
        if (value_from_first <= first.size() and value_from_second <= second.size()){
            winner = recursivePlaying(deque<int>(first.begin(), first.begin() + value_from_first), deque<int>(second.begin(), second.begin() + value_from_second), deep + 1).first;
        }
        else {
            if(value_from_first > value_from_second){
                winner = First;
            }
            if(value_from_first < value_from_second){
                winner = Second;
            }
        }
        if(winner == First){
            first.push_back(value_from_first);
            first.push_back(value_from_second);
        }
        if(winner == Second){
            second.push_back(value_from_second);
            second.push_back(value_from_first);
        }
        // cout << "Deep " << deep << endl;
        // cout << "First " ; print_forward(first);
        // cout << "Second " ; print_forward(second);

    }

    if(first.size() > 0){
        return pair<int, deque<int>>(First, first);
    }
    if(second.size() > 0){
        return pair<int, deque<int>>(Second, second);
    }
}

int main(){
    string string_;
    while (getline(input,string_))
    {
        if(string_.length()>0){
            if(regex_match(string_, regex("(Player)(.*)"))){
                list_.push_back(deque<int>());
            }
            else {
                list_.back().push_back(stoi(string_));
            }
        }
    }
    deque<int> winnerDeque = recursivePlaying(list_.front(), list_.back(), 0).second;
    int sum_ = 0;
    while (winnerDeque.size())
    {
        sum_ += winnerDeque.front() * winnerDeque.size();
        winnerDeque.pop_front();
    }
    cout << sum_ << endl;
    if (sum_ <= 30976){
        cout<< "Too low"<<endl;
    } 
    return 0;
}
