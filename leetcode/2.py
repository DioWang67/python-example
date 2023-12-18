#!usr/bin/python
# -*- coding:UTF-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l1 = [8,1,9]
#         l2 = [2,2,1]

#         len_l1= len(l1)-1
#         len_l2= len(l2)-1

#         len_3=[]
#         i = 0
#         I = 0
#         if len_l1 >len_l2:
#             for i in range(len_l1-len_l2):
#                 l2.append(0)
#                 print(l1)
#         if len_l1 <len_l2:
#             for i in range(len_l2-len_l1):
#                 l1.append(0)
#                 print(l2)


#         while I <= len_l1 or I<= len_l2 :
#             print(l1[I],l2[I])
#             try:
#                 len_3[I]=len_3[I]+l1[I]+l2[I]
#                 print (len_3[I])
#                 if len_3[I] >=10:
#                     len_3[I]=len_3[I]%10
#                     len_3.append(1)
#             except:
#                 len_3.append(l1[I]+l2[I])
#                 if len_3[I] >=10:
#                     len_3[I]=len_3[I]%10 
#                     len_3.append(1)
#             I +=1
#         print(len_3)




class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"









# class Solution:


#     def addTwoNumbers(self, l1, l2):
#         head = curr = ListNode(0)
#         carry = 0
#         l1 = ListNode(l1)
#         l2 = ListNode(l2)



#         # l1 = [8,1,9]
#         # l2 = [2,2,1]
#         while l1 or l2 or carry:
#             if l1:
#                 num1 = l1.val
#                 l1 = l1.next
#             else:
#                 num1 = 0
#             if l2:
#                 num2 = l2.val
#                 l2 = l2.next

#             else:
#                 num2 = 0


#             sum = num1 + num2 + carry
#             carry = sum // 10
#             print(sum)

#             curr.next = ListNode(sum % 10)
#             curr = curr.next
#             print(curr)

#         return head.next





class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        # print(root)
        l1 = ListNode(l1)
        l2 = ListNode(l2)
        # print(l1,l2)

        while l1 or l2 or carry:
            v1 = v2 = 0
            # print(l1)
            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1+v2+carry, 10)
            print(carry,val)
            n.next = ListNode(val)
            n = n.next
            # print(n)
            # print(root.next)
        return root.next









    # def func(self, l1, l2) -> ListNode:
    #     l1 = ListNode(l1)
    #     l2 = ListNode(l2)
    #     l3 = []
        # print(l1,l2)

        # print(self.addTwoNumbers(l1,l2))





if __name__ =='__main__' :
    s = Solution()
    l1=[2,4,3]
    l2=[5,6,4]




    # s.func(l1,l2)
    print (s.addTwoNumbers(l1,l2))




# class Solution:
# # @return a ListNode
#     def addTwoNumbers(self, l1, l2):
#         carry = 0
#         root = n = ListNode(0)
#         while l1 or l2 or carry:
#             v1 = v2 = 0
#             if l1:
#                 v1 = l1.val
#                 l1 = l1.next
#             if l2:
#                 v2 = l2.val
#                 l2 = l2.next
#             carry, val = divmod(v1+v2+carry, 10)
#             n.next = ListNode(val)
#             n = n.next
#         return root.next













# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         n = l1
#         i = 1
#         num_l1 = 0
#         # get num of l1
#         while n:
#             num_l1 = num_l1 + n.val * i
#             i = i * 10
#             n = n.next

#         m = l2
#         j = 1
#         num_l2 = 0
#         # get num of l2
#         while m:
#             num_l2 = num_l2 + m.val * j
#             j = j * 10
#             m = m.next

#         str_num = str(num_l1 + num_l2) 
#         str_num = str_num[::-1]
#         res = list_result = ListNode(0)
        
#         for s in str_num:
#             list_result.next = ListNode(int(s))
#             list_result = list_result.next          
#         return res.next

# if __name__ == '__main__':
#     a=Solution()
#     l1=ListNode(1)
#     l2=ListNode(2)
#     # print (a.addTwoNumbers(l1,l2))

#     l1=ListNode(5,3)
#     l2=ListNode(3,2)

#     print (a.addTwoNumbers(l1,l2))

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