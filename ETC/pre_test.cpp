/*
	NHN Pre-Test 1차
*/

#include <cstdio>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
	int N;
	int cnt = 0;
	scanf("%d", &N);
	vector<vector<int> > board;
	vector<int> domain;
	for(int i = 0 ; i < N ; ++i) {
		vector<int> row(N);
		board.push_back(row);
		for(int j = 0 ; j < N ; ++j) {
			scanf("%d", &board[i][j]);
		}
	}
	int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
	for(int i = 0 ; i < N ; ++i) {
		for(int j = 0 ; j < N ; ++j) {
			if (board[i][j]) {
				deque<vector<int> > q;
				int domain_cnt = 0;
				q.push_back(vector<int> {i, j});
				while (!q.empty()) {
					vector<int> temp = q.front();
					q.pop_front();
					for(int i = 0 ; i < 4 ; i++) {
						int x = temp[0] + directions[i][0];
						int y = temp[1] + directions[i][1];
						if (((0 <= x) && (x < N)) && ((0 <= y) && (y < N))) {
							if (board[x][y]) {
								q.push_back(vector<int> {x, y});
								board[x][y] = 0;
								++domain_cnt;
							}
						}
					}
				}
				++cnt;
				domain.push_back(domain_cnt);
			}
		}
	}
	printf("%d\n", cnt);
	sort(domain.begin(), domain.end());
	for(int i = 0 ; i < domain.size() ; ++i) {
		if (i != domain.size()-1)
			printf("%d ", domain[i]);
		else
			printf("%d\n", domain[i]);
	}
	return 0;
}
