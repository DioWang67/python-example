#!usr/bin/python3
# -*- coding:UTF-8 -*-

# 21.leetcode题目讲解（Python）：合并两个有序链表

import sys
import time

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1 is None and l2 is None:
#             return None
#         elif l1 is not None and l2 is None:
#             return l1
#         elif l2 is not None and l1 is None:
#             return l2

#         l = []
#         while l1 is not None:
#             l.append(l1.val)
#             l1 = l1.next
#         while l2 is not None:
#             l.append(l2.val)
#             l2 = l2.next
#         print(l)
#         l = sorted(l)
#         print(l)
#         new_l = ListNode(l[0])
#         head_l = new_l
#         for i in range(1,len(l)):
#             new_l.next = ListNode(l[i])
#             new_l = new_l.next
#         new_l.next = None
#         print(list(head_l))
#         return head_l
  


# s=Solution()
# l1=ListNode(input("l1="))
# l2=ListNode(input("l2="))
# l1 = [1, 2, 4,7,8,9]
# l1=iter(l1)
# l2=[1, 3, 4]

# listnode=ListNode(l1)
# l2=iter(l2)
# # print(list11)
# print(list(list11))

# print(s.mergeTwoLists(l1,l2))

####################################################


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
 
# myclass = MyNumbers()
# myiter = iter(myclass)
 
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

###################################################

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self,data):
        self.head = ListNode(data[0])
        r = self.head
        p = self.head

        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self,head):
        if head == None: return
        node = head
        while node != None:
            print(node.val,end='')
            node = node.next

class Solution:
    def mergeTwoList(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next

            else:
                head.next = l2
                l2= l2.next
            head = head.next
        if l1 != None:
            head.next = l1
        elif l2 != None:
            head.next = l2
        return first.next

if __name__ == '__main__':
    a =Solution()
    l = LinkList()
    data1 = [1,2,3,4]
    data2 = [2,4,6]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    l.printlist(l1)
    print("\r")
    l.printlist(l2)
    print("\r")
    m = a.mergeTwoList(l1,l2)
    l.printlist(m)