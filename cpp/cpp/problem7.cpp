#include<iostream>
#include<vector>
using namespace std;

bool is_prime(vector<int> primes, int val) {
	for (int i = 0; i < primes.size(); i++) {
		if (val % primes[i] == 0) {
			return false;
		}
	}
	return true;
}

int run_prob7() {
	vector<int> primes;
	int cnt, number;
	bool res;
	// initialize
	primes.push_back(2);
	primes.push_back(3);
	primes.push_back(5);
	primes.push_back(7);
	primes.push_back(11);
	cnt = 5;
	number = 12;
	while (true) {
		res = is_prime(primes, number);
		if (res) {
			cnt++;
			primes.push_back(number);
		}
		if (cnt >= 10001) {
			break;
		}
		number++;
	}
	return number;
}
