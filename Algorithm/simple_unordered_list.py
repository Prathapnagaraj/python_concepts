__author__ = 'pbillava'

from mynode import Node

class UnorderedList(object):

    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self, item):
        temp=Node(item)
        temp.setNextNode(self.head)
        self.head=temp

    def size(self):
        count=0
        current=self.head
        while current != None:
            count=count+1
            current=current.getNextNode()
        return count

    def search(self, item):
        current=self.head
        found=False
        while current != None:
            if current.getData()==item:
                found=True
            current=current.getNextNode()
        return found

    def remove(self, item):
        current=self.head
        previous=None
        found=False
        while current != None and (not found):
            if item==current.getData():
                found=True
            else:
                previous=current
                current=current.getNextNode()
        if previous == None:
            self.head=current.getNextNode()
        else:
            previous.setNextNode(current.getNextNode())

    def printlist(self):
        current=self.head
        while current != None:
            print "node data %s"%current.getData()
            current=current.getNextNode()



if __name__=="__main__":
    mylist=UnorderedList()
    print mylist.isEmpty()
    print mylist.size()
    mylist.printlist()
    mylist.add(10)
    print mylist.size()
    mylist.add(20)
    print mylist.size()
    mylist.add(30)
    print mylist.size()
    mylist.add(40)
    mylist.printlist()
    print mylist.isEmpty()
    print mylist.size()
    print mylist.search(20)
    mylist.remove(20)
    print mylist.search(20)



