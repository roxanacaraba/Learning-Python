class A:
     def __init__(self):
         print("Class A - constructor")
     def method1(self):
         print("method1 is a method of class A")

class B:
    def __init__(self):
        print("Class B - constructor")
    def method2(self):
        obiect = A()
        obiect.method1()
        print("method2 is a method of class B")

obiect = B()
obiect.method2()


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def emp_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Data:

    def __init__(self, role, emp_object):
        self.role = role
        self.emp_object = emp_object

    def display(self):
        self.emp_object.emp_data()
        print("Role: ", self.role)

employee = Employee("Tom", 30)
data = Data("Manager", employee)
data.display()


