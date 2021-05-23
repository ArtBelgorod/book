class Employee():

    def __init__(self,name,family,myraise):
        self.name = name
        self.family = family
        self.myraise = myraise

    def give_raise(self,plus = 5000):
        self.myraise += plus



