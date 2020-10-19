#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

long long solution(int n, vector<int> times) {
	long long left = 1;
	long long right = (*max_element(times.begin(), times.end())) * (long long)n;
	long long mid;
	long long answer = 0;
	while (left <= right) {
		long long people = 0;
		mid = (left + right) / 2;
		for (int i = 0 ; i < times.size() ; i++) {
			people += mid / times[i];
		}
		if (people >= n) {
			answer = mid;
			right = mid-1;
		}
		else {
			left = mid+1;
		}
	}
	return answer;
}
