#include <iostream>
#include "problem2.h"
using namespace std;


int fibonacci(int number1, int number2) {
	return number1 + number2;
}


int run_prob2() {
	int val1, val2, temp_num;
	long int sum = 0;
	val1 = val2 = 1;
	temp_num = 0;
	while (1) {
		if (temp_num > 4000000) {
			break;
		}
		temp_num = fibonacci(val1, val2);
		val1 = val2;
		val2 = temp_num;
		if (temp_num % 2 == 0) {
			sum += temp_num;
		}
	}
	//cout << sum << endl;
	return sum;
}