#include <cstdio>
#include <map>
#include <stack>
#include <vector>
#include <utility>
using namespace std;

class LRUCache {
  int capacity;
  vector<pair<int, int>> lru;
  
public:
    LRUCache(int cp) {
      capacity = cp;
    }

  int get(int);
  void put(int,int);
  
};
    
int LRUCache::get(int key) {
  vector<pair<int,int>>::iterator it;
  int i;
  
  for (it = this->lru.begin(), i = 0; it <= this->lru.end() && i < this->lru.size(); it++ ) {
    if((*it).first == key) {
      pair<int,int> entry = *it;
      
      // delete this entry
      this->lru.erase(it);

      // Push to the beginning
      this->lru.emplace(lru.begin(), make_pair(entry.first, entry.second));

      // return
      return entry.second;
    }
  }
  
  return -1;
}
    
void LRUCache::put(int key, int value) {
  int ret = this->get(key);

  if (ret == -1) {
    
    if(this->lru.size() >= this->capacity){
      // delete last element
      lru.erase(this->lru.end());
    }
    
    lru.emplace(this->lru.begin(), make_pair(key, value));
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
int main() {
  LRUCache cache( 2 );
  cache.put(1, 1);
  cache.put(2, 2);
  
  printf ("get(1) : %d\n",cache.get(1));       // returns 1

  cache.put(3, 3);    // evicts key 2
  //printf("...\n\n");
  printf("get(2): %d\n",cache.get(2));       // returns -1 (not found)
  //printf("...\n\n");
  cache.put(4, 4);    // evicts key 1
  printf ("get(1) : %d\n",cache.get(1));    // returns -1 (not found)
  printf ("get(3) : %d\n",cache.get(3));       // returns 3
  printf ("get(4) : %d\n",cache.get(4));       // returns 4

  return 0;
}
