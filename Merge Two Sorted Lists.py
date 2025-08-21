# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

# ----------------------------
# Helper functions for testing
# ----------------------------

# Convert Python list -> Linked list
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Convert Linked list -> Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
# ----------------------------
# Testing
# ----------------------------
if __name__ == "__main__":
    # Example input
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    # Output
    print("Merged List:", linked_list_to_list(merged_head))
