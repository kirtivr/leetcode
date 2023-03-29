#include <functional>
#include <chrono>
#include <thread>
#include <iostream>
#include <deque>
#include <mutex>
#include <vector>
#include <map>
//#include <set>

/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */
class HtmlParser {
    public:
        std::vector<std::string> getUrls(std::string startUrl) {
            return {"http://www.news.youtube.com"};
        }
};

class Solution {
public:
    std::string hostnameFromUrl(std::string startUrl) {
        int protocol_pos = startUrl.find_first_of("://");
        std::string path = startUrl.substr(protocol_pos + 3);
        //std::cout << "path = " << path << std::endl;
        return path.substr(0,path.find_first_of("/"));
    }

    bool hostnameMatches(std::string input, std::string hostname) {
        int start = input.find_first_of("://");
        int end = input.substr(start + 3).find_first_of("/");
        bool matches = input.substr(start + 3, end) == hostname;
        return matches;
    }

    void doCrawl(HtmlParser& htmlParser,
        std::vector<std::string>& out, std::string hostname) {
        //std::cout << "hostname = " << hostname << std::endl;
        while (true) {
            std::unique_lock<std::mutex> ul(c);

            // Wait until there is some work.
            cv.wait(ul, [&]() {
                return q.size() > 0 || done;
            });

            if (done) {
                return;
            }
            working++;
            auto startUrl = q.front(); q.pop_back();
            c.unlock();
            for (auto url : htmlParser.getUrls(startUrl)) {
                std::lock_guard<std::mutex> g(c);
                {
                    //std::lock_guard<std::mutex> g(c);
                    if (visited.find(url) != visited.end()) {
                        continue;
                    }
                }
                if (hostnameMatches(url, hostname)) {
                    //std::lock_guard<std::mutex> g(c);
                    visited[url] = true;
                    q.push_back(url);
                }
            }
            c.lock();
            working--;
            if (working == 0 && q.empty()) {
                done = true;
            }
            c.unlock();
            cv.notify_all();
        }
    }

    std::vector<std::string> crawl(std::string startUrl, HtmlParser htmlParser) {
        visited[startUrl] = true;
        q.push_back(startUrl);
        // Extract the hostname from startUrl.
        auto hostname = hostnameFromUrl(startUrl);
        auto num_t = std::thread::hardware_concurrency();
        std::cout<< "Hardware concurrency = " << num_t << std::endl;

        for (int i = 0; i < num_t; ++i) {
            threads.emplace_back([&]() {
                doCrawl(htmlParser, out, hostname);
            });
        }
        for (int i = 0; i < num_t; ++i) {
            threads[i].join();
        }
        std::vector<std::string> out;
        for (auto it = visited.begin(); it != visited.end(); ++it) {
            out.push_back(it->first);
        }
        return out;
    }

public:
    std::vector<std::string> out;
    std::map<std::string, bool> visited;
    std::vector<std::thread> threads;
    std::deque<std::string> q;
    bool done = false;
    int working = 0;
    std::condition_variable cv;
    std::mutex c;
};

int main() {
    std::unique_ptr<Solution> x = std::make_unique<Solution>();
    x->crawl("http:://www.news.youtube.com", HtmlParser());
    return 0;
}