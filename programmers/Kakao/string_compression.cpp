#include <string>
#include <vector>
#include <iostream>

using namespace std;

string appendStr(int count, string previous, string new_string){
	if (count > 1)
		new_string += to_string(count);
	new_string += previous;
	return (new_string);
}

int solution(string s) {
	int length = s.length();
	int answer = length;
	int count;
	string previous;
	string new_string;

	for(int len = 1 ; len <= length / 2 ; len++){
		count = 0;
		previous = "";
		new_string = "";
		for(int i = 0 ; i < length ; i += len)
		{
			if (s.substr(i,len).compare(previous) == 0)
			{
				count++;
			}
			else
			{
				new_string = appendStr(count, previous, new_string);
				count = 1;
				previous = s.substr(i,len);
			}
			if (i + len >= length)
				new_string = appendStr(count, previous, new_string);
		}
		if (count >= 1 && !(new_string.compare("")))
		{
			if (count > 1)
				new_string += to_string(count);
			new_string += previous;
		}
		if (new_string.length() < answer)
			answer = new_string.length();
	}
    return answer;
}

// int main(){
// 	string s = "aabbaccc";
// 	cout << solution(s);
// 	return (0);
// }
