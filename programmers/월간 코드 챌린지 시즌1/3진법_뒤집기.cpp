#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int solution(int n) {
	int answer = 0;
	string str_answer = "";
	while (n > 0) {
		str_answer += (n % 3) + '0';
		n = n / 3;
	}
	reverse(str_answer.begin(), str_answer.end());
	for (int i = 0 ; i < str_answer.size() ; i++)
		answer += (str_answer[i] - '0') * pow(3, i);
	return answer;
}
