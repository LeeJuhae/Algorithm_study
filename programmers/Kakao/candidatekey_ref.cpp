// #include <bits/stdc++.h>
#include <stdio.h>
#include <vector>
#include <set>
#include <string>
// #include <iostream>

using namespace std;

bool possi(vector<int> &vec, int now)
{
	for (int i = 0; i < vec.size(); i++)
		if ((vec[i] & now) == vec[i])
			return false;
	return true;
}
int solution(vector<vector<string>> relation)
{
	vector<int> ans;
	int n = relation.size();
	int m = relation[0].size();

	for (int i = 1; i < (1 << m); i++)
	{
		set<string> s;
		for (int j = 0; j < n; j++)
		{
			string now = "";
			for (int k = 0; k < m; k++)
			{
				if (i & (1 << k))
					now += (relation[j][k] + " ");
			}
			s.insert(now);
		}
		if (s.size() == n && possi(ans, i))
			ans.push_back(i);
	}
	return ans.size();
}

// int main()
// {
// 	// vector<vector<string>> relation = {{"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"}, {"300", "tube", "computer", "3"}, {"400", "con", "computer", "1"}, {"500", "muzi", "music", "3"}, {"600", "apeach", "music", "2"}};
// 	// vector<vector<string>> relation = {{"a","1","4"}, {"2","1","5"}, {"a","2","4"}};
// 	vector<vector<string>> relation = {{"ab","c"}, {"a","bc"}, {"a","x"},{"x","c"}};
// 	// vector<vector<string>> relation = {{"a","b","c"}, {"1","b","c"}, {"a","b","4"},{"a","5","c"}};
// 	// vector<vector<string>> relation = {{"a","m","2"}, {"b","u","3"}, {"a","m","6"}};
// 	cout << solution(relation);
// 	// solution(relation);
// }
