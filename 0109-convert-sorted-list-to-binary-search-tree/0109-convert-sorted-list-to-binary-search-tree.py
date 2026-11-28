# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        current = head

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal current

            if left > right:
                return None

            mid = (left + right + 1) // 2

            left_child = build(left, mid - 1)

            root = TreeNode(current.val)
            current = current.next
            root.left = left_child

            root.right = build(mid + 1, right)

            return root

        return build(0, size - 1)