#include <bits/stdc++.h>
#include "/home/magody/programming/AdventOfCode2021/utils.h"

using namespace std;

string day = "3";
string path = "/home/magody/programming/AdventOfCode2021/files/standard/input" + day + ".txt";


int solve1(vector<string> values) {

    int values_len = values.size();
    int length = values[0].size();

    string gamma_rate = "";
    string epsilon_rate = "";

    for(int i=0;i<length;i++){
        int ones = 0;
        int zeros = 0;
        for(int j=0;j<values_len;j++){

            if(values[j][i] == '0'){
                zeros++;
            }
            else{
                ones++;
            }
        }

        if(ones > zeros){
            // ones wins
            gamma_rate.append("1");
            epsilon_rate.append("0");
        }
        else{
            gamma_rate.append("0");
            epsilon_rate.append("1");
        }

    }

    int a = std::bitset<12>(gamma_rate).to_ulong();
    int b = std::bitset<12>(epsilon_rate).to_ulong();

    return a * b;
}


int solve2(vector<string> values) {

    int values_len = values.size();
    int length = values[0].size();

    string oxygen = "";
    string c02 = "";

    vector<string> values_new;

    for(int j=0;j<values_len;j++){
        values_new.push_back(values[j]);
    }

    for(int i=0;i<length && values_new.size() > 1;i++){
        values_len = values_new.size();
        int ones = 0;
        vector<int> positions_ones;
        int zeros = 0;
        vector<int> positions_zeros;
        for(int j=0;j<values_len;j++){

            if(values_new[j][i] == '0'){
                zeros++;
                positions_zeros.push_back(j);
            }
            else{
                positions_ones.push_back(j);
                ones++;
            }
        }

        vector<string> temp;

        if(ones >= zeros){

            // ones wins
            for(int j=0;j<positions_ones.size();j++){
                temp.push_back(values_new[positions_ones[j]]);
            }
        }
        else if(ones < zeros){
            // zeros wins
            for(int j=0;j<positions_zeros.size();j++){
                temp.push_back(values_new[positions_zeros[j]]);
            }
        }
        values_new = temp;


    }




    oxygen = values_new[0];

    vector<string> values_new2;

    for(int j=0;j<values.size();j++){
        values_new2.push_back(values[j]);
    }


    for(int i=0;i<length && values_new2.size() > 1;i++){
        values_len = values_new2.size();
        int ones = 0;
        vector<int> positions_ones;
        int zeros = 0;
        vector<int> positions_zeros;
        for(int j=0;j<values_len;j++){

            if(values_new2[j][i] == '0'){
                zeros++;
                positions_zeros.push_back(j);
            }
            else{
                positions_ones.push_back(j);
                ones++;
            }
        }

        vector<string> temp;

        if(ones < zeros){

            // ones wins
            for(int j=0;j<positions_ones.size();j++){
                temp.push_back(values_new2[positions_ones[j]]);
            }
        }
        else{
            // zeros wins
            for(int j=0;j<positions_zeros.size();j++){
                temp.push_back(values_new2[positions_zeros[j]]);
            }
        }
        values_new2 = temp;


    }

    c02 = values_new2[0];
    

    int a = std::bitset<12>(oxygen).to_ulong();
    int b = std::bitset<12>(c02).to_ulong();

    return a * b;
}


int main(){
    vector<string> values = getArrayStringFromTxt(path);
    cout << solve2(values) << endl;


    return 0;
}