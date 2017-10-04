from operator import attrgetter
import os

class ParsedFile:
    def __init__(self, path):
        self.path = path

    def get_name(self):
        return os.path.basename(self.path)

    def set_source(self, source):
        self.source = source

    def print(self):
        indent = "    "
        print(self.title)
        print(indent + self.author)
        print(indent + self.publication_idno)        
        print(indent + self.publisher)
        print(indent + self.year_published)


class ExplorationResult:
    def __init__(self):
        self.nodes = []

    def add_node(self, new_node):
        already_exists = False
        
        for node in self.nodes:
            if node.name == new_node.name:
                node.increase_count()
                already_exists = True

        if not already_exists:
            self.nodes.append(new_node) 

    def print(self, file):
        self.nodes.sort(key=attrgetter('depth', 'name', 'path'))
        
        for node in self.nodes:
            file.write("{}(count: {}; depth: {}; path: {})".format(node.name, node.count, node.depth, node.path))
            file.write("\n")
            node.print(file)


class Node:
    def __init__(self, name, depth, path):
        self.name = name
        self.depth = depth
        self.path = path
        self.count = 1
        self.subnodes = []

    def add_subnode(self, new_node):
        already_exists = False

        for subnode in self.subnodes:
            if subnode.name == new_node.name:
                subnode.increase_count()
                already_exists = True

        if not already_exists:
            self.subnodes.append(new_node)

    def increase_count(self):
        self.count = self.count + 1

    def print(self, file):
        self.subnodes.sort(key=attrgetter('name', 'count'))
        
        for subnode in self.subnodes:
            file.write("    {}({})".format(subnode.name, subnode.count))
            file.write("\n")

        file.write("\n")

class SubNode:
    def __init__(self, name):
        self.name = name
        self.count = 1

    def increase_count(self):
        self.count = self.count + 1
