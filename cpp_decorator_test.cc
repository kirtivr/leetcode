#include <utility>
#include <cstdio>

class Base {
public:
  int get_number() {
    return 3;
  }
};

template <typename U>
class Decorator : public U {
public:
  Decorator(U&& u) : U(u) {}

  int get_number() {
    // printf("U = %p\n", U);
    return U::get_number() + 5;
  }
};

int main() {
  auto b = Base();
  auto x = Decorator(std::move(b));
  printf("%d\n", x.get_number());
  return 0;
}
