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

vector<string> getArrayStringFromTxtParsingBlankLines(string path){
    vector<string> array;
    ifstream MyReadFile(path);

    string holder_text;
    string whole = "";
    while (getline (MyReadFile, holder_text)) {

        if(holder_text == ""){
            array.push_back(whole);
            whole = "";
        }
        else{
            if(whole == ""){
                whole = holder_text;
            }
            else{
                whole += " " + holder_text;
            }
            
        }
    }

    if(whole != ""){
        array.push_back(whole);
    }

    MyReadFile.close();
    return array;
}

vector<vector<char>> getMatrixCharFromTxt(string path, bool exist_separation){
    vector<vector<char>> matrix;
    ifstream MyReadFile(path);

    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        vector<char> v;
        if(exist_separation){
            vector<string> s = splitStrings(holder_text, " ");
            for(auto c: s){
                v.push_back(c[0]);
            }
        }
        else{
            for(auto c: holder_text){
                v.push_back(c);
            }
        }

        matrix.push_back(v);
        
    }

    MyReadFile.close();
    return matrix;
}

vector<vector<int>> getMatrixIntFromTxt(string path, bool exist_separation){
    vector<vector<int>> matrix;
    ifstream MyReadFile(path);

    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        vector<int> v;
        if(exist_separation){
            vector<string> s = splitStrings(holder_text, " ");
            for(auto c: s){
                v.push_back(stoi(c));
            }
        }
        else{
            for(auto c: holder_text){
                v.push_back(c - '0');
            }
        }

        matrix.push_back(v);
        
    }

    MyReadFile.close();
    return matrix;
}


vector<vector<vector<int>>> getMatricesIntFromTxt(string path, bool exist_separation){
    vector<vector<vector<int>>> matrices;
    ifstream MyReadFile(path);

    vector<vector<int>> matrix;

    string holder_text;
    while (getline (MyReadFile, holder_text)) {

        if(holder_text == ""){
            matrices.push_back(matrix);
            matrix.clear();
            continue;
        }
        vector<int> v;
        if(exist_separation){
            vector<string> s = splitStrings(holder_text, " ");
            for(auto c: s){
                if(c == "" || c == " ") continue;
                v.push_back(stoi(c));
            }
        }
        else{
            for(auto c: holder_text){
                v.push_back(c - '0');
            }
        }

        if(v.size() > 0){
            matrix.push_back(v);
        }
        
    }

    if(matrix.size() > 0){
        matrices.push_back(matrix);
        matrix.clear();
    }

    MyReadFile.close();
    return matrices;
}


vector<vector<float>> getMatrixFloatFromTxt(string path, bool exist_separation){
    vector<vector<float>> matrix;
    ifstream MyReadFile(path);

    string holder_text;
    while (getline (MyReadFile, holder_text)) {
        vector<float> v;
        if(exist_separation){
            vector<string> s = splitStrings(holder_text, " ");
            for(auto c: s){
                v.push_back(stof(c));
            }
        }
        else{
            for(auto c: holder_text){
                v.push_back(c - '0');
            }
        }

        matrix.push_back(v);
        
    }

    MyReadFile.close();
    return matrix;
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



unordered_map<string,string> mapVectorKeyPair(vector<string> v){
    int v_len = v.size();
    unordered_map<string,string> m;

    for(auto kp:v){
        vector<string> s = splitStrings(kp, ":");
        m[s[0]] = s[1];
    } 

    return m;
}

smatch regexMatch(string str, string r){
    regex regex1 (r);
    smatch m;
    regex_match (str, m, regex1);
    return m;
}
    
bool hasFourDigits(string s){
    smatch m = regexMatch(s, "[0-9]{4}");
    return m.size() == 1;
}


template <class T>
bool isInRange(T value, T min, T max){
    return value >= min && value <= max;    
}
