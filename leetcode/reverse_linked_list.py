'''

    This is the solution to the leetcode problem "206. Reverse Linked List".
    In this file, I go in depth on the processes for the purpose of learning
    more about recursion and linked list operations. The link to the problem
    is provided below:

    https://leetcode.com/problems/reverse-linked-list/

'''


class ListNode:

    '''

        This is simply the creation of the list node. A list node
        is an object that makes up a linked list, with each node
        storing a value as well as a pointer to the next node.

    '''

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:

    def iterative(self, head):
        '''

            In the iterative solution, we simply iterate through each node
            and reassign the next value to that of the pervious value.

            In the reassignment process, we create a next_temp variable which
            serves the purpose of a placeholder, allowing us to iterate to the
            next node as the curr variable's next attribute is already being
            modified.

            'while curr' explained:
            In python, certain values hold a "truthiness"; any value other zero
            will equate to True, on the other hand if the value is zero or None,
            it will equate to False. You can test this out in the terminal or
            uncomment the line print(bool(curr))

        '''
        curr, prev = head, None

        # Reassignment process
        while curr:
            #print(bool(curr))

            next_temp = curr.next
            curr.next = prev

            prev = curr
            curr = next_temp

        return prev

    def recursive(self, head):
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
