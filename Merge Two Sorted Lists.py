# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)   # Create a dummy node as a fake start
        current = dummy        # Pointer 'current' starts at dummy

        # Traverse both lists while they are not empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1   # Attach list1 node to the merged list
                list1 = list1.next     # Move list1 pointer forward
            else:
                current.next = list2   # Attach list2 node to the merged list
                list2 = list2.next     # Move list2 pointer forward

            current = current.next     # Move the current pointer to the end

        # Attach the remaining nodes of whichever list is not empty
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next   # Return the merged list starting after dummy

# ----------------------------
# Helper functions for testing
# ----------------------------

# Convert Python list -> Linked list
# def build_linked_list(values):
#     dummy = ListNode()
#     current = dummy
#     for val in values:
#         current.next = ListNode(val)
#         current = current.next
#     return dummy.next

# # Convert Linked list -> Python list
# def linked_list_to_list(head):
#     result = []
#     while head:
#         result.append(head.val)
#         head = head.next
#     return result
# ----------------------------
# Testing
# ----------------------------
if __name__ == "__main__":
    # Example input
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    # Output
    print("Merged List:", linked_list_to_list(merged_head))
