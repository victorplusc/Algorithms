# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    slow = head
    fast = head
    for i in range(positionFromTail):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow.data
