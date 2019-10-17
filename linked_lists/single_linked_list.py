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


    def removeNthFromEnd(self, n):
        """
        :type n: int
        :rtype: ListNode
        """
        slow = self.head
        fast = self.head

        while(n>0):
            fast = fast.next
            n = n-1

        if fast is None:
            return self.head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        if slow.next is not None:
            slow.next = slow.next.next
        else:
            slow.next = None

        self.length -= 1


    def printList(self):
        """
        Print contents of the list from head
        :rtype None
        """
        vals = []
        curr = self.head
        while curr != None:
            vals.append(curr.data)
            curr = curr.next
        print vals


    def reverseList(self):
        """
        Reverse a list
        """

        curr = self.head
        prev_node = None
        next_node = None

        if self.length == 0:
            return
        elif self.length == 1:
            return

        while curr is not None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head = prev_node


    def removeElements(self, val):
        """
        :type val: int
        """

        found = False

        while self.head and self.head.data == val:
            self.head = self.head.next

        if self.head == None:
            return
        else:
            curr = self.head
            while curr is not None:
                if curr.next is not None:
                    if curr.next.data == val:
                        curr.next = curr.next.next
                        found = True
                    else:
                        curr = curr.next
                else:
                    curr = curr.next

        if found:
            self.length -= 1


    def oddEvenList(self):
        """
        Maintain 2 lists - odd and even. Build both independently
        and connect both lists in the end
        """

        if self.head is None:
            return

        odd = self.head
        even = self.head.next
        even_first = even

        if self.head.next is None:
            even_first = None
            odd.next = even_first
        else:
            while(1):
                if (odd is None or even is None or even.next is None):
                    odd.next = even_first
                    break

                odd.next = even.next
                odd = even.next

                if odd.next is None:
                    even.next = None
                    odd.next = even_first
                    break

                even.next = odd.next
                even = odd.next


    def checkPalindrome(self):
        """
        Check if a string is palindrome
        2 ways -
            1. Traverse list once and put it in stack. Pop each element from stacka nd compare data
            2. Keep a copy of reversed list and then check element by element
        """

        if self.head is None:
            return False

        if self.head.next is None:
            return True

        curr = self.head
        vals = []
        while(curr is not None):
            vals.append(curr.data)
            curr = curr.next

        idx = 0
        num = len(vals)
        is_palindrome = True
        while idx < (num/2):
            if vals[idx] != vals[num-idx-1]:
                is_palindrome = False
            idx += 1

        return is_palindrome


    def swapPairs(self):
        """
        Given a linked list, swap every two adjacent nodes and return its head.
        """
        if self.head is None:
            return
        if self.head.next is None:
            return

        curr = self.head
        while (curr is not None):
            if (curr.next is not None):
                curr_next = curr.next
                tmp = curr.data
                curr.data = curr_next.data
                curr_next.data = tmp
                curr = curr_next.next
            else:
                curr = curr.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

ll = MyLinkedList()
ll.addAtTail(1)
ll.addAtTail(2)
ll.addAtTail(3)
ll.addAtTail(4)
ll.addAtTail(5)
# ll.addAtTail(6)

ll.printList()

ll.swapPairs()
ll.printList()
