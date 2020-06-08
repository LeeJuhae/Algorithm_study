#include <string>
#include <vector>
<<<<<<< HEAD
#include <map>
#include <algorithm>
// #include <iostream>

using namespace std;

=======

using namespace std;

#include <iostream>
#include <algorithm>
#include <map>
#include <typeinfo>

>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
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

<<<<<<< HEAD
map<int, vector<vector<int>>> setMap(int attr_cnt, vector<vector<int>> comb)
{
	map<int, vector<vector<int>>> attr_map;

	for (int i = 1 ; i <= attr_cnt ; i++)
=======
int solution(vector<vector<string>> relation) {
	int answer = 0;
	vector<vector<int>> comb;
	map<int, vector<vector<int>>> m;
	int	each_size = relation[0].size();

	comb = combination(relation[0].size());

	for (int i = 1 ; i <= each_size ; i++)
>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
	{
		for(int j = 0 ; j < comb.size() ; j++)
		{
			if (comb[j].size() == i)
<<<<<<< HEAD
				attr_map[i].push_back(comb[j]);
		}
	}
	return (attr_map);
}

int solution(vector<vector<string>> relation) {
	vector<vector<int>> attr_comb;
	map<int, vector<vector<int>>> attr_map;
	int answer = 0;
	int attr_cnt = relation[0].size();

	attr_comb = combination(relation[0].size());
	attr_map = setMap(attr_cnt, attr_comb);

	map<int,vector<vector<int>>>::iterator iter;
	vector<vector<int>> delete_list;
	int key;
	bool can_be_candidate_key = true;

	for(iter=attr_map.begin();iter!=attr_map.end();iter++)
	{
		vector<vector<string>> attr_value;
		key = iter->first;
		for(int i = 0 ; i < attr_map[key].size() ; i++)
		{
			can_be_candidate_key = true;
			attr_value.clear();
			for(int j = 0 ; j < attr_map[key][i].size() ; j++)
			{
				for (int k = 0 ; k < delete_list.size() ; k++)
				{
					for(int l = 0; l < delete_list[k].size() ; l++)
					{
						if (find(attr_map[key][i].begin(), attr_map[key][i].end(), delete_list[k][l]) != attr_map[key][i].end())
						{
							can_be_candidate_key = false;
						}
						else
						{
							can_be_candidate_key = true;
							break ;
						}
					}
					if (can_be_candidate_key == false)
						break ;
				}
				if (can_be_candidate_key == false)
					break ;
				for (int k = 0 ; k < relation.size() ; k++)
				{
					vector<string> tmp;
					string s = relation[k][attr_map[key][i][j]];

					if (j != 0)
						tmp = attr_value[k];
					tmp.push_back(s);
					if (find(attr_value.begin(), attr_value.end(), tmp) != attr_value.end() && tmp.size() == key)
					{
=======
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
>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
						can_be_candidate_key = false;
					}
					else
					{
						if (j != 0)
<<<<<<< HEAD
							attr_value[k] = tmp;
						else
							attr_value.push_back(tmp);
=======
							tmp[k] = t;
						else
							tmp.push_back(t);

						// cout << "k : " + to_string(k) << endl;
						// for (int a = 0; a < tmp[k].size() ; a++)
						// 	cout << tmp[k][a] + " ";
						// cout << endl;
>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
					}
				}
			}
			if (can_be_candidate_key)
			{
<<<<<<< HEAD
				answer++;
				delete_list.push_back(attr_map[key][i]);
=======
				// for (int k = 0 ; k < relation.size() ; k++)
				// {
				// 	for (int a = 0; a < tmp[k].size() ; a++)
				// 		cout << tmp[k][a] + " ";
				// 	cout << endl;
				// }
				answer++;
>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
			}
		}
	}
    return answer;
}

<<<<<<< HEAD
// int main(){
// 	vector<vector<string>> relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","1"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
// 	// vector<vector<string>> relation = {{"a","1","4"}, {"2","1","5"}, {"a","2","4"}};
// 	// vector<vector<string>> relation = {{"ab","c"}, {"a","bc"}, {"a","x"},{"x","c"}};
// 	// vector<vector<string>> relation = {{"a","b","c"}, {"1","b","c"}, {"a","b","4"},{"a","5","c"}};
// 	// vector<vector<string>> relation = {{"a","m","2"}, {"b","u","3"}, {"a","m","6"}};
// 	// cout << solution(relation);
// 	solution(relation);
// }
=======
int main(){
	vector<vector<string>> relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","1"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
	// vector<vector<string>> relation = {{"a","m","2"}, {"b","u","3"}, {"a","m","6"}};
	cout << solution(relation);
}
>>>>>>> 25ce2252b9f784b15e23e95f893a2ecd61206b88
