/*
	10825. 국영수
*/
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Person {
	string name;
	int kor, eng, math;
};

bool compare(Person a, Person b) {
	if (a.kor == b.kor) {
		if (a.eng == b.eng) {
			if (a.math == b.math) {
				return a.name < b.name;
			} else {
				return a.math > b.math;
			}
		}
		else {
			return a.eng < b.eng;
		}
	} else {
		return a.kor > b.kor;
	}
}
int main(void) {
	int T;
	scanf("%d", &T);
	vector<Person> people(T);

	for (int i = 0 ; i < T ; i++) {
		char name[100];
		scanf("%s %d %d %d", name, &(people[i].kor), &(people[i].eng), &(people[i].math));
		people[i].name = name;
	}
	sort(people.begin(), people.end(), compare);
	for (int i = 0 ; i < T ; i++) {
		printf("%s\n", people[i].name.c_str());
	}
	return 0;
}
