class Node:
    """Represents a node in a tree data structure"""

    def __init__(self, data):
        self.children = []
        self.parent = None
        self.data = data

    def add_child(self, data):
        """Creates a new node with the given data and adds it to the list of children"""

        child = Node(data)
        child.parent = self
        self.children.append(child)
        return child

    def remove_child(self, data):
        """Removes all nodes from children that contain the given data"""

        self.children = [child for child in self.children if child.data != data]

    def check_children(self, data):
        """Checks if node exists in children with given data and returns child if true"""
        
        for c in self.children:
            if c.data == data:
                return c
        return None