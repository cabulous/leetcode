from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        array1 = self.tree_to_array(root1)
        array2 = self.tree_to_array(root2)

        for num in array1:
            complement = target - num
            if complement in array2:
                return True

        return False

    def tree_to_array(self, node: Optional[TreeNode]) -> List[int]:
        return [node.val] + self.tree_to_array(node.left) + self.tree_to_array(node.right) if node else []
