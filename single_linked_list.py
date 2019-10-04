#!/proj/olympus/work/sw/hware/tools/centos-7/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 0
        curr = self.head
        if index < 0 or self.head == None or index >= self.length:
            return -1
        elif index == 0:
            return self.head.data
        else:
            while (count < index):
                if curr == None:
                    return -1
                count = count + 1
                curr = curr.next
            return curr.data

    def addAtHead(self, data):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, data):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.addAtHead(data)
        else:
            curr = self.head
            new_node = Node(data)
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
        else:
            if index > self.length:
                return
            elif index == self.length:
                self.addAtTail(val)
            else:
                new_node = Node(val)
                curr = self.head
                count = 0
                while count < index-1:
                    curr = curr.next
                    count +=1
                new_node.next = curr.next
                curr.next = new_node
                self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or self.head is None or index >= self.length:
            return
        elif index == 0:
            curr = self.head.next
            self.head = curr
            self.length -= 1
        else:
            curr = self.head
            count = 0
            while count < (index-1):
                curr = curr.next
                count += 1
            curr.next = curr.next.next
            self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
