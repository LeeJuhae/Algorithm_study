#include <string>

using namespace std;

string solution(string s) {
	int len = s.length();
	if (len % 2 == 0)
		return s.substr((len-1) / 2, 2);
	return s.substr((len / 2), 1);
}

// substr(position, length);
