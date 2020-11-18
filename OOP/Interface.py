import abc

class MyInterface(abc.ABC):
    @abc.abstractmethod
    def printfunct(self):
      pass

class Subclass(MyInterface):
    def printfunct(self):
        print("This is a subclass of my interface")


myclass = Subclass()
myclass.printfunct()
