#include<iostream>
using namespace std;

int run_prob9() {
	int c, val;
	val = 0;
	for (int a = 1; a < 333; a++) {
		for (int b = a + 1; b < 1000; b++) {
			c = 1000 - a - b;
			if (c <= b || c <= a) {
				continue;
			}
			if (c * c == a * a + b * b) {
				if (a * b * c > val) {
					val = a * b * c;
				}
			}
		}
	}
	return val;
}