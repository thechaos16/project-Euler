#include<iostream>
#include<math.h>
using namespace std;

int count_divisor(int number) {
	int cnt = 1;
	for (int i = 2; i <= int(sqrt(number)); i++) {
		if ((number % i) == 0) {
			cnt++;
			if (number / i != i)
				cnt++;
		}
	}
	return cnt;
}

int run_prob12() {
	int idx = 1;
	int cnt = 0;
	while (true) {
		if (idx >= 1000000)
			break;
		cnt = count_divisor(idx * (idx + 1) / 2);
		if (cnt >= 500) {
			break;
		}
		idx++;
	}
	return (idx * (idx + 1) / 2);
}