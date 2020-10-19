#include <string>
#include <vector>
#include <iostream>

using namespace std;

int target_num;

int dfs(vector<int> numbers, int now_sum, int depth) {
	if (depth == numbers.size()) {
		if (now_sum == target_num)
			return 1;
		else
			return 0;
	} else {
		return dfs(numbers, now_sum + numbers[depth], depth+1) + dfs(numbers, now_sum - numbers[depth], depth+1);
	}
}

int solution(vector<int> numbers, int target) {
	target_num = target;
	return dfs(numbers, 0, 0);
}
