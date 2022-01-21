#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;



int main()
{
	vector <int> stacks;
	string x;
	cout << "Enter the height of each stack from left to right" << endl;
	getline(cin, x);
	stringstream ss(x);
	string digit;
	while (ss >> digit) {
		if (stoi(digit) > 4) {
			cout << "Stack size is invalid please try again" << endl;
			break;
		}
		stacks.push_back(stoi(digit));
	}
	for (std::vector<int>::iterator it = stacks.begin(); it != stacks.end(); ++it)
		std::cout << ' ' << *it;
	cout << endl;
	
	vector <int> process;
	string com;
	int crane = 0;
	int box = 0;
	cout << "Please enter the process command" << endl;
	getline(cin, com);
	stringstream s(com);
	while (s >> digit) {
		process.push_back(stoi(digit));
	}
	for (std::vector<int>::iterator it = process.begin(); it != process.end(); ++it)
		std::cout << ' ' << *it;
		
	for (int i = 0; i < process.size(); i++) {
		switch (process[i]) {
		case 0:
			//quit
		case 1:
			//move left unless at 0
			if (i == 0) {
				cout << "You are already at the left most stack" << endl;
				crane = 0;
			}
			else {
				crane++;
			}

		case 2:
			//move right unless at end
			if (i == process.size()) {
				cout << "You are already at the right most stack" << endl;
				crane = process.size();
			}
			else {
				crane--;
			}
		case 3:
			//pick up box unless no box present or currently carrying box
			if (box == 0 && stacks[crane] != 0) {
				box = 1;
				stacks[crane]--;
			}
			if (box == 1 || stacks[crane] == 0) {
				cout << "The crane is currently carrying a box or the stack is empty" << endl;
			}

		case 4:
			if (box == 1 && stacks[crane] < 4) {
				box = 0;
				stacks[crane]++;
			}
			if (box == 0 || stacks[crane] >= 4)
				cout << "There is no box being carried or the stack is at max size" << endl;
			
			//drop box unless at stack size 4 or carrying no box
		case 5:
			//error if number not between 0 and 4
		}

	}
	return 0;
}