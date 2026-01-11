# learning classes and objects in oops 
class Employee():
    def __init__(self, role, depart, salary):
        self.role=role
        self.depart=depart
        self.salary=salary
    def showdetails(self):
        print("role is :",self.role)
        print("department is :",self.depart)
        print("salary is :",self.salary)
class Enginner(Employee):
    def __init__(self, name , age):
        super().__init__("engg","it","40,000")
        self.name=name
        self.age=age
 
engg=Enginner("lakshit",20)
engg.showdetails()

class order:
    def __init__(self, item, price):
        self.item=item 
        self.price=price
    def __gt__(self,ord2):
        return self.price > ord2.price
    
    

ord1=order("chips",80)
ord2=order("tea",60)

print(ord1 > ord2)

class shape:
    @staticmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self, r):
        self.r=r
    def Area(self):
        area=(22/7)*self.r**2
        return area
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def Area(self):
        area=self.l*self.b
        return area
    

r1=Circle(21)
r2=rectangle(4,8)
print("area of a circle",r1.Area())
print("area of a rectangle",r2.Area())
    
print("done github")