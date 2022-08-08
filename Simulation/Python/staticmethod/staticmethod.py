"""
    Implements decorator staticMethod() which simulates staticmethod()
"""

class staticMethod():
    def __init__(self, fn):
        self.fn = fn
    def __get__(self, ins, own):
        return self.fn

### Testing

# Class used in test
class Foo():
    @staticMethod
    def add(a, b):

        return a + b
    
# Test code

print("Instance call:", Foo().add(1, 3))
print("Class call", Foo.add(2, 5))

