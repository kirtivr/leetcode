#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>
#include <functional>

using namespace std;
enum ToPrint {
    FIZZ = 0,
    BUZZ,
    FIZZBUZZ,
    NUM,
    INVALID
};

class FizzBuzz {
private:
    int n;
    int i = 1;
    std::mutex m;
    std::condition_variable i_changed;

public:
    FizzBuzz(int n) {
        this->n = n;
    }

    ToPrint evaluateI() {
        if (i % 3 == 0 && i % 5 != 0) {
            return FIZZ;
        } else if (i % 3 == 0 && i % 5 == 0) {
            return FIZZBUZZ;
        } else if (i % 3 != 0 && i % 5 != 0) {
            return NUM;
        } else if (i % 5 == 0 && i % 3 != 0) {
            return BUZZ;
        }
        return INVALID;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        while (true) {
            std::unique_lock<std::mutex> um(m);
            //cout << "i = " << i << "evaluateI = " << evaluateI();
            i_changed.wait(um, [&]() {
                return evaluateI() == FIZZ || i > n;
            });
            if (i > n) {
                break;
            }
            printFizz();
            i += 1;
            i_changed.notify_all();
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        while (true) {
            std::unique_lock<std::mutex> um(m);
            i_changed.wait(um, [&]() {
                return evaluateI() == BUZZ || i > n;
            });
            if (i > n) {
                break;
            }
            printBuzz();
            i += 1;
            i_changed.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        while (true) {
            std::unique_lock<std::mutex> um(m);
            i_changed.wait(um, [&]() {
                return evaluateI() == FIZZBUZZ || i > n;
            });
            if (i > n) {
                break;
            }
            printFizzBuzz();
            i += 1;
            i_changed.notify_all();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        while (true) {
            std::unique_lock<std::mutex> um(m);
            i_changed.wait(um, [&]() {
                return evaluateI() == NUM || i > n;
            });
            if (i > n) {
                break;
            }
            printNumber(i);
            i += 1;
            i_changed.notify_all();
        }
    }
};


int main() { 
    auto start = std::chrono::high_resolution_clock::now();
    int N = 5;
    FizzBuzz fb(N);
    std::thread fizz([&]{
        fb.fizz([]{
            std::cout << "fizz" << std::endl;
        });
    });
    std::thread buzz([&]{
        fb.buzz([]{
            std::cout << "buzz" << std::endl;
        });
    });
    std::thread fizzbuzz([&]{
        fb.fizzbuzz([]{
            std::cout << "fizzbuzz" << std::endl;
        });
    });
    std::thread num([&]{
        fb.number([&](int n){
            std::cout << n << std::endl;
        });
    });
    fizz.join();
    buzz.join();
    fizzbuzz.join();
    num.join();
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
 
    // To get the value of duration use the count()
    // member function on the duration object
    std::cout << duration.count() << std::endl;
}
