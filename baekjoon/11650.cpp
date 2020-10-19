#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Location {
	int x;
	int y;
};

bool compare(Location &a, Location &b) {
	if (a.x == b.x)
		return a.y < b.y;
	return a.x < b.x;
}

int main() {
	int N;
	scanf("%d", &N);
	vector<Location> loc(N);
	for(int i = 0 ; i < N ; i++) {
		scanf("%d %d", &(loc[i].x), &(loc[i].y));
	}
	sort(loc.begin(), loc.end(), compare);
	for(int i = 0 ; i < N ; i++) {
		printf("%d %d\n", loc[i].x, loc[i].y);
	}
	return 0;
}
