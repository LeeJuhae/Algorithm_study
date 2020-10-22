#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;

template <typename T>
set<vector<T> > combination(vector<T>& arr, int k) {
	int arr_size = arr.size();
	set<vector<T> >ret;
	vector<int> flag(arr_size);

	for (int i = 0 ; i < k ; ++i) {
		if (i < k)
			flag[i] = true;
		else
			flag[i] = false;
	}
	sort(flag.begin(), flag.end());

	do {
		vector<T> temp;
		for(int i = 0; i < arr_size ; ++i) {
			if (flag[i])
				temp.push_back(arr[i]);
		}
		ret.insert(temp);
	} while (next_permutation(flag.begin(), flag.end()));
	return ret;
}

// int main(){
// 	vector <int> arr = {1,2,3,4};
// 	set<vector<int> > ret;
// 	ret = combination(arr, 2);
// 	for (auto &row : ret) {
// 		for (auto &col : row)
// 			printf("%d ", col);
// 		printf("\n");
// 	}
// 	return 0;
// }
