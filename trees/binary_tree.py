#!/proj/olympus/work/sw/hware/tools/centos-7/bin/python

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, node, val):
        if val <= node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert_node(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert_node(node.right, val)

    def print_tree(self, mode='inorder'):
        if self.root is None:
            return
        else:
            if mode == 'inorder':
                self.print_inorder(self.root)
            elif mode == 'preorder':
                self.print_preorder(self.root)
            elif mode == 'postorder':
                self.print_postorder(self.root)
            else:
                print "Bad traversal option"
                return

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print node.val
            self.print_inorder(node.right)

    def print_preorder(self, node):
        if node:
            print node.val
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print node.val


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(27)
    bst.insert(14)
    bst.insert(10)
    bst.insert(19)
    bst.insert(35)
    bst.insert(31)
    bst.insert(42)

    bst.print_tree(mode='postorder')





