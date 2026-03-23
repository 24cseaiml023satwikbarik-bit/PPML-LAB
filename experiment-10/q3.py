class father:
    def skill1(self):
        print("father method")
class mother:
    def skill2(self):
        print("mother method")
class child(father,mother):
    def skill3(self):
        print("child method")
obj=child()
obj.skill1()
obj.skill2()
obj.skill3()


