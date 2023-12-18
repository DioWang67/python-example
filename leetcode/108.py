class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def sortedArrayToBST(self, nums):
#         def build(left, right):
#             if left > right:
#                 return 
#             mid = left + (right - left) // 2
#             # print(mid)
#             root = TreeNode(nums[mid])
#             root.left = build(left, mid - 1)
#             root.right = build(mid + 1, right)
#             print(root)
#             return root

#         # print(build(left,right))
#         return build(0, len(nums) - 1)

####################################################################

# class TreeNode:
#     def __init__(self,value):
#         self.children = []
#         self.value = value
 
#     def add_child(self,*child):
#         self.children+=child
 
#     def show(self,layer):
#         print  (""*layer+self.value)
#         map(lambda child:child.show(layer+1),self.children)
 
 
# def main():
#     a1 = TreeNode("A-1")
#     b1 = TreeNode("B-1")
#     b2 = TreeNode("B-2")
#     c1 = TreeNode("C-1")
#     d1 = TreeNode("D-1")
#     a1.add_child(b1,b2)
#     b1.add_child(c1,TreeNode("C-2"))
#     b2.add_child(TreeNode("C-3"),TreeNode("C-4"))
#     c1.add_child(d1)
#     d1.add_child(TreeNode("E-1"),TreeNode("E-2"))
#     a1.show(0)









class Solution:
    def sortedArrayToBST(self, nums):
        # Base condition...
        if len(nums) == 0:
            return None
        # set the middle node...
        mid = len(nums)//2
        print(mid)
        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # Assign left subtrees as the same function called on left subranges...
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign right subtrees as the same function called on right subranges...
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # Return the root node...
        return root

if __name__== '__main__':

    nums = [1,3,5,6,7,8,10,14,16,19]




    s = Solution()
    print(s.sortedArrayToBST(nums))




##################################################################################



# class treeNode:

#     def __init__(self, val):
#         # 初始化節點
#         self.val = val
#         self.left = None
#         self.right = None

#     def insertLeft(self, val):
#         # 如果要新增左邊節點，先檢查是否已存在，若左節點不存在則放入左節點
#         if self.left == None:
#             self.left = treeNode(val)
#         # 如果左節點已經存在，則放入左節點的下一層左節點，這邊用遞迴的方式進行搜尋，直到可以讓入左節點為止
#         else:
#             self.left.insertLeft(val)
    
#     def insertRight(self, val):
#          # 新增右邊節點的方式則和新增左節點的方式相同
#         if self.right == None:
#             self.right = treeNode(val)
#         else:
#             self.right.insertRight(val)

# # 執行方式
# sampleTree = treeNode(5)
# sampleTree.insertRight(7)
# sampleTree.insertRight(8)
# sampleTree.insertLeft(3)
# sampleTree.insertLeft(2)
# sampleTree.right.insertLeft(6)
# sampleTree.left.insertRight(4)


############################################################

def show(TreeNode: TreeNode):
    """
    友好的打印tree_node格式
    :param tree_node: 
    :return: 
    """
    # 广度优先遍历值
    ls = [TreeNode]
    pre_ls = []
    data = [[TreeNode.val]]
    while ls:
        cur = ls.pop(0)
        if not ls:
            data.append([])
            ls.extend(pre_ls)
        data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])
        pre_ls.extend([cur.left, cur.right])
    data.append([])
    while pre_ls:
        cur = pre_ls.pop(0)
        data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])

    # 阶梯序数
    span_list = []
    for i in range(len(data)):
        if span_list:
            span_list.append(span_list[-1] * 2 + 1)
        else:
            span_list.append(1)

    # 最合适的span长度
    span = 0
    for line_idx, val_list in enumerate(data):
        formatted_val_list = []
        for i, val in enumerate(val_list):
            str_val = str(val) if val is not None else ""
            span = span if span >= len(str_val) else len(str_val)
            if line_idx == 0:
                formatted_val_list.append(str_val)
            else:
                formatted_val_list.append(str_val)
        data[line_idx] = formatted_val_list
    c_span = span + 2

    # 格式化
    char_val_print_list = []
    formatted_val_print_list = []
    for line_idx, formatted_val_list in enumerate(data):
        char_val_list = [''] * len(formatted_val_list)
        for i, formatted_val in enumerate(formatted_val_list):
            two_space_formatted_val = ' ' * c_span if not formatted_val else ' ' + formatted_val + ' '
            formatted_val_list[i] = two_space_formatted_val
            if formatted_val:
                if i % 2 == 0:
                    # 左侧节点
                    char = ' ' * (len(two_space_formatted_val) - 1) + '/'
                else:
                    # 右侧节点
                    char = '\\' + ' ' * (len(two_space_formatted_val) - 1)
                char_val_list[i] = char
            else:
                char_val_list[i] = ' ' * c_span
        if line_idx != 0:
            char_val_print_list.append(char_val_list)
        formatted_val_print_list.append(formatted_val_list)

    # 打印
    center_length = span_list[-1] * c_span
    for line_idx, formatted_val_list in enumerate(formatted_val_print_list):
        num = span_list[-1 * line_idx - 1]
        mid_span = " " * (c_span * num)
        formatted_val_str = mid_span.join(formatted_val_list)
        print(formatted_val_str.center(center_length, " "))
        if line_idx < len(char_val_print_list):
            num = span_list[-1 * line_idx - 1 - 1]
            mid_span = " " * c_span * num
            char_val_str = mid_span.join(char_val_print_list[line_idx])
            print(char_val_str.center(center_length, " "))

