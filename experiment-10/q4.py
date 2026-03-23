class parent():
    def show(self):
        print("parent class method")
class child(parent):
    def __init__(self,a):
        self.a=a
    def show(self):
        print("parent class method override",self.a)
obj1=parent()
obj2=child(5)
obj1.show()
obj2.show()
class GrandParent():
    def property(self):
        print("grandparent method")
class parent(GrandParent):
    def buisness(self):
        print("parent method")
class child(parent):
    def education(self):
        print("child method")
obj=child()
obj.property()
obj.buisness()
obj.education()