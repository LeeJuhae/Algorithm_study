#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(const pair<string,int>& a, const pair<string,int>& b) {
	if (a.second == b.second)
		return a.first > b.first;
	return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
	vector<int> answer;
	map<string, int> info;

	// genre별 재생 횟수의 총합을 구한다.
	for(int i = 0 ; i < genres.size() ; i++) {
		if (info.find(genres[i]) != info.end())
			info[genres[i]] += plays[i];
		else
			info[genres[i]] = plays[i];
	}
	// genre(key) : 재생 횟수(value) map인 info를 vector로 바꾼 후, value를 기준으로 내림차순 정렬한다.
	vector<pair<string,int>> vec( info.begin(), info.end() );
	sort(vec.begin(), vec.end(), cmp);

	for (int i = 0 ; i < vec.size() ; i++) {
		string genre = vec[i].first;
		int a = 0; // 가장 큰 재생 횟수 값
		int b = 0; // 두번째로 큰 재생 횟수 값
		int a_idx = -1; // 가장 큰 재생 횟수 값을 가진 노래의 고유 번호
		int b_idx = -1; // 두번째로 큰 재생 횟수 값을 가진 노래의 고유 번호
		for(int j = 0 ; j < genres.size() ; j++) {
			if (genre == genres[j]) {
				if (plays[j] > a) {
					b = a;
					b_idx = a_idx;
					a = plays[j];
					a_idx = j;
				}
				else if((plays[j] <= a) && (plays[j] > b)) {
					b = plays[j];
					b_idx = j;
				}
			}
		}
		if (a_idx != -1) {
			answer.push_back(a_idx);
			if (b_idx != -1)
				answer.push_back(b_idx);
		}
	}
	return answer;
}
