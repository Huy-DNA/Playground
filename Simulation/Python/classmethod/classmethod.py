"""
    Implements a decorator classMethod() that simulates classmethod()
"""

class classMethod():
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, obj, own):
        def bound_fn(*args, **kwargs):
            return self.fn(own, *args, **kwargs)
        return bound_fn


### Testing

# Class used in Test
class Foo():
    name = "huyDNA"
    @classMethod
    def get_name_cls(cls, mes):
        return f"{cls.name} - {mes}"
    
    def get_name_ins(self, mes):
        return f"{self.name} - {mes}"

    def __init__(self, name):
        self.name = name

# Testing Code
print("Testing....")
f = Foo("huyNormal")
print("Dot access:", f.name)
print("get_name_cls called:", f.get_name_cls("hi"))
print("get_name_cls called:", f.get_name_cls("hi"))

print("get_name_ins called:", f.get_name_ins(mes = "hi"))
print("get_name_ins called:", f.get_name_ins(mes = "hi"))
# Further observations
print("\nObserving....")
print("f.get_name_cls's class:", f.get_name_cls.__class__)
print("f.get_name_ins's class:", f.get_name_ins.__class__)



