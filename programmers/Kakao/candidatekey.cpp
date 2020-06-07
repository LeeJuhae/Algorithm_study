#include <string>
#include <vector>

using namespace std;

#include <iostream>
#include <algorithm>
#include <map>
#include <typeinfo>

vector<vector<int>> dfs(vector<bool> visit, vector<int>arr, int n, vector<vector<int>> re)
{
	if (n == visit.size())
	{
		vector<int> v;
		for (int i = 0 ; i < visit.size() ; i++)
		{
			if (visit[i])
				v.push_back(arr[i]);
		}
		if (!v.empty())
			re.push_back(v);
	}
	else
	{
		visit[n] = true;
		re = dfs(visit, arr, n+1,re);
		visit[n] = false;
		re = dfs(visit, arr, n+1, re);
	}
	return re;
}

vector<vector<int>> combination(int size)
{
	vector<bool> visit(size);
	vector<int> arr;
	vector<vector<int>> comb;

	for(int i = 0 ; i < size ; i++)
		arr.push_back(i);

	comb = dfs(visit, arr, 0, comb);
	return comb;
}

int solution(vector<vector<string>> relation) {
	int answer = 0;
	vector<vector<int>> comb;
	map<int, vector<vector<int>>> m;
	int	each_size = relation[0].size();

	comb = combination(relation[0].size());

	for (int i = 1 ; i <= each_size ; i++)
	{
		for(int j = 0 ; j < comb.size() ; j++)
		{
			if (comb[j].size() == i)
				m[i].push_back(comb[j]);

		}
	}

	map<int,vector<vector<int>>>::iterator iter;
	int col_cnt;
	bool can_be_candidate_key = true;

	for(iter=m.begin();iter!=m.end();iter++)
	{
		vector<vector<string>> tmp;
		col_cnt = iter->first;
		cout << "Key : " << iter->first << endl;
		for(int i = 0 ; i < m[col_cnt].size() ; i++)
		{
			can_be_candidate_key = true;
			tmp.clear();
			for(int j = 0 ; j < m[col_cnt][i].size() ; j++)
			{
				for (int k = 0 ; k < relation.size() ; k++)
				{
					vector<string> t;
					string s = relation[k][m[col_cnt][i][j]];
					// cout << "i, j, k, s :" + to_string(i) + " " + to_string(j) + " " + to_string(k) + " " + s << endl;
					if (j != 0)
					{
						t = tmp[k];
					}
					t.push_back(s);
					// cout << "t size : "+to_string(t.size()) + ", col_cnt : " + to_string(col_cnt) << endl;
					if (find(tmp.begin(), tmp.end(), t) != tmp.end() && t.size() == col_cnt)
					{
						// cout << endl << "here" << endl;
						can_be_candidate_key = false;
					}
					else
					{
						if (j != 0)
							tmp[k] = t;
						else
							tmp.push_back(t);

						// cout << "k : " + to_string(k) << endl;
						// for (int a = 0; a < tmp[k].size() ; a++)
						// 	cout << tmp[k][a] + " ";
						// cout << endl;
					}
				}
			}
			if (can_be_candidate_key)
			{
				// for (int k = 0 ; k < relation.size() ; k++)
				// {
				// 	for (int a = 0; a < tmp[k].size() ; a++)
				// 		cout << tmp[k][a] + " ";
				// 	cout << endl;
				// }
				answer++;
			}
		}
	}
    return answer;
}

int main(){
	vector<vector<string>> relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","1"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
	// vector<vector<string>> relation = {{"a","m","2"}, {"b","u","3"}, {"a","m","6"}};
	cout << solution(relation);
}
