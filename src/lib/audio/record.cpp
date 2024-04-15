#include <iostream>
#include <vector>
#include <C:/Users/User/AppData/Local/Programs/Python/Python39/Lib/site-packages/sounddevice.py>

int main() {
    // Set up parameters
    int sample_rate = 44100;
    int duration_seconds = 5;  // Recording duration

    // Record audio
    std::vector<float> recording = sd::rec(sample_rate * duration_seconds, sample_rate, 1);

    // Print recording length
    std::cout << "Recorded " << recording.size() << " samples." << std::endl;

    return 0;
}