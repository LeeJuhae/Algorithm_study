#include <string>
#include <vector>
#include <map>
#include <algorithm>
// #include <iostream>

using namespace std;

bool compare(vector<int> &a, vector<int> &b)
{
	return a[1] < b[1] ;
}

int solution(vector<int> food_times, long long k) {
	vector<vector<int>>time_idx(food_times.size());
	int answer = -1;
	int	idx;
	int before_time = 0;

	for(int i = 0 ; i < food_times.size() ; i++)
	{
		time_idx[i].push_back(food_times[i]);
		time_idx[i].push_back(i + 1);
	}

	sort(time_idx.begin(), time_idx.end());

	for(int i = 0 ; i < food_times.size() ;)
	{
		int same_sec = 1;
		for (int j = i + 1 ; j < food_times.size() ; j++)
		{
			if (time_idx[i][0] != time_idx[j][0])
				break ;
			same_sec++;
		}
		if (k < (time_idx[i][0] - before_time) * (food_times.size() - i))
		{
			if (time_idx.begin() + i + 1 == time_idx.end())
			{
				answer = time_idx[i][1];
				break ;
			}
			else
			{
				sort(time_idx.begin() + i, time_idx.end(), compare);
				answer = time_idx[i + k % (food_times.size() - i)][1];
				break ;
			}
		}
		if (i + same_sec >= food_times.size())
			break ;
		k -= (time_idx[i][0] - before_time) * (food_times.size() - i);
		before_time = time_idx[i][0];
		i += same_sec;
	}
	return answer;
}

// int main()
// {
// 	// vector<int> food_times = {3,1,2};
// 	// cout << solution(food_times, 5); // 1
// 	// vector<int> food_times = {1,1,1,1,1};
// 	// cout << solution(food_times, 4);
// 	// vector<int> food_times = {4,3,5,6,2};
// 	// cout << solution(food_times, 7); // 2
// 	vector<int> food_times = {3,1,1,1,2,4,3};
// 	cout << solution(food_times,12); // 6
// }
