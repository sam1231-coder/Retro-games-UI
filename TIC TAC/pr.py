# # # name = "TONY"
# # # print(name.lower())
# # # print(name.find('y'))
# # # print(name.replace('N', 'm'))
# # # i = 4
# # # i += 2
# # # print(i)

# # def formatList(items):
# #     if len(items) == 0:
# #         return ''

    
# #     if len(items) == 1:
# #         return items[0]

   
# #     if len(items) == 2:
# #         return items[0] + ' and ' + items[1]

    
# #     str = ''
# #     for i in range(len(items)):
# #         if i < len(items) - 2:
# #             str += items[i] + ', '
# #         elif i == len(items) - 2:
# #             str += items[i] + ' and '
# #         else:
# #             str += items[i]
# #     return str

# # def main():
# #     items = []

# #     while True:
# #         item = input("Enter an item (enter 'done' when finished): ")
# #         if item == 'done':
# #             break
# #         items.append(item)

# #     formatted_list = formatList(items)
# #     print("The formatted list is:", formatted_list)

# # main()

# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None
 
 
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
 
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
 
#     def get_prev_node(self, ref_node):
#         current = self.head
#         while (current and current.next != ref_node):
#             current = current.next
#         return current
 
 
# def is_palindrome(llist):
#     start = llist.head
#     end = llist.last_node
#     while (start != end and end.next != start):
#         if start.data != end.data:
#             return False
#         start = start.next
#         end = llist.get_prev_node(end)
#     return True
 
 
# a_llist = LinkedList()
 
# data_list = input('Please enter the elements in the linked list: ').split()
# for data in data_list:
#     a_llist.append(int(data))
 
# if is_palindrome(a_llist):
#     print('The linked list is palindromic.')
# else:
#     print('The linked list is not palindromic.')

