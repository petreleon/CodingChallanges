#include <stdio.h>
#include <cstring>
#include <iostream>
char arr[100], character;
int len, min_limit, max_limit;
int main(){
    int countPass = 0;
    FILE *input= fopen("input", "r");
    while (fscanf(input,"%d-%d %c: %s",&min_limit, &max_limit, &character, arr) != EOF)
    {
        min_limit--, max_limit --;
        len = strlen(arr);
        int count = 0;
        char* arrPointer = arr;
        /*for (count=0; arrPointer[count]; arrPointer[count]==character ? count++ : *arrPointer++);
        if( count >= min_limit && count <= max_limit){
            countPass ++;
        
        }*/
        if((arr[min_limit]==character) != (arr[max_limit]==character)){
            countPass++;
        }

    }
    std::cout<<countPass;
    
}