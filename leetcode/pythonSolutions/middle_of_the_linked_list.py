'''

    This is the solution to the leetcode problem "876. Middle of the Linked List".
    In this file, I go in depth on the processes for the purpose of learning
    more about linked list operations and notation. The link to the problem
    is provided below:

    https://leetcode.com/problems/middle-of-the-linked-list/

'''

class Listnode:

    '''

        Creating the list node object, these objects are what make
        up a linked list, with each node containing a value as well
        as information for the next node.

    '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next - next

class Solution:

    def simple(self, head):

        '''

            This is my first solo solution to a linked list problem, though
            it is quite simple and most likely not the most effecient, I am
            still proud of it nonetheless as it shows growth.

            In the solution I have implemented, we simply find the size of the
            linked list and then perform floor division as it asks to include
            both middles given an even length. Then from there we iterate by
            the newly divided size until we reach the halfway point where we
            then return the rest of the linked list.

        '''

        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        curr = head
        for _ in range(size // 2):
            curr = curr.next
        return curr

    def pointer(self, head):

        '''

            In the pointer solution, we have two pointers: a fast and
            a slow. We can see in the first line they both start at
            the head (beginning) of the linked list, however they both
            iterate through the list at different speeds.

            The while loop essentially has the condition that as long
            as the node contains a value, continue the operation. Inside
            the loop, the slow pointer iterates by one, and the fast
            pointer iterates by two. Given this, the fast moves twice as
            fast so the slow must end up in the middle.

        '''

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
