# @Time    : 2018/9/19 下午9:11
# 根据一棵树的前序遍历与中序遍历构造二叉树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 优化思路，没次都把找到的根节点记录下来
class Solution:

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def help(left_begin, left_end, right_begin, right_end):
            if left_begin>left_end or right_begin>right_end:
                return
            root = TreeNode(preorder[left_begin])
            root_index = value_dict[preorder[left_begin]]

            print(root_index-right_begin)
            left_length=root_index-right_begin
            root.left = help(
                left_begin=left_begin + 1,
                left_end=left_begin+left_length,
                right_begin=right_begin,
                right_end=root_index-1
            )
            # key: right_begin will change
            #  left_length=root_index-right_begin
            # right_begin=left_begin+left_length+1
            root.right = help(
                left_begin=left_begin+left_length+1,
                left_end=right_end,
                right_begin=root_index+1,
                right_end=right_end,

            )
            return root

        value_dict = {each: index for index, each in enumerate(inorder)}
        return help(left_begin=0, left_end=len(preorder) - 1,
                    right_begin=0, right_end=len(inorder) - 1
                    )


if __name__ == '__main__':
    class_a = Solution()
    pre_order = [4,1,2,3]
    in_order = [1,2,3,4]
    root = class_a.buildTree(pre_order, in_order)
    print(root.val)
