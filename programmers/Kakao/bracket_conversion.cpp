/*
* 주어진 logic
* 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
* 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
* 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
*   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
* 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
*   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
*   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
*   4-3. ')'를 다시 붙입니다.
*   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
*   4-5. 생성된 문자열을 반환합니다.
*/

#include <string>
#include <vector>

#include <iostream>

using namespace std;

int is_right_str(string str){
	int count = 0;

	for(int i = 0 ; i < str.length() ; i++)
	{
		if (str[i] == '(')
			count++;
		else
			count--;
		if (count < 0)
			return (-1);
	}
	return (1);
}

int getSeparateIdx(string p)
{
	int	idx = 0;
	int	left = 0;
	int right = 0;

	for (; idx < p.length() ; idx++){
		if (p[idx] == '(')
			left++;
		else if (p[idx] == ')')
			right++;
		if (left > 0 && left == right)
			break ;
	}
	return (idx);
}

string solution(string p) {
    string answer = "";
	string u = "";
	string v = "";
	int separate_idx = 0;

	if (p.compare("") != 0)
	{
		separate_idx = getSeparateIdx(p);
		u = p.substr(0, separate_idx + 1);
		v = p.substr(separate_idx + 1);
		if (is_right_str(u) == 1)
		{
			answer = answer + u + solution(v);
		}
		else
		{
			answer += '(';
			answer += solution(v);
			answer += ')';
			for(int i = 1 ; i < u.length() - 1; i++)
			{
				if (u[i] == '(')
					answer +=  ')';
				else
					answer += '(';
			}
		}
	}
    return answer;
}

// int main(){
// 	string s = "()))((()";
// 	cout << solution(s);
// }
