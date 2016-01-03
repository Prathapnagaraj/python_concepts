__author__ = 'pbillava'

from mynode import Node

class UnorderedList(object):

    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self, item):
        temp=None(item)

        if self.head==None:
            self.head=temp
        else:
            temp.setNextNode(self.head)
            self.head=temp

    def size(self):
        count=0
        current=self.head
        while current != None:
            count=+1
            current=current.getNextNode()
        return count