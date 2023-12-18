# #!usr/bin/python
# # -*- coding:UTF-8 -*-




# # 19.leetcode题目讲解（Python）：删除链表的倒数第N个节点



# from re import M


# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """

#         node_list = []
#         node_list = iter(node_list)
#         while head:
#             node_list.append(head)
#             if next(head) is None:
#                 break
#             else:
#                 head = next(head)

#         if len(node_list) == 1:
#             return None

#         elif len(node_list) == n:
#             node_list.pop(0)
#             return node_list[0]

#         n = 0 - n
#         node_list[n - 1].next = node_list[n].next
#         node_list.pop(n)
#         return node_list[0]
# s=Solution()
# head=list(map(int, input("input:").split()))

# M=input("N=")
# n = int(M)
# print(s.removeNthFromEnd(head,n))



####gpt
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)  # 哑節點
    dummy.next = head
    first = dummy
    second = dummy

    # 將第一個指針向前移動 N+1 步
    for i in range(n + 1):
        first = first.next


    # 同時移動兩個指針，直到第一個指針到達末尾
    while first is not None:
        first = first.next
        second = second.next

    # 此時第二個指針的下一個節點就是要移除的節點
    second.next = second.next.next

    return dummy.next  # 返回新的鏈表

# 創建一個示例鏈表：1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 移除倒數第二個節點
new_head = removeNthFromEnd(head, 1)

# 輸出新的鏈表
current = new_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")
