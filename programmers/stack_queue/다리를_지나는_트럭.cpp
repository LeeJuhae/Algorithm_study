#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	queue<int> q;
	int current_weight = 0;
    int answer = 0;

	for(int i = 0 ; i < truck_weights.size() ; i++)
	{
		if (q.size() < bridge_length && current_weight + truck_weights[i] <= weight)
		{
			q.push(truck_weights[i]);
			current_weight += truck_weights[i];
			answer++;
		}
		else
		{
			while (1)
			{
				if (q.size() == bridge_length)
				{
					current_weight -= q.front();
					q.pop();
					if (current_weight + truck_weights[i] <= weight)
					{
						q.push(truck_weights[i]);
						current_weight += truck_weights[i];
						answer++;
						break ;
					}
					else
					{
						q.push(0);
						answer++;
					}
				}
				else if (current_weight + truck_weights[i] > weight)
				{
					q.push(0);
					answer++;
				}
			}
		}
		if (i == truck_weights.size() - 1)
			answer += bridge_length;
	}
    return answer;
}

int main(){
	vector<int> v;
	// [test_case_1]
	v.push_back(7);
	v.push_back(4);
	v.push_back(5);
	v.push_back(6);
	cout<< solution(2,10,v);

	// [test_case_2]
	v.push_back(10);
	cout<< solution(100,100,v);

	// [test_case_3]
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	v.push_back(10);
	cout<< solution(100,100,v);

	return (0);
}
