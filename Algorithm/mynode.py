__author__ = 'pbillava'

class Node(object):
    def __init__(self, initdata):
        self.data=initdata
        self.nextnode=None

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextnode

    def setdata(self, data):
        self.data=data

    def setNextNode(self, nextnode):
        self.nextnode=nextnode

if __name__=='__main__':
    n1=Node(10)
    n2=Node(20)
    print "n1 has %s"%n1.getData()
    print "n1 next node is %s"%n1.getNextNode()
    n1.setNextNode(n2)
    print "n2 has %s"%n2.getData()
    print "n2 next node is %s"%n2.getNextNode()
    print "n1 has %s"%n1.getData()
    print "n1 next node is %s"%n1.getNextNode()
    print "n1 next node data is %s"%n1.getNextNode().getData()



