#include<iostream>
#include<math.h>
using namespace std;


bool is_palindrome(int value) {
	int length = 0;
	int temp_val = value;
	int *change;
	while (true) {
		if (temp_val == 0) {
			break;
		}
		else {
			length++;
		}
		temp_val /= 10;
	}
	change = new int[length];
	for (int i = 0; i < length; i++) {
		temp_val = value % 10;
		change[i] = temp_val;
		value /= 10;
	}
	bool palin = true;
	for (int i = 0; i < length; i++) {
		if (change[i] != change[length - i - 1]) {
			palin = false;
			break;
		}
	}
	return palin;
}

int run_prob4(int value) {
	int max_val = 0;
	int min, max, new_val;
	min = pow(10, value - 1);
	max = pow(10, value) - 1;
	for (int i = min; i <= max; i++) {
		for (int j = min; j <= max; j++) {
			new_val = i * j;
			if (is_palindrome(new_val)) {
				if (new_val > max_val) {
					max_val = new_val;
				}
			}
		}
	}
	return max_val;
}
