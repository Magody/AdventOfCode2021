#include <bits/stdc++.h>
#include "/home/magody/programming/AdventOfCode2021/utils.h"

using namespace std;

string day = "5";
string path = "/home/magody/programming/AdventOfCode2021/files/standard/input" + day + ".txt";

typedef unsigned long long longest;


/*
for(int i=0;i<matrix.size();i++){
    for(int j=0;j<matrix[0].size();j++){
        
    }
}
*/
int solve1(vector<string> array){
    int array_len = array.size();
    int answer = 0;

    vector<vector<int>> matrix(1000, vector<int>(1000, 0));

    for(auto line:array){
        vector<string> s = splitStrings(line, " -> ");
        vector<string> p1 = splitStrings(s[0], ",");
        vector<string> p2 = splitStrings(s[1], ",");
        int x1 = stoi(p1[0]);
        int y1 = stoi(p1[1]);
        int x2 = stoi(p2[0]);
        int y2 = stoi(p2[1]);

        if(x1 == x2){
            //vertical
            int j = x1;
            int a = min(y1,y2);
            int b = max(y1,y2);

            for(int i=a;i<=b;i++){
                matrix[i][j] += 1;
            }
        }
        else if(y1 == y2){
            //horizontal
            int i = y1;
            int a = min(x1,x2);
            int b = max(x1,x2);

            for(int j=a;j<=b;j++){
                matrix[i][j] += 1;
            }
        }


    }


    for(int i=0;i<matrix.size();i++){
        for(int j=0;j<matrix[0].size();j++){
            if(matrix[i][j] >= 2){
                answer++;
            }
        }
    }

    

    return answer;
}


int solve2(vector<string> array){
    int array_len = array.size();
    int answer = 0;

    vector<vector<int>> matrix(1000, vector<int>(1000, 0));

    for(auto line:array){
        vector<string> s = splitStrings(line, " -> ");
        vector<string> p1 = splitStrings(s[0], ",");
        vector<string> p2 = splitStrings(s[1], ",");
        int x1 = stoi(p1[0]);
        int y1 = stoi(p1[1]);
        int x2 = stoi(p2[0]);
        int y2 = stoi(p2[1]);

        if(x1 == x2){
            //vertical
            int j = x1;
            int a = min(y1,y2);
            int b = max(y1,y2);

            for(int i=a;i<=b;i++){
                matrix[i][j] += 1;
            }
        }
        else if(y1 == y2){
            //horizontal
            int i = y1;
            int a = min(x1,x2);
            int b = max(x1,x2);

            for(int j=a;j<=b;j++){
                matrix[i][j] += 1;
            }
        }
        else{
            // diagonal

            if(y1 < y2 && x1 < x2){
                // d-r
                int i = y1;
                int j = x1;
                while(i <= y2 && j <=x2){
                    matrix[i][j] += 1;
                    i++;
                    j++;
                }
            }
            else if(y2 < y1 && x2 < x1){

                int i = y2;
                int j = x2;
                while(i <= y1 && j <= x1){
                    matrix[i][j] += 1;
                    i++;
                    j++;
                }
            }
            else if(y1 < y2 && x1 > x2){
                // d-l
                int i = y1;
                int j = x1;
                while(i <= y2 && j >= x2){
                    matrix[i][j] += 1;
                    i++;
                    j--;
                }
            }
            else if(y2 < y1 && x2 > x1){
                // u-l
                int i = y2;
                int j = x2;
                while(i <= y1 && j >= x1){
                    matrix[i][j] += 1;
                    i++;
                    j--;
                }
            }

            


        }

        // cout << "(" << x1 << "," << y1 << ")" << endl;
        // cout << "(" << x2 << "," << y2 << ")" << endl;
        // printMatrix<int>(matrix);

        // cout << "\n";

        


    }

    printMatrix<int>(matrix);


    for(int i=0;i<matrix.size();i++){
        for(int j=0;j<matrix[0].size();j++){
            if(matrix[i][j] >= 2){
                answer++;
            }
        }
    }

    

    return answer;
}

int main(){
    vector<string> array = getArrayStringFromTxt(path);
    cout << solve2(array) << endl;

    return 0;
}