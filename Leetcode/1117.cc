#include <functional>
#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>

using namespace std;

#include <condition_variable>
        
class Semaphore {
public:
    Semaphore (int count_ = 0)
    : count(count_) 
    {
    }
    
    inline void release() {
        std::unique_lock<std::mutex> lock(mtx);
        count++;
    }
    inline bool try_acquire() {
        std::unique_lock<std::mutex> lock(mtx);
        if (count > 0) {
            count--;
            return true;
        } else {
            return false;
        }
    }
private:
    std::mutex mtx;
    int count;
};

class H2O {
public:
    H2O(): hs(0), os(0) {}

    void hydrogen(function<void()> releaseHydrogen) {
        // We have a hydrogen atom. Wait until there are two Hydrogen atoms and one oxygen atom.
        hs.release();
        bool first = true;
        auto cleanup = [&]() {
            // Release oxygen, and other hydrogen, notify ro, rh condition variable.
            //std::cout << "called cleanup from hydrogen" << endl;
            {
                std::unique_lock<std::mutex> ul(pm);
                sp.wait(ul, [&] {
                    auto cond = release_oxygen == 0 && release_hydrogen == 0;
                    if (cond) {
                        release_oxygen += 1;
                        release_hydrogen += 1;
                    }
                    return cond;
                });
            }
            rh.notify_one();
            ro.notify_one();
        };
        while (true) {
            if (!first) {
                std::unique_lock<std::mutex> ul(pm);
                rh.wait(ul, [&]() {
                    auto cond = release_hydrogen > 0;
                    if (cond) {
                        cout << "releasing hydrogen" << release_hydrogen << endl;
                        release_hydrogen--;
//                        cout << "releasing hydrogen" <<endl;
                    }
                    return cond;
                });
                break;
            } else {
                first = false;
            }
            if (!os.try_acquire()) {
                continue;
            }
            //cout << "hydrogen, O acquired" << endl;
            if (!hs.try_acquire()) {
                os.release();
                continue;
            }
            //cout << "hydrogen, H acquired" << endl;
            if (!hs.try_acquire()) {
                os.release();
                hs.release();
                continue;
            }
            //cout << "hydrogen, H2O acquired" << endl;
            {   
                std::unique_lock<std::mutex> pml(pm);
                sp.wait(pml, [&]() {
                    return released % 3 == 0;
                });
            }
            cleanup();
            break;
        }
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        {
            std::unique_lock<std::mutex> pml(pm);
            released += 1;
        }
        sp.notify_all();
    }

    void oxygen(function<void()> releaseOxygen) {
        os.release();
        bool first = true;
        auto cleanup = [&]() {
            // Release 2 hydrogen, and notify rh condition variable.
            {   
                std::unique_lock<std::mutex> ul(pm);
                sp.wait(ul, [&] {
                    auto cond = release_oxygen == 0 && release_hydrogen == 0;
                    if (cond) {
                        release_hydrogen += 2;
                    }
                    return cond;
                });
            }
            rh.notify_one();
            rh.notify_one();
        };
        while (true) {
            if (!first) {
                std::unique_lock<std::mutex> ul(pm);
                ro.wait(ul, [&]() {
                    auto cond = release_oxygen > 0;
                    if (cond) {
                        cout << "releasing oxygen" << release_oxygen << endl;
                        release_oxygen--;
                    }
                    return cond;
                });
                break;
            } else {
                first = false;
            }
            if (!os.try_acquire()) {
                continue;
            }
            //cout << "oxygen, O acquired" << endl;
            if (!hs.try_acquire()) {
                os.release();
                continue;
            }
            //cout << "oxygen, H acquired" << endl;
            if (!hs.try_acquire()) {
                os.release();
                hs.release();
                continue;
            }
            //cout << "oxygen, H2O acquired" << endl;
            {   
                std::unique_lock<std::mutex> pml(pm);
                sp.wait(pml, [&]() {
                    return released % 3 == 0;
                });
            }
            cleanup();
            break;
        }
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        {
            std::unique_lock<std::mutex> pml(pm);
            released += 1;
        }
        sp.notify_all();
    }

private:
    int n;
    std::mutex pm;
    std::condition_variable rh;
    int release_hydrogen = 0;
    std::condition_variable ro;
    int release_oxygen = 0;
    std::condition_variable sp;
    int released = 0;
    Semaphore hs;
    Semaphore os;
};


int main() { 
    auto start = std::chrono::high_resolution_clock::now();

    H2O h2o;
    auto releaseHydrogen = [&] () {
        h2o.hydrogen([&] () {
            //std::cout << "H";
        });
    };
    auto releaseOxygen = [&] () {
        h2o.oxygen([&] () {
            //std::cout << "O";
        });
    };

    std::string input = "HHOHHOOOOHHHHHH";
    std::vector<std::thread> threads(sizeof(input));

    int i = 0;
    for (char c : input) {
        if (c == 'O') {
            threads[i++] = std::thread(releaseOxygen);
        }
        if (c == 'H') {
            threads[i++] = std::thread(releaseHydrogen);
        }
    }
    for(int i = 0; i < size(threads); ++i) {
        threads[i].join();
        //cout << "joined " << input[i] << endl;
    }
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
 
    // To get the value of duration use the count()
    // member function on the duration object
    std::cout << std::endl << duration.count() << "ms" << std::endl;
}