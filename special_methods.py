#Object Representation
####################################################################################################
#__str__(self):Defines the string representation of the object for print() or str()
#__repr__(self):Defines a formal string representation for debuging

# class Person():
#     def __init__(self,name):
#         self.name = name

#     # def __str__(self):
#     #     return f"Person named {self.name}"
    
#     # def __repr__(self):
#     #     return f"fsafsd('{self.name}')"
    

# p = Person('Alice')
# print(p)
# print(str(p))
# print(repr(p))

####################################################################################################
# Arithmetic Operations (Operator Overloading)
# __add__(self, other): Implements +.
# __sub__(self, other): Implements -.
# __mul__(self, other): Implements *, and so on.


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __add__(self,other):
#         return Point(self.x + other.x,self.y + other.y)

#     def __repr__(self):
#         return f"Point({self.x} , {self.y})"
# p1 = Point(1,2)
# p2 = Point(3,4)
# print(p1 + p2 )
# print(repr(p1) )
# print(repr(p2) )
####################################################################################################

# Comparison Operators
# __eq__(self, other): Implements ==.
# __lt__(self, other): Implements <.
# __gt__(self, other): Implements >.

# class Box:
#     def __init__(self,data):
#         self.data = data

#     def __lt__(self,other):
#         return self.data < other.data   
    
# b1 = Box(3)
# b2 = Box(6)

# print(b1 < b2)

####################################################################################################
# Attribute Access
# __getattr__(self, name): Called when an attribute is not found in an object.
# __setattr__(self, name, value): Customizes setting an attribute.

# class DynamicAttributes:
#     def __getattr__(self,name):
#         return f"{name} attribute does not exist "

# obj = DynamicAttributes('foo')
# print(obj.foo)

# class DynamicAttributes:
#     def __init__(self,data):
#         self.data = data

#     def __getattr__(self, name):
#         if name in self.data:
#             return self.data[name]
#         else:
#             return f"{name} Does not exist"


# class DynamicObject:
#     def __init__(self, data):
#         self.data = data

#     def __getattr__(self, name):
#         if name in self.data:
#             return self.data[name]
#         else:
#             raise AttributeError(f"Attribute '{name}' not found")

# obj = DynamicAttributes({'a':1,'b':2})
# #obj = DynamicObject({'a':1,'b':2})

# print(obj.a)
# print(obj.c)

####################################################################################################

# Callable Objects
# __call__(self, ...): Makes an instance of a class callable like a function.


# class Greeter:
#     def __call__(self, *args, **kwds):
#         return f"Greetings! {args}"


# greet = Greeter()

# print(greet('Alice'))

####################################################################################################
# Container-Like Behavior
# __getitem__(self, key): Implements indexing (obj[key]).
# __setitem__(self, key, value): Implements setting an item.
# __len__(self): Returns the length of the container.

# class CustomList:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

#     def __len__(self):
#         return len(self.items)

# cl = CustomList([1, 2, 3])
# print(cl[1])  # 2
# print(len(cl))  # 3

####################################################################################################

class Archar:
    def __init__(self,hp,mana,arrows):
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    # def __str__(self):
    #     return f"Archer with hp = {self.hp} mana = {self.mana} arrows = {self.arrows}"
    
    def __repr__(self):
        return f"Archer({self.hp},{self.mana},{self.arrows})"
    

    # def __add__(self,other):
    #     if not (other,Archar):
    #         return NotImplemented
    #     new_hp = self.hp + other.hp
    #     new_mana = self.mana + other.mana
    #     new_arrows = self.arrows + other.arrows
    #     return (new_hp,new_mana,new_arrows)

    # def __hash__(self):
    #     return 1

archer1 = Archar(100,100,5)
archer2 = Archar(100,100,5)
#print(archer1 + archer2) 

# new_dict = {archer1:"test"}

class Company:
    def __init__(self,size):
        self.size = size
        self.archers = []
        self.index = 0

    def add_archer(self,archer):
        if not isinstance(archer,Archar):
            raise TypeError("Only Archers allowed")
        if len(self.archers) > self.size:
            raise ValueError("Comapny already full")
        else:
            self.archers.append(archer)

    def __add__(self,other):
        if not isinstance(other,Archar):
            raise TypeError("Only Archers can be added")
        self.add_archer(other)
        return self
cp = Company(5)
# cp.add_archer(archer1)
# print(cp.archers)
# cp.add_archer(archer2)
# print(cp.archers)


new_company = archer1 + cp
print(cp.archers)
print(new_company.archers)