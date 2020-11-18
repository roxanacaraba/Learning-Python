#A context manager is a mechanism where an object is created an notification about the moment that object is being access and the moment that object is being terminated.
#Context managers are used along with with keyword. The objects that available in a context manager should implement __enter__ and __exit__ methods.

"""
with item1 as alias1, [item2 as alias2, … item n as alias n]:
<statement 1>
<statement 2>
….
<statement n>


with item1, [item2, … item n]:
<statement 1>
<statement 2>
….
<statement n>
"""

class CachedFile:
    def __init__(self,fileName):
        self.data = ""
        self.fileName = fileName
    def __enter__(self):
        print("__enter__ is called")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__ is called")
        open(self.fileName,"wt").write(self.data)
        return False
with CachedFile("Test.txt") as f:
    f.data = "Python course"