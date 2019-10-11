#!/proj/olympus/work/sw/hware/tools/centos-7/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            curr = self.head
            while (curr.next is not None):
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr
            self.length += 1


    def addAtIndex(self, val, index):
        if self.head is None or index <= 0:
            self.addAtHead(val)
        elif index >= self.length:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            curr = self.head
            count = 0
            while (count < (index-1)):
                curr = curr.next
                count  = count + 1

            new_node.next = curr.next
            curr.next.prev = new_node
            new_node.prev = curr
            curr.next = new_node
            self.length += 1

    def deleteFromIndex(self, index):
        if self.head is None or index < 0 or index > self.length:
            return

        if index == 0:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            count = 0
            curr = self.head
            while count < (index-1):
                curr = curr.next
                count += 1

            curr.next = curr.next.next
            curr.next.prev = curr


    def printList(self):
        if self.head is None:
            return

        curr = self.head
        vals = []
        while (curr is not None):
            vals.append(curr.data)
            curr = curr.next

        print vals




if __name__ == '__main__':
    ll = MyLinkedList()

    ll.addAtHead(3)
    ll.addAtHead(2)
    ll.addAtHead(1)
    ll.addAtTail(4)
    ll.addAtTail(5)
    ll.printList()

