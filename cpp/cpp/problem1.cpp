#include<iostream>
using namespace std;

int run_prob1(int max) {
	int sum = 0;
	int max3, max5;
	max3 = (max - 1) / 3;
	max5 = (max - 1) / 5;
	for (int i = 1; i <= max3; i++) {
		sum += (3 * i);
	}
	for (int i = 1; i <= max5; i++) {
		if (i % 3 != 0) {
			sum += (5 * i);
		}
	}
	return sum;
}