class parent():
    def par(self):
        print("parent  class method")
class child(parent):
    print("child class")
    obj=parent()
    obj.par()