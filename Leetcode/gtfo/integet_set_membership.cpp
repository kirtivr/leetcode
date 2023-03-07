#include <set>
#include <string>

/*
Given a set of integers S, output its predicate expression (or indicator expression), ids(S) as a string.

The expression must evaluate to True if x is a member of S and to False otherwise. for example, ind({1,2}) = "x == 1 or x == 2".

The expression can contain:

the variable: x
integer constants: [0-9]+
boolean constants: True, False
parentheses: ( and )
And the following operators, in decreasing precedence:

integer comparisons: <, <=, >, >=, ==, !=
logical not
logical and
logical or
Meaning that x==1 or x==2 is equivalent to (x==1) or (x==2), also X and Y or Z and W is equivalent to (X and Y) or (Z and W)

*/

std::string FindMinRepresentation(std::set<std::set<int>> disjunctive_sets) {
}

int DoBinarySearchFromLeftIndex(std::set<int> input, int start, int end) {
  int mid = start + (end - start) / 2;
  if (start == end) {
    return start;
  }
  if (mid - start == input[mid] - input[start]) {
    // Can we add more elements?
    auto rightmost = DoBinarySearchFromLeftIndex(input, mid, end);
    return rightmost;
  }
  return DoBinarySearchFromLeftIndex(input, start, mid - start);
}

std::set<std::pair<int, int>> FindClusters(std::set<int> input) {
  int current_idx = 0;
  std::set<std::set<int>> all_consecutive_sets;
  while (current_idx < input.size()) {
    int consecutive_limit = DoBinarySearchFromLeftIndex(input, current_idx, input.size() - 1);
    all_consecutive_sets.insert(std::make_pair(current_idx, consecutive_limit));
    current_idx = consecutive_limit + 1;
  }
  return all_consecutive_sets;
}

std::set<int> SortInputSet() {
  // You can assume the input set is sorted (?).
}

std::string ind(std::set<int> s) {
  std::set<std::pair<int, int>> all_consecutive_sets = FindClusters(s);
  std::string rep = "";
  for (int i = 1; i < all_consecutive_sets.size(); ++i) {
    if (all_consecutive_sets[i].first > all_consecutive_sets[i-1].second + 1) {
      rep = rep + all_consecutive_sets[i-1].first + " < x < " + all_consecutive_sets[i-1].second + " or ";
    } else {
      rep = rep + all_consecutive_sets[i-1].first + " < x < " + all_consecutive_sets[i].second + " and " + " x != " + all_consecutive_sets[i].first - 1 + " or ";
    }
  }
  return rep;
}

int main() {
  std::set<int> S = { 1,2,3,4,4 };
  // Types of integer sets.
  // All elements are not equal.
  // {1,2,3,5,8,12,16,21,27}
  // check if we have consecutive integers.
  // If we have consecutive integers, find the bounds and express that.

  // when will we use the NOT or the AND operator.
  // in general, is it possible to have a conjunctive or a disjunctive expression?
  // that implies that we need to compare X to two or more sets.
  // that would imply there are regula

  // Trivial solution is to have an OR of all the input set's distinct elements.
  int x = 3;
}
