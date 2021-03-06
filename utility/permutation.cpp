#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;

template <typename T>
vector<vector<T> > permutation(vector<T>& arr, int k) {
	int arr_size = arr.size();
	vector<vector<T> >ret;
	vector<bool> flag(arr_size);

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
		sort(temp.begin(), temp.end());
		do {
			ret.push_back(temp);
		} while (next_permutation(temp.begin(), temp.end()));
	} while (next_permutation(flag.begin(), flag.end()));
	return ret;
}

// int main(){
// 	vector <int> arr = {1,2,3,4};
// 	vector<vector<int> > ret;
// 	ret = permutation(arr, 3);
// 	for (auto &row : ret) {
// 		for (auto &col : row)
// 			printf("%d ", col);
// 		printf("\n");
// 	}
// 	return 0;
// }
