#include<iostream>
using namespace std;

int run_prob5() {
	int until_10 = 2520;
    int normal = until_10 * 11 * 13 * 17 * 19;
	if (normal % 16 == 0) {
		return normal;
	}
	else {
		return normal * 2;
	}
}