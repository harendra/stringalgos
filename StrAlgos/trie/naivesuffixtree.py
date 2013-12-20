'''
Created on 2013/12/20

@author: harendra
'''
class Node(object):
    val=None
    edges=None

class Edge(object):
    destinationNode=None
    edgevalue=None

class SuffixTree(object):
    rootnode=None
    order=0
    def __init__(self,inputstring):
        self.rootnode=Node()
        self.rootnode.val="Root"
        self.inputstring=inputstring
        self.createTree()

    def createTree(self):
        for i in range(1,len(self.inputstring)+1):
            self.insert(self.rootnode,self.inputstring[-i:])

    def insert(self,node,substring):
        self.order+=1
        addnewedge=True
        if node.edges==None:
            node.edges=[]
        for edge in node.edges:
            currentsubstring=edge.edgevalue
            if currentsubstring[0]==substring[0]:
                addnewedge=False
                common_prefix=self._get_longest_prefix(substring,currentsubstring)
                currentresidual=currentsubstring[len(common_prefix):]
                substringresidual=substring[len(common_prefix):]
                if(len(currentresidual)!=0):
                    self.attachEdge(edge.destinationNode,currentresidual)
                if(len(substringresidual)!=0):
                    self.insert(edge.destinationNode,substringresidual)
                return
        if addnewedge:
            self.attachEdge(node,substring)

    def doBFS(self,nodes):
        if nodes is None:
            nodes=[self.rootnode]
        if len(nodes)==0:
            return
        nextnodes=[]
        for node in nodes:
            for edge in node.edges:
                print edge.edgevalue
                nextnodes.append(edge.destinationNode)
        print "############################################################"
        self.doBFS(nextnodes)

    def attachEdge(self,node,edgeval):
        newnode=Node()
        newnode.val='$'
        newnode.edges=[]
        edge=Edge()
        edge.edgevalue=edgeval
        edge.destinationNode=newnode
        node.edges.append(edge)


    def _get_longest_prefix(self,seq1,seq2):
        start=0
        while start<min(len(seq1),len(seq2)):
            if seq1[start]!=seq2[start]:
                break
            start+=1
        return seq1[:start]

string_="bananasbananasbananasbananasbananas"
s=SuffixTree(string_)
s.doBFS(None)
print s.order
print len(string_)
