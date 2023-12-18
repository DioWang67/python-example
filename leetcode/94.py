from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res

if __name__ == "__main__":
    # 創建一個二叉樹
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))

    # 創建 Solution 的實例
    s = Solution()

    # 呼叫 inorderTraversal 方法
    result = s.inorderTraversal(root)

    # 輸出結果
    print(result)




# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# def find_nth_node(head, n):
#     current = head
#     for _ in range(n-1):
#         if current is None:
#             return None  # 鏈表長度小於n
#         current = current.next
#     return current

# # 創建鏈表 1 -> 2 -> 3 -> ... -> 20
# head = ListNode(1)
# current = head
# for i in range(2, 21):
#     current.next = ListNode(i)
#     current = current.next

# # 找到第15個節點
# nth_node = find_nth_node(head, 15)

# if nth_node is not None:
#     print(f"The value of the 15th node is: {nth_node.value}")
# else:
#     print("The linked list is shorter than 15 nodes.")
