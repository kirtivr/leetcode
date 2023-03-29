#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>

class BoundedBlockingQueue {
public:
    BoundedBlockingQueue(int capacity): capacity(capacity) {}
    
    void enqueue(int element) {
        while (size() >= capacity) {
        }
        //std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        std::lock_guard<std::mutex> guard(elements_mutex);
        //std::cout << "Enqueued " << element << std::endl;
        elements.push_back(element);
    }
    
    int dequeue() {
        while (size() == 0) {
            // Release mutex and block.
        }
        //std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        //std::cout << "size of elements = " << size();
        //std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        std::lock_guard<std::mutex> guard(elements_mutex);
        int ret = elements.front();
        elements.pop_front();
        return ret;
    }
    
    int size() {
        std::lock_guard<std::mutex> guard(elements_mutex);
        // std::cout<< "size = " << elements.size();
        return elements.size();
    }

public:
    int capacity;
    std::mutex elements_mutex;
    std::deque<int> elements;
};

int main() { 
    BoundedBlockingQueue queue(2);
    std::vector<int> enqueue {1, 2, 3};
    std::thread t1([&enqueue, &queue] (){
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        queue.enqueue(1);
        //while (queue.size() != 0) {
        //}
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        queue.enqueue(0);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        queue.enqueue(2);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        queue.enqueue(3);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        queue.enqueue(4);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    });
    std::thread t2([&queue] () {
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        std::cout << "Dequeued " << queue.dequeue() << " from queue.\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        std::cout << "Dequeued " << queue.dequeue() << " from queue.\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        std::cout << "Dequeued " << queue.dequeue() << " from queue.\n";
    });
 
    t1.join();
    t2.join();

    std::cout << "Queue size is " << queue.size() << std::endl;
}