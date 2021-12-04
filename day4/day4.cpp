#include <bits/stdc++.h>
#include "/home/magody/programming/AdventOfCode2021/utils.h"

using namespace std;

string day = "4";
string path_base = "/home/magody/programming/AdventOfCode2021/";
string path = path_base + "day" + day + "/input" + day + ".txt";

typedef unsigned long long longest;


void mark(vector<vector<int>>& matrix, int number){

    for(int i=0;i<matrix.size();i++){
        for(int j=0;j<matrix[0].size();j++){
            if(matrix[i][j] == number){
                matrix[i][j] = -1;
            }
        }
    }
}

int checkWin(vector<vector<vector<int>>> matrices){

    int winer = -1;
    for(int k=0;k<matrices.size();k++){
        vector<vector<int>> matrix = matrices[k];

        for(int i=0;i<matrix.size();i++){
            int counter = 0;
            for(int j=0;j<matrix[0].size();j++){
                int value = matrix[i][j];
                if(value == -1){
                    counter++;
                }
            }
            if(counter == matrix[0].size()){
                winer = k;
                return winer;
            }
        }

        for(int i=0;i<matrix[0].size();i++){
            int counter = 0;
            for(int j=0;j<matrix.size();j++){
                int value = matrix[j][i];
                if(value == -1){
                    counter++;
                }
            }
            if(counter == matrix.size()){
                winer = k;
                return winer;
            }
        }

        

    }


    return -1;
}

int solve1(vector<vector<vector<int>>> matrices ){

    vector<int> numbers = {7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1};


    int answer = 0;

    for(auto number: numbers){

        for(int i=0;i<matrices.size();i++){
            mark(matrices[i], number);
            printMatrix<int>(matrices[i]);
            cout << endl;
        }

        int index = checkWin(matrices);
        if(index >= 0){
            vector<vector<int>> matrix = matrices[index];
            int sum = 0;
            for(int i=0;i<matrix.size();i++){
                for(int j=0;j<matrix[0].size();j++){
                    int value = matrix[i][j];
                    if(value != -1){
                        sum += matrix[i][j];
                    }
                }
            }
            answer = sum;
            return sum * number;
        }

    }

    return answer;

}


vector<int> checkWin2(vector<vector<vector<int>>> matrices){

    vector<int> winners;

    for(int k=0;k<matrices.size();k++){
        vector<vector<int>> matrix = matrices[k];
        bool added = false;
        for(int i=0;i<matrix.size();i++){
            int counter = 0;
            for(int j=0;j<matrix[0].size();j++){
                int value = matrix[i][j];
                if(value == -1){
                    counter++;
                }
            }
            if(counter == matrix[0].size()){
                winners.push_back(k);
                added = true;
            }
        }

        if(added) continue;

        for(int i=0;i<matrix[0].size();i++){
            int counter = 0;
            for(int j=0;j<matrix.size();j++){
                int value = matrix[j][i];
                if(value == -1){
                    counter++;
                }
            }
            if(counter == matrix.size()){
                winners.push_back(k);
            }
        }

        

    }


    return winners;
}

int solve2(vector<vector<vector<int>>> matrices ){

    int mat = matrices.size();

    vector<int> numbers = {0,56,39,4,52,7,73,57,65,13,3,72,69,96,18,9,49,83,24,31,12,64,29,21,80,71,66,95,2,62,68,46,11,33,74,88,17,15,5,6,98,30,51,78,76,75,28,53,87,48,20,22,55,86,82,90,47,19,25,1,27,60,94,38,97,58,70,10,43,40,89,26,34,32,23,45,50,91,61,44,35,85,63,16,99,92,8,36,81,84,79,37,93,67,59,54,41,77,42,14};


    int answer = 0;

    int counter_win = 0;

    int last_win = 0;

    for(auto number: numbers){

        for(int i=0;i<matrices.size();i++){
            mark(matrices[i], number);
            // printMatrix<int>(matrices[i]);
            // cout << endl;
        }

        vector<int> indexes = checkWin2(matrices);

        if(indexes.size() > 0){
            counter_win+=indexes.size();

            for(auto index: indexes){
                vector<vector<int>> matrix = matrices[index];

                if(counter_win == mat){
                    
                    int sum = 0;
                    for(int i=0;i<matrix.size();i++){
                        for(int j=0;j<matrix[0].size();j++){
                            int value = matrix[i][j];
                            if(value != -1){
                                sum += matrix[i][j];
                            }
                        }
                    }
                    answer = sum;
                    return sum * number;
                }
                else{

                    int sum = 0;
                    for(int i=0;i<matrix.size();i++){
                        for(int j=0;j<matrix[0].size();j++){
                            int value = matrix[i][j];
                            if(value != -1){
                                sum += matrix[i][j];
                            }
                        }
                    }
                    last_win = sum * number;


                    for(int i=0;i<matrix.size();i++){
                        for(int j=0;j<matrix[0].size();j++){
                            matrices[index][i][j] = 200;
                        }
                    }
                }
            }


            

            
        }

    }

    return last_win;

}

int main(){
    vector<vector<vector<int>>> matrices = getMatricesIntFromTxt(path, true);
    cout << solve2(matrices) << endl;

    return 0;
}