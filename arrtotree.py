arr = [-10, -3, 0, 5, 9]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid)
        node.right = self.helper(nums, mid + 1, right)
        return node

    def move_around_tree(self, root):
        if root is None:
            return

        print(root.val)
        self.move_around_tree(root.left)
        self.move_around_tree(root.right)

s = Solution()
print(s.move_around_tree(s.sortedArrayToBST(arr)))