#include <vector>

using namespace std;

void dfs(vector<vector<int>>& computers, vector<bool>& visited, int now, int n) {
	visited[now] = true;
	for(int i = 0 ; i < n ; i++) {
		if (computers[now][i] && !visited[i])
			dfs(computers, visited, i, n);
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	vector<bool> visited(n, false);

	for(int i = 0 ; i < n ; i++) {
		if (!visited[i]) {
			++answer;
			dfs(computers, visited, i, n);
		}
	}
	return answer;
}
