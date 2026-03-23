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