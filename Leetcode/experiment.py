from typing import List, Optional, Tuple
import time

def IterateThroughListWhileDeletingElements(words: List[str]):
    for i in range(len(words)):
        print(f"i = {i} length of words = {words} words[i] = {words[i]}")
        print(words.pop())
    return

def IterateThroughListWhileModifyingIteratedElement(words: List[str]):
    for i in range(len(words)):
        print(f"i = {i} len = {len(words)}")
        i += 2
    return

if __name__ == '__main__':
    start = time.time()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    IterateThroughListWhileDeletingElements(tasks)
    tasks = ["A","A","A","B","B","B"]
    IterateThroughListWhileModifyingIteratedElement(tasks)
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')