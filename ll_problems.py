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
            print "No List"
            return

        curr = self.head
        vals = []
        while (curr is not None):
            vals.append(curr.data)
            curr = curr.next

        print vals


def merge_lists(list1, list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1

    list3 = MyLinkedList()
    curr1 = list1.head
    curr2 = list2.head
    while (1):
        if curr1 is None:
            while curr2 is not None:
                list3.addAtTail(curr2.data)
                curr2 = curr2.next
            break
        elif curr2 is None:
            while curr1 is not None:
                list3.addAtTail(curr1.data)
                curr1 = curr1.next
            break
        elif curr1.data <= curr2.data:
            list3.addAtTail(curr1.data)
            curr1 = curr1.next
        elif curr2.data < curr1.data:
            list3.addAtTail(curr2.data)
            curr2 = curr2.next

    return list3


def add_lists(list1, list2):
    add_sum = 0
    add_carry = 0

    curr1 = list1.head
    curr2 = list2.head

    lsum = MyLinkedList()
    while(1):
        if curr1 is None and curr2 is None:
            break
        elif curr1 is None:
            while curr2 is not None:
                this_sum = add_carry + curr2.data
                add_carry = this_sum/10
                lsum.addAtTail(this_sum%10)
                curr2 = curr2.next
            break
        elif curr2 is None:
            while curr1 is not None:
                this_sum = add_carry + curr1.data
                add_carry = this_sum/10
                lsum.addAtTail(this_sum%10)
                curr1 = curr1.next
            break
        else:
            this_sum = add_carry + curr1.data + curr2.data
            add_carry = this_sum/10
            lsum.addAtTail(this_sum%10)
            curr1 = curr1.next
            curr2 = curr2.next

    if add_carry:
        lsum.addAtTail(add_carry)


    lsum.printList()





if __name__ == '__main__':

    ll1 = MyLinkedList()
    ll1.addAtTail(1)
    ll1.addAtTail(2)
    ll1.addAtTail(3)

    ll1.printList()

    ll2 = MyLinkedList()
    ll2.addAtTail(9)
    ll2.addAtTail(9)
    ll2.addAtTail(9)
    ll2.addAtTail(9)

    ll2.printList()

    # merge_lists(ll1, ll2)
    add_lists(ll1, ll2)



