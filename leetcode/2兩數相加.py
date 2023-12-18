#!usr/bin/python
# -*- coding:UTF-8 -*-



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = l1
        i = 1
        num_l1 = 0
        # get num of l1
        while n:
            num_l1 = num_l1 + n.val * i
            i = i * 10
            n = n.next

        m = l2
        j = 1
        num_l2 = 0
        # get num of l2
        while m:
            num_l2 = num_l2 + m.val * j
            j = j * 10
            m = m.next

        str_num = str(num_l1 + num_l2) 
        str_num = str_num[::-1]
        res = list_result = ListNode(0)
        
        for s in str_num:
            list_result.next = ListNode(int(s))
            list_result = list_result.next          
        return res.next


#########################################################################

# class Node(object):
# 	def __init__(self):
# 		self.val = None
# 		self.next = None

# class Node_handle():
# 	def __init__(self):
# 		self.cur_node = None

# 	def find(self,node,num,a = 0):
# 		while node:
# 			if a == num:
# 				return node
# 			a += 1
# 			node = node.next

# 	def add(self,data):
# 		node = Node()
# 		node.val = data
# 		node.next = self.cur_node
# 		self.cur_node = node
# 		return node
# 	def printNode(self,node):
# 		while node:
# 			print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
# 			node = node.next

# 	def delete(self,node,num,b = 1):
# 		if num == 0:
# 			node = node.next
# 			return node
# 		while node and node.next:
# 			if num == b:
# 				node.next = node.next.next
# 			b += 1
# 			node = node.next
# 		return node

# 	def reverse(self,nodelist):
# 		list = []
# 		while nodelist:
# 			list.append(nodelist.val)
# 			nodelist = nodelist.next
# 		result = Node()
# 		result_handle =Node_handle()
# 		for i in list:
# 			result = result_handle.add(i)
# 		return result

# if __name__ == "__main__":
# 	l1 = Node()
# 	ListNode_1 = Node_handle()
# 	l1_list = [1, 8, 3]
# 	for i in l1_list:
# 	    l1 = ListNode_1.add(i)
# 	ListNode_1.printNode(l1)
# 	l1 = ListNode_1.delete(l1,0)
# 	ListNode_1.printNode(l1)
# 	l1 = ListNode_1.reverse(l1)
# 	ListNode_1.printNode(l1)
# 	l1 = ListNode_1.find(l1,1)
# 	ListNode_1.printNode(l1)