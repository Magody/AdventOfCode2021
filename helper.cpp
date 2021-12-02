#include <bits/stdc++.h>

using namespace std;

int main()
{
    string holder_text;
    ifstream MyReadFile("/home/magody/programming/AdventOfCode/input.txt");
    ofstream MyFile("/home/magody/programming/AdventOfCode/output.txt");


    while (getline (MyReadFile, holder_text)) {
        // input += holder_text + "\n";
        replace(holder_text.begin(), holder_text.end(), '[', '{');
        replace(holder_text.begin(), holder_text.end(), ']', '}');
        replace(holder_text.begin(), holder_text.end(), '=', ' ');
        MyFile << "vector<vector<int>> " + holder_text + ";\n";
    }



    MyReadFile.close(); 
    MyFile.close();
    return 0;
}