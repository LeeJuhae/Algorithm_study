#include <string>
#include <vector>
#include <cstdio>

using namespace std;

vector<int> solution(int brown, int yellow) {
	vector<int> answer;
	int mul = brown + yellow;
	// h*v = brown + yellow, (h-2)*(v-2) = yellow 방정식 2개를 이용해 도출한 식.
	// h+h = (b+4) / 2
	int sum = (int)((brown + 4) / 2);
	for (int v = 1 ; v < sum ; ++v) {
		int h = sum - v;
		if (h * v == mul) {
			answer.push_back(h);
			answer.push_back(v);
			break;
		};
	}
	return answer;
}
