from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        
    def addContent(self, new_content):
        self.content += new_content

    def readContent(self):
        return self.content

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.nodes = {}
        self.files = {}

    def list_everything(self):
        everything = []
        for node in self.nodes.keys():
            everything.append(node)
        for file in self.files:
            everything.append(file)
            
        return sorted(everything)

    def list_specific(self, path):
        if path in self.nodes.keys():
            return self.nodes[path].list_everything()
        elif path in self.files.keys():
            return [path]
        return []

    def get_to_node(self, path):
        #pdb.set_trace()
        fl_path_idx = path.find('/')
        node = self

        while fl_path_idx != -1:
            fl_path = path[:fl_path_idx]
            if fl_path not in node.nodes:
                break
            node = node.nodes[fl_path]
            path = path[fl_path_idx + 1 :]
            fl_path_idx = path.find('/')

        #print(f'node: {node} path: {path}')
        # Now we have the actual node referred to.
        if path == '':
            return node
        elif path in node.nodes:
            return node.nodes[path]
        elif path in node.files:
            return node.files[path]
        else:
            return node

    def list(self, path):
        #print(f'path = {path}')
        node = self.get_to_node(path)
        if isinstance(node, File):
            return [node.name]
        else:
            return node.list_everything()
    
    def make_directory(self, path):
        self.nodes[path] = TreeNode(path)
        return self.nodes[path]        

    def add_next_and_propagate(self, first_path, remaining_path):
        #print(f'first path = {first_path} remaining = {remaining_path}')
        next_node = self.make_directory(first_path)
        next_node.make_directories(remaining_path)

    def make_directories(self, path):
        #pdb.set_trace()
        first_level_path_idx = path.find('/')
        if first_level_path_idx == -1:
            if path == '':
                return
            else:
                self.add_next_and_propagate(path, '')
                return

        first_level_path = path[:first_level_path_idx]
        if first_level_path == '':
            # Nothing to make.
            return
        if first_level_path in self.nodes:
            return self.nodes[first_level_path].make_directories(path[first_level_path_idx + 1 :])
        else:
            self.add_next_and_propagate(path[:first_level_path_idx], path[first_level_path_idx + 1:] if len(path) > first_level_path_idx else '')

    def add_content_to_file(self, filePath: str, content: str) -> None:
        file = self.get_to_node(filePath)
        if isinstance(file, File):
            file.addContent(content)
        else:
            last_dir = filePath.rfind('/')
            filep = filePath[last_dir + 1 :]
            file.files[filep] = File(filep, content)
        #print(file)

    def read_content_from_file(self, filePath: str) -> None:
        file = self.get_to_node(filePath)
        return file.readContent()

    def __repr__(self):
        return f'node: {self.name} files: {self.files} nodes: {self.nodes}'

class FileSystem:
    def __init__(self):
        self.root = TreeNode('/')

    def ls(self, path: str) -> List[str]:
        path = path[1:]
        return self.root.list(path)

    def mkdir(self, path: str) -> None:
        path = path[1:]
        self.root.make_directories(path)     

    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath = filePath[1:]
        self.root.add_content_to_file(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        filePath = filePath[1:]
        return self.root.read_content_from_file(filePath)

if __name__ == '__main__':
    start = time.time()
    x = FileSystem()
    with open('588_tc.text', 'r') as f:
        cmds = ast.literal_eval(f.readline())
        cmds = cmds[1:]
        args = ast.literal_eval(f.readline())
        args = args[1:]

        for idx, cmd in enumerate(cmds):
            print('--------------------------------------------------------------')
            print(cmd)
            print(f'args : {args[idx]}')
            if cmd == "ls":
                print(x.ls(args[idx][0]))
            elif cmd == "mkdir":
                print(x.mkdir(args[idx][0]))
            elif cmd == "addContentToFile":
                print(x.addContentToFile(args[idx][0], args[idx][1]))
            elif cmd == "readContentFromFile":
                print(x.readContentFromFile(args[idx][0]))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')