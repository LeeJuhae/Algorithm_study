#include <string>
#include <vector>

// #include <iostream>

using namespace std;

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;

	for(int i = 0 ; i < queries.size() ; i++)
	{
		int	count = 0;
		int	q_mark_idx = queries[i].find("?");
		int	q_is_prefix = 0;
		string cmp_str = "";

		if (q_mark_idx != string::npos)
		{
			if (q_mark_idx == 0)
			{
				q_is_prefix = 1;
				q_mark_idx = queries[i].find_last_of("?") + 1;
				cmp_str = queries[i].substr(q_mark_idx);
			}
			else
			{
				cmp_str = queries[i].substr(0, q_mark_idx);
			}
			for(int j = 0 ; j < words.size() ; j++)
			{
				if (queries[i].length() != words[j].length())
					continue;
				else
				{
					if (q_is_prefix == 0)
					{
						if (words[j].substr(0, q_mark_idx).compare(queries[i].substr(0, q_mark_idx)) == 0)
							count++;
					}
					else
					{
						if (words[j].substr(q_mark_idx).compare(queries[i].substr(q_mark_idx)) == 0)
							count++;
					}
				}
			}
		}
		answer.push_back(count);
	}
    return answer;
}

// int main(){
// 	// vector<string>v(6);
// 	// vector<string>q(5);
// 	vector<string> v = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
// 	vector<string> q = {"fro??", "????o", "fr???", "fro???", "pro?"};
// 	vector<int> ret = solution(v, q);
// 	for(int i = 0 ; i < ret.size() ; i++)
// 		cout << ret[i] << endl;
// }
