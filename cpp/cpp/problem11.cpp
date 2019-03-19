#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

vector<string> split(const string str, const string delim)
{
	vector<string> tokens;
	size_t prev = 0, pos = 0;
	do
	{
		pos = str.find(delim, prev);
		if (pos == string::npos) pos = str.length();
		string token = str.substr(prev, pos - prev);
		if (!token.empty()) tokens.push_back(token);
		prev = pos + delim.length();
	} while (pos < str.length() && prev < str.length());
	return tokens;
}

int run_prob11() {
	string file_path = "problem11.txt";
	vector<string> input_str;
	vector<vector<int>> matrix;
	string line;

	ifstream open_file(file_path);
	if (open_file.is_open()) {
		while (getline(open_file, line)) {
			input_str.push_back(line);
		}
	}
	for (int i = 0; i < input_str.size(); i++) {
		vector<string> temp = split(input_str[i], " ");
		vector<int> row;
		for (int j = 0; j < temp.size(); j++) {
			row.push_back(stoi(temp[j]));
		}
		matrix.push_back(row);
	}

	int max_product = 0;
	int cur_product = 1;
	for (int i = 0; i < matrix.size(); i++) {
		for (int j = 0; j < matrix[i].size(); j++) {
			// row
			if (j + 3 < matrix[i].size()) {
				cur_product = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3];
				if (cur_product > max_product) {
					max_product = cur_product;
				}
			}
			// col
			if (i + 3 < matrix.size()) {
				cur_product = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j];
				if (cur_product > max_product) {
					max_product = cur_product;
				}
			}
			// diag
			if (j + 3 < matrix[i].size() && i + 3 < matrix.size()) {
				cur_product = matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3];
				if (cur_product > max_product) {
					max_product = cur_product;
				}
			}
			// reverse diag
			if (j + 3 < matrix[i].size() && i - 3 >= 0){
				cur_product = matrix[i][j] * matrix[i - 1][j + 1] * matrix[i - 2][j + 2] * matrix[i - 3][j + 3];
				if (cur_product > max_product) {
					max_product = cur_product;
				}
			}
		}
	}

	return max_product;
}