import hashlib
from turtle import left

class Node:
    def __init__(self,left,right,content,hashvalue,is_copyied=False) -> None:
        self.left=left
        self.right=right
        self.hash=hashvalue
        self.content=content
        self.is_copyied=is_copyied
    def print_node(self):
        print("###################")
        if self.left:
            print("Left",self.left.content)
        if self.right:
            print("Right",self.right.content)
        print("Hash:",self.hash,"\ncontent:",self.content)
        
        print("###################")
    def get_hash(content):
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    def __str__(self) -> str:
        return str(self.hash)
    
    def copy(self):
        return Node(self.left,self.right,self.content,self.hash,True)
class MerkleTree:
    def __init__(self,items) -> None:
        nodes=[]
        self.root=None
        self.root1=None
        for item in items:
            #node=Node(None,None,item,Node.get_hash(item),False)
            self.merkle_tree_insert(self.root1,item)
            #nodes.append(node)
        #root=self.buildTree(nodes)
        print("***Tree1")
        self.print_nodes(self.root1)
        print("***Merkle Tree")
        #self.print_nodes(root)
    def new_hash(self,left,right):
        if left and right:
            Node.get_hash(left.hash+right.hash)
        if left:
            return left.hash
        else:
            return right.hash
        
    # merkle tree with Binary search tree also maintain hash of node where we are inserting the node
    def merkle_tree_insert(self,temp,val):
        if temp==None:
            self.root1=Node(None,None,val,Node.get_hash(val))
            return
        if val<=temp.content:
            if temp.left is None:
                temp.left=Node(None,None,val,Node.get_hash(val))
                leftright=self.new_hash(temp.left,temp.right)
                temp.hash=Node.get_hash(leftright)
                 
            else:
                self.merkle_tree_insert(temp.left,val)
                leftright=self.new_hash(temp.left,temp.right)
                temp.hash=Node.get_hash(leftright)
            return  
        else:
            if temp.right is None:
                temp.right=Node(None,None,val,Node.get_hash(val))
                leftright=self.new_hash(temp.left,temp.right)
                temp.hash=Node.get_hash(leftright)
                return 
            else:
                self.merkle_tree_insert(temp.right,val)
                leftright=self.new_hash(temp.left,temp.right)
                temp.hash=Node.get_hash(leftright)
            return
    # simple insert nodes in tree
    def insert(self,val):
        if self.root1==None:
            self.root1=Node(None,None,val,Node.get_hash(val))
            return
        temp=self.root1
        while temp:
            if val<=temp.content:
                if temp.left is None:
                    temp.left=Node(None,None,val,Node.get_hash(val))
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is None:
                    temp.right=Node(None,None,val,Node.get_hash(val))
                    break
                else:
                    
                    temp=temp.right
        
    # merkle Simple Tree combine two hash no order    
    def buildTree(self,nodes):
        while len(nodes)!=1:
            temp = []
            for i in range(0,len(nodes),2):
                node1 = nodes[i]
                if i+1 < len(nodes):
                    node2 = nodes[i+1]
                else:
                    temp.append(nodes[i])
                    break
                concatenatedHash = node1.hash + node2.hash
                new_node=Node(node1,node2,node1.content+node2.content,concatenatedHash)
                temp.append(new_node)
            nodes = temp 
        return nodes[0]   
    def print_nodes(self,node):
        if node==None:
            return
        node.print_node()
        self.print_nodes(node.left)
        self.print_nodes(node.right)
    
    
list=["5","3","1","10","4"]
MerkleTree(list)

        
