#include<iostream>
using namespace std;

int run_prob6() {
	int square_sum = 0;
	int sum_square = 0;
	for (int i = 1; i <= 100; i++) {
		square_sum += i;
		sum_square += i * i;
	}
	return square_sum * square_sum - sum_square;
}