#!/usr/bin/env python3

class Node:
  def __init__(self, data, next = None):
    self.data_1 = data
    self.next = next
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_node(self, data):
    newNode = Node(data)
    
    
first = Node(3)
print("The first node is: {}".format(first.data_1))