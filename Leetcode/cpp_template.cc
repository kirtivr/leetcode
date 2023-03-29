#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>
#include <functional>

class Solution {

};

int main() { 
    auto start = std::chrono::high_resolution_clock::now();


    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
 
    // To get the value of duration use the count()
    // member function on the duration object
    std::cout << duration.count() << std::endl;
}