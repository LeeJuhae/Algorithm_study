/*
	소수 찾기
*/

#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;

int solution(string numbers) {
	int answer = 0;
	vector<string> v;
	set<int> s;
	for(int i = 0 ; i < numbers.length() ; ++i) {
		string temp = "";
		temp += numbers[i];
		v.push_back(temp);
	}
	int vec_size = v.size();
	for (int i = 0 ; i < vec_size ; ++i) {
		vector<int> flag;
		//(j - i + 1) 개의 원소로 구성된 순열을 구하고자 한다.
		for (int j = 0 ; j <= i ; ++j)
			flag.push_back(1);
		for (int j = i + 1 ; j < vec_size ; ++j)
			flag.push_back(0);
		// 정렬을 해주지 않으면 1이 0보다 앞에 와서 next_permutation으로 순열을 모두 구할 수 없다.
		// 때문에 오름차순으로 정렬을 하거나 prev_permutation을 사용해야 한다.
		sort(flag.begin(), flag.end());
		do {
			vector<string> temp;
			for(int i = 0; i < flag.size() ; ++i) {
				if (flag[i])
					temp.push_back(v[i]);
			}
			// 위와 동일한 이유로 오름차순 정렬을 해준다.
			sort(temp.begin(), temp.end());
			do {
				string st = "";
				for (int k = 0 ; k < temp.size() ; ++k)
					st += temp[k];
				s.insert(stoi(st));
			} while (next_permutation(temp.begin(), temp.end()));
		} while (next_permutation(flag.begin(), flag.end()));
	}
	for(auto &num : s) {
		bool isPrime = true;
		for (int i = 2 ; i * i <= num ; ++i) {
			if (num % i == 0) {
				isPrime = false;
				break;
			}
		}
		if (num != 0 && num != 1 && isPrime)
			++answer;
	}
	return answer;
}

int main(){
	printf("\n%d", solution("011"));
	return 0;
}
