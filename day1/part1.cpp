#include <bits/stdc++.h>

using namespace std;


string day = "1";
string path = "/home/magody/programming/AdventOfCode2021/day" + day + "/input.txt";

int solve() {
    cout << path << endl;
    ifstream MyReadFile(path);

    int value_last = -1;
    int value;

    int answer = 0;
    
    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        value = stoi(holder_text);
        if(value_last == -1){
            value_last = value;
            continue;
        }

        if(value > value_last){
            answer++;
        }

        value_last = value;
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