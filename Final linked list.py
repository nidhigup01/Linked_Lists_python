# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:41:56 2018

@author: nidhi
#learned from https://www.youtube.com/watch?v=JlMyYuY1aXU
#"""

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        cur = self.head
        new_node = Node(data) 
        while cur.next:
            cur = cur.next  
        cur.next = new_node
        cur.next.data = data
        
            
    def length(self):
        current_node = self.head
        total_length = 0
        while current_node.next:
            total_length += 1
            current_node = current_node.next
        return total_length
       
    
    def display(self):
        list = []
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            list.append(current_node.data)
        print (list)
        
    def get(self, index):
        cur = self.head
        ctr = 0
        if index >= self.length():
            print ('error, out of range')
        while ctr <= index:
            cur = cur.next
            ctr +=1
            
        print ('for index {} data is {}'.format(index, cur.data))
               

    def remove(self,index):
        current_node = self.head
        last_node = None
        counter = 0
        
        
        if index >= self.length() or index < 0:
            print('Out of index range')
            return False
        
        while current_node:
            if counter == index+1:
                last_node.next = current_node.next
                print('The node with index {} is deleted'.format(index))
                return True
            else:
                counter += 1
                last_node = current_node
                current_node = current_node.next
        return



    
            
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.display()
print(l.length())
l.get(2)
l.get(3)
l.remove(2)
l.display()
l.get(2)
l.get(1)
l.get(2)
l.get(0)

