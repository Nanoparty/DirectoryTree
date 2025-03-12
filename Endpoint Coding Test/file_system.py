from node import Node


class FileSystem:
    """
    A simple file system representation with a tree data structure backing.
    Contains functions for the operations of creating files, moving files, deleting files and viewing files.
    """

    def __init__(self):
        self.root = Node("root")

    def add_directory(self, directory_name):
        """
        Adds a new file to the system with the given directory name.
        Function will create new parent directories as needed.
        Given directories cannot already exist in the system
        """

        tokens = directory_name.split("/")

        if len(tokens) == 1:
            if self.root.check_children(directory_name) is None:
                self.root.add_child(directory_name)
            else:
                print("Directory already exists")
            return

        parent = self.get_parent_directory(self.root, tokens[:-1])

        if parent is None:
            parent = self.create_directories(self.root, tokens[:-1])
        
        if parent.check_children(tokens[-1]) is None:
            parent.add_child(tokens[-1])
        else:
            print("Directory already exists")

    def list_directories(self):
        """Outputs a heirarchical visualization of the current file system"""

        self.preorder_traversal(self.root, -1)

    def move_directory(self, source, target):
        """
        Moves a given source directory into a given target directory.
        Source directory must already exist in file system.
        Target directory will be created if it does not already exist.
        """

        source_tokens = source.split("/")
        source_parent = None

        if len(source_tokens) == 1:
            source_parent = self.root if self.root.check_children(source) is not None else None
        else:
            source_parent = self.get_parent_directory(self.root, source_tokens[:-1])

        if source_parent is None:
            print("Source directory does not exist.")
            return

        source_node = source_parent.check_children(source_tokens[-1])

        if source_node is None:
            print("Source directory does not exist")
            return

        target_tokens = target.split("/")
        target_parent = None

        if len(target_tokens) == 1:
            if (self.root.check_children(target_tokens[0])) is None:
                target_parent = self.root.add_child(target_tokens[0])
            else:
                target_parent = self.root.check_children(target_tokens[0])
        else:
            target_parent = self.create_directories(self.root, target_tokens)

        copy = target_parent.add_child(source_node.data)
        copy.children = source_node.children
        
        source_parent.remove_child(source_node.data)

    def delete_directory(self, directory):
        """
        Removes a given file directory from the file system.
        Directory must currently exist in the system.
        """
        tokens = directory.split("/")

        if len(tokens) == 1:
            if self.root.check_children(directory) is not None:
                self.root.remove_child(directory)
            else:
                print("Directory does not exist")
            return

        parent = self.get_parent_directory(self.root, tokens[:-1])
        if parent is not None:
            parent.remove_child(tokens[-1])
        else:
            print("Directory does not exist.")

    def get_parent_directory(self, node, tokens):
        """
        Returns the directory node of the given directory path in the form of tokens.
        Each token represents a node in the directory path.
        Used to help find the parent node of a deeply nested directory.
        """

        parent = node.check_children(tokens[0])

        if len(tokens) == 1:
            return parent

        if parent is not None:
            return self.get_parent_directory(parent, tokens[1:])
        else:
            return None

    def create_directories(self, node, tokens):
        """
        Creates directory tree from given list of tokens if directories do not currently exist.
        Used to create new parent directories when adding a deeply nested directory.
        """

        if len(tokens) == 1:
            child = node.check_children(tokens[0])
            if child:
                return child
            else:
                return node.add_child(tokens[0])

        child = node.check_children(tokens[0])
        if child is None:
            child = node.add_child(tokens[0])

        return self.create_directories(child, tokens[1:])

    def preorder_traversal(self, node, depth):
        """Performs a preorder traversal of the nodes in the file system and outputs their data."""

        if node is None:
            return

        if depth >= 0:
            indentation = "\t" * depth
            print(indentation + node.data)
        
        for child in node.children:
            self.preorder_traversal(child, depth + 1)




