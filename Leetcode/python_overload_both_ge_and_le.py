from typing import List, Optional, Tuple, Dict
import pdb
from functools import cmp_to_key
import time

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

class Ingredient():
    def __init__(self, name):
        self.name = name
        self.uses = []
        self.creates = []

    def __str__(self):
        print(f'{self.name} uses: {self.uses} creates: {self.creates}')

    def __repr__(self):
        return f'{self.name} creates: {self.creates}'

    def __lt__(self, other):
        print(f'compare {self.name} oth = {other.name}')
        if self.name in other.uses:
            print(f'{self.name} less than {other.name}')
            return True
        if other.name in self.creates:
            print(f'{self.name} less than {other.name}')
            return True
        print(f'out {other.name} less than {self.name}')
        return False

class Solution:
    def connectionsGraph(self, recipes: List[str], ingredients: List[List[str]]):
        graph = {}
        for r_idx in range(len(recipes)):
            recipe_name = recipes[r_idx]
            recipe = None
            if recipe_name in ingredients:
                recipe = ingredients[recipe_name]
            else:
                recipe = Ingredient(recipe_name)
                graph[recipe_name] = recipe

            for ingredient_name in ingredients[r_idx]:
                if ingredient_name in graph:
                    ingredient = graph[ingredient_name]
                else:
                    ingredient = Ingredient(ingredient_name)
                    graph[ingredient_name] = ingredient
                ingredient.creates.append(recipe)
                recipe.uses.append(ingredient)

        return graph

    def getTopologicalOrdering(self, graph: Dict[str, Ingredient]):
        ordering = [ingredient for key, ingredient in graph.items()]
        print(f'original ordering = {ordering}')
        for element_to_sort_idx in range(len(ordering)):
            for j in range(element_to_sort_idx + 1, len(ordering)):
                element = ordering[element_to_sort_idx]
                if element > ordering[j]:
                    print(f'exchange {element} and {ordering[j]}')
                    temp = ordering[j]
                    ordering[j] = element
                    ordering[element_to_sort_idx] = temp

        return ordering
            
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        connections = self.connectionsGraph(recipes, ingredients)
        #print(connections)
        print(self.getTopologicalOrdering(connections))

if __name__ == '__main__':
    x = Solution()
    start = time.time()
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    print(x.findAllRecipes(recipes, ingredients, supplies))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')