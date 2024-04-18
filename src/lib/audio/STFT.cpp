#include <fstream>
#include <string>
#include <iostream>
using namespace std;
void read(const int len, char* argv[]) {
    ifstream file("../../data/audio/data.bin", ios::binary);
    if (!file.is_open()) {
        cout << "Error opening file" << endl;
        return;
    }
    char* reader = new char[len];
    file.read(reader, len);
    file.close();
    for (int i = 0; i<len; i++) {
        cout << static_cast<int>(reader[i]) << endl;
    }
    delete reader;
}

void main(int argc, char* argv[]) {
    int a = stoi(argv[1]);
    cout << string(argv[0]) << endl;
    read(a, argv);
}