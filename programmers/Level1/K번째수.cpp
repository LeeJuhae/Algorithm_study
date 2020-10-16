#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> slice(vector<int> v, int s, int e) {
    vector<int>::iterator first = v.begin() + s;
    vector<int>::iterator last = v.begin() + e + 1;
    return vector<int>(first, last);
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (vector<int> arr : commands) {
        vector<int> temp = slice(array, arr[0]-1, arr[1]-1);
        sort(temp.begin(), temp.end());
        answer.push_back(temp[arr[2]-1]);
    }
    return answer;
}
