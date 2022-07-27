'''

    My First Singly Linked List

    This program is the basic singly linked list data structure.
    This program contains a singly linked list that has been heavily
    annotated for studying purposes.

    Before attempting to understand linked lists, it may help to
    first learn about Object Oriented Programming (OOP).

    This code comes from leetcode (This may require subscription):

    https://leetcode.com/problems/design-linked-list/solution/

'''

class ListNode:

    # Initiailzing the List Node object
    def __init__(self,x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        '''

            Creates the linked list with an initial length
            (size) of zero. Includes a sentinel node for the
            purpose of making operations easier, specifically
            insert and delete.

        '''
        self.size = 0
        self.head = ListNode(0) # Noting that the size is still zero, this node technically doesn't exist

    def get(self, index: int) -> int:
        '''

            Gets the value at the i-th index in the linked list.
            It first checks for the validity of the index, if
            the index is indeed valid, it will continue, otherwise,
            it will return -1. It then iterates through the nodes
            until it has reached the index of the desired node, in
            which it finally returns the value stored at the index.

            We iterate to a range "index + 1" due to the sentinel node.

        '''
        if index < 0 or index >= self.size: # If index is valid
            return -1

        curr = self.head
        # Iterating process; Index + 1 because of sentinel node
        for _ in range(index + 1):
            curr = curr.next
        return curr.val


    '''

        The addAtHead and addAtTail functions are relatively self
        explanatory and do not hold any operation besides calling
        the add at index function, thus they will be skipped over

    '''
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        '''

            This function adds a node at the desired index. First,
            the index itself is checked: If the index is larger
            than the size of the list, do nothing, if the index is
            less than zero, add it to the front. To account for the
            increase in size of the list, we add 1 to the size.
            We then search for the predecessor node by iterating through
            the list until we reach the desired index. We then
            initialize a node with a user given value and call it
            "to_add". We then do the insertion process in which we
            set the next value of the new node to the predecessor's
            next value and the predecessor's next value to the new node.

        '''
        if index > self.size:
            return

        # If negative index, node will be inserted at head of list
        if index < 0:
            index = 0

        self.size += 1

        pred = self.head
        # Iterating process
        for _ in range(index):
            pred = pred.next

        # The node to be added
        to_add = ListNode(val)

        # The insertion process
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        '''

            This function deletes a node at a given index.
            It first checks for the validity of the index;
            if the desired index doesn't exist, the operation
            cannot be completed, thus it'll do nothing.
            To account for the deletion of a node, the list
            size will go down by one. A similar iteration
            process is conducted to reach the desired index
            followed by a very simply deletion process. To
            delete the node at the given index, simply set
            the predecessor's next value to the node that is
            two spaces over.

        '''
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        pred = self.head
        # Iterating to desired index
        for _ in range(index):
            pred = pred.next

        # Deletion process
        pred.next = pred.next.next
