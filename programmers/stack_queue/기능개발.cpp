#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	int size = progresses.size();
	int idx = 0;
	int day = 0;

	while (idx < size) {
		day = (int)ceil((100 - progresses[idx]) / (double)speeds[idx]);
		answer.push_back(1);
		++idx;
		while (idx < size) {
			if (progresses[idx] + speeds[idx] * day >= 100) {
				++answer.back();
				++idx;
			}
			else {
				break;
			}
		}
	}
	return answer;
}
