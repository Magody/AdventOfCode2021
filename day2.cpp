#include <bits/stdc++.h>

using namespace std;


string day = "2";
string path = "/home/magody/programming/AdventOfCode2021/files/standard/input" + day + ".txt";

vector<string> splitStrings(string s, string delimiter)
{
    int textLength = s.length() + 1;

    size_t pos = 0;
    string token;
    vector<string> values;
    while ((pos = s.find(delimiter)) != std::string::npos)
    {
        token = s.substr(0, pos);
        values.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    token = s.substr(0, pos);
    values.push_back(token);

    return values;
}


int solve1() {
    cout << path << endl;
    ifstream MyReadFile(path);

    int horizontal = 0;
    int depth = 0;
    
    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        
        vector<string> res = splitStrings(holder_text, " ");

        string direction = res[0];
        int value = stoi(res[1]);
        if(direction == "forward"){
            horizontal += value;
        }
        else if(direction == "down"){
            depth += value;
        }
        else if(direction == "up"){
            depth -= value;
        }
    }
    

    MyReadFile.close(); 

    return horizontal * depth;
}


int solve2() {
    cout << path << endl;
    ifstream MyReadFile(path);

    int horizontal = 0;
    int depth = 0;
    int aim = 0;
    
    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        
        vector<string> res = splitStrings(holder_text, " ");

        string direction = res[0];
        int value = stoi(res[1]);
        if(direction == "forward"){
            horizontal += value;
            depth += aim * value;
        }
        else if(direction == "down"){
            aim += value;
        }
        else if(direction == "up"){
            aim -= value;
        }
    }
    

    MyReadFile.close(); 

    return horizontal * depth;
}

int main(){


    chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

   
    cout << solve2() << endl;

    chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    cout << "Time = " << chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;
    return 0;
}