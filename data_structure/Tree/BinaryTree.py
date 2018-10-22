class TreeNode:

    def __init__(self,value=-1,left=None,right=None):
        self.left=left
        self.right=right
        self.value=value

class Tree:
    def __init__(self,root):
        self.root=root

    def insert_into_left(self,value):
        child_node=TreeNode(value)
        if not self.root:
            self.root=child_node
            # 左节点为空
        if not self.root.left:
            self.root.left=child_node
        else:
            child_node.left=self.root.left
            self.root.left=child_node

    def insert_into_right(self,value):
        child_node=TreeNode(value)
        if not self.root:
            self.root=child_node

        if not self.root.right:
            self.root.right=child_node
        else:
            child_node.right=self.root.right
            self.root.right=child_node

    def get_right_node(self):
        if not self.root or self.root.right:
            return None
        return self.root.right.value

    # 先序遍历 根左右
    def pre_order(self,node):
        if not node:
            return
        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    # 中序遍历
    def mid_order(self,node):
        if not node:
            return
        self.mid_order(node.left)
        print(node.value)
        self.mid_order(node.right)

    # 后序遍历
    def last_order(self,node):
        if not node:
            return
        self.last_order(node.left)
        self.last_order(node.right)
        print(node.value)

    # 层序遍历
    def level_order(self):
        
        pass



    def outPut(self):
        temp=self.root
        while temp.left:
            print(temp.value)
            temp=temp.left
        print('right-----')
        temp=self.root
        while temp.right:
            print(temp.value)
            temp=temp.right


if __name__ == '__main__':
     root=TreeNode(value=0)
     tree=Tree(root)
     for i in range(1,10):
        tree.insert_into_left(i)

     for i in range(10,20):
        tree.insert_into_right(i)

     # tree.outPut()
     tree.pre_order(root)
     print('*'*20)
     tree.mid_order(root)
     print('*'*20)
     tree.last_order(root)
     print('*'*20)






