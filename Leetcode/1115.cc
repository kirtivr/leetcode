#include <functional>
#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>

class FooBar {
public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(std::function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            {
                std::unique_lock<std::mutex> lg(pm);
                cv.wait(lg, [this] {
                    return !should_print;
                });            
            	// printFoo() outputs "foo". Do not change or remove this line.
            	printFoo();
                should_print = true;
                lg.unlock();
                cv.notify_one();
            }
        }
    }

    void bar(std::function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            {
                std::unique_lock<std::mutex> lg(pm);
                cv.wait(lg, [this] {
                    return should_print;
                });
            	// printBar() outputs "bar". Do not change or remove this line.
            	printBar();
                should_print = false;
                lg.unlock();
                cv.notify_one();
            }
        }
    }

private:
    int n;
    std::mutex pm;
    bool should_print = false;
    std::condition_variable cv;
};

int main() { 
    auto start = std::chrono::high_resolution_clock::now();

    FooBar fb(10);
    std::thread t1([&fb] {
        fb.foo([] (){
            std::cout << "foo";
        });
    });
    std::thread t2([&fb] {
        fb.bar([] (){
            std::cout << "bar";
        });
    });
    t1.join();
    t2.join();
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
 
    // To get the value of duration use the count()
    // member function on the duration object
    std::cout << std::endl << duration.count() << "ms" << std::endl;
}