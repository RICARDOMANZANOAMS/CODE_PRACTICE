from turtle import right


class binary_node:
    def __init__(self,val=0,left=None,rigth=None):
        self.val=val
        self.left=left
        self.rigth=rigth
    def insert_node(self,val):
        print("comparison")
        print(self.val)
        print(val)
class solution(binary_node):
    def check_tree(self,s):
        print("test")
        print(self.val)
        print(s)
a=binary_node(2)
a.insert_node(4)
b=solution(3)
b.check_tree(8)



#conclusion. solution no hereda nada de la anterior clase solo por poner self