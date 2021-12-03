#include <bits/stdc++.h>

using namespace std;

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


vector<string> getArrayStringFromTxt(string path){
    vector<string> array;
    ifstream MyReadFile(path);

    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        array.push_back(holder_text);
    }

    MyReadFile.close();
    return array;
}

vector<int> getArrayIntFromTxt(string path){
    vector<int> array;
    ifstream MyReadFile(path);

    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        array.push_back(stoi(holder_text));
    }

    MyReadFile.close();
    return array;
}

void deepCopyMatrix(int **fromMatrix, int **toMatrix, int n, int m){
     for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            toMatrix[i][j] = fromMatrix[i][j];

        }
    }
}

template <class T>
bool existValueInList(vector<T> my_list, T my_var)
{
    return (find(my_list.begin(), my_list.end(), my_var) != my_list.end());
}

template <class T>
void printVector(vector<T> v)
{
    for (size_t i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}

template <class T>
void printMatrix(vector<vector<T>> matrix)
{
    int n = matrix.size();
    int m = matrix[0].size();
    
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < m; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}