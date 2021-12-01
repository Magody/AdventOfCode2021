#include <bits/stdc++.h>

using namespace std;


string day = "1";
string path = "/home/magody/programming/AdventOfCode2021/day" + day + "/input.txt";



int getValue(ifstream &MyReadFile){
    string holder_text;
    if(!getline (MyReadFile, holder_text)){
        return -1;
    }
    return stoi(holder_text);
}

int solve() {
    cout << path << endl;
    ifstream MyReadFile(path);

    int length = 2000;
    int expected = length - 2;
    vector<int> sums(expected, 0);
    int first = getValue(MyReadFile);
    int second = getValue(MyReadFile);
    sums[0] = first + second;
    sums[1] = second;

    int answer = 0;

    int value = 1;

    int counter = 1;
    int index = 0;

    while(value != -1 && index < expected){

        value = getValue(MyReadFile);

        sums[index] += value;

        if(index+1 < expected){
            sums[index+1] += value;
        }

        if(index+2 < expected){
            sums[index+2] += value;
        }

        cout << "";
        index++;
    }

    for (size_t i = 1; i < sums.size(); i++)
    {
        if(sums[i] > sums[i-1]){
            answer++;
        }
    }
    

    MyReadFile.close(); 

    return answer;
}

int main(){


    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

   
    cout << solve() << endl;

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    return 0;
}