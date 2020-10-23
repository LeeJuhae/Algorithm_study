#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	double result = 0;
	double x, y, c;
	double pow_x, pow_y;
	double i, j, mid;
	double left, right;
	scanf("%lf %lf %lf", &x, &y, &c);
	left = 0;
	right = min(x, y);
	pow_x = x*x;
	pow_y = y*y;
	while (right - left > 0.000001) {
		mid = (left + right) / 2.0;
		i = sqrt(pow_x - mid*mid);
		j = sqrt(pow_y - mid*mid);
		if (c <= ((i*j)/(i + j))) {
			result = mid;
			left = mid;
		} else{
			right = mid;
		}
	}
	printf("%.3lf", result);
	return 0;
}
