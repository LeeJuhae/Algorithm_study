#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	deque<int> q;
	deque<int> idx;

	for(int i = 0 ; i < priorities.size() ; i++) {
		idx.push_back(i);
		q.push_back(priorities[i]);
	}
	int max = *max_element(q.begin(), q.end());
	while (!q.empty()) {
		int temp = q.front();
		int now_idx = idx.front();
		q.pop_front();
		idx.pop_front();
		if (temp == max) {
			++answer;
			if (location == now_idx)
				break;
			max = *max_element(q.begin(), q.end());
		}
		else {
			q.push_back(temp);
			idx.push_back(now_idx);
		}
	}
	return answer;
}
