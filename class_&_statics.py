# define class method and static method in python with example

class A:
    def __init__(self):
        pass
    @staticmethod
    def static_method():
        return"this is a static method"
    @classmethod
    def class_method(selfx):
        return "this is a class method"
obj1 = A()
print(A.static_method())
print(A.static_method)