class num:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return num(self.value+other.value)