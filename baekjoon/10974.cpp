/*
	모든 순열
*/

#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
	vector<int> vec;
	scanf("%d", &N);
	for(int i = 1 ; i <= N ; i++)
		vec.push_back(i);
	do {
		for(int i = 0 ; i < N ; i++) {
			printf("%d", vec[i]);
			if (i != N-1)
				printf(" ");
			else
				printf("\n");
		}
	} while (next_permutation(vec.begin(), vec.end()));
	return 0;
}
