#include<iostream>
#include<list>


using namespace std;
struct Myhash {
	int Bucket;
	list<int>* table;
	Myhash(int b) {
		Bucket = b;
		table = new list<int>[Bucket];
	}
	int hash(int key) {
		return key % Bucket;
	}
	void insert(int key) {
		int i = hash(key);
		table[i].push_back(key);
	}

	void print() {
		for (auto i = 0; i < Bucket; i++) {
			for (auto j : table[i]) {
				cout << j << " ";
			}
			cout << "\n";
		}
	}
};
int main() {
	struct Myhash h = Myhash(7);
	h.insert(46);
	h.insert(35);
	h.insert(29);
	h.insert(3);
	h.insert(8);
	h.insert(16);
	h.insert(22);
	h.print();
	return 0;
}
