#include <fstream>
#include <string>
#include <iostream>
using namespace std;
fstream file("C:/Users/User/PycharmProjects/WhistleRun/src/data/audio/data.bin",ios::in | ios::out |ios::binary);

int* read(const int len) {
    char* reader = new char[len];
    int* arr = new int[len];
    file.read(reader, len);
    for (int i = 0; i<len; i++) {
        arr[i] = static_cast<int>(reader[i]);
    }
    delete reader;
    return arr;
}

void write(int* arr, const int len){
    for (int i = 0; i < len; i++) {
        file.write(reinterpret_cast<const char*>(&arr[i]), sizeof(arr[i]));
    }

}

void main(int argc, char* argv[]) {
    int a = stoi(argv[1]);
    int* data = read(a);
    write(data, a);
    delete data;
}