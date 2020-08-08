# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    head = dummy
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        if curr1.data < curr2.data:
            head.next = curr1
            curr1 = curr1.next
        else:
            head.next = curr2
            curr2 = curr2.next
        head = head.next
    if curr1:
        head.next = curr1
    if curr2:
        head.next = curr2
    return dummy.next
