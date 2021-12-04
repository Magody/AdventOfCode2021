#include <bits/stdc++.h>
#include "/home/magody/programming/AdventOfCode2021/utils.h"

using namespace std;


int main(){

    
    string str = "shiny all bags contain 1 dotted lime bag, 2 clear gold bags.";
    regex r("([A-z\\s]+) bags contain ([0-9]+) ([A-z\\s]+), ([0-9]+) ([A-z\\s]+).");

    smatch m;
    regex_match (str, m, r);


    cout << m.size() << endl;
    for(auto v:m){
        cout << v << endl;
    }

    return 0;
}