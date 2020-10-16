#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> numbers) {
	set<int> s_answer;
	vector<int> v_answer;
	for (int i = 0 ; i < numbers.size() ; i++) {
		for (int j = i + 1 ; j < numbers.size() ; j++) {
			s_answer.insert(numbers[i]+numbers[j]);
		}
	}
	v_answer.assign(s_answer.begin(), s_answer.end());
	return v_answer;
}
