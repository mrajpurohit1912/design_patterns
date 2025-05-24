from dataclasses import dataclass

# @dataclass
# class ABCD:
#     name:str = "Mahavir"
#     age:int = 26
#     status:bool = False


# @dataclass
# class XYX:
#     name:str = "Mahavir"
#     age:int = 26
#     status:bool = False

# cl  = ABCD()
# bl  = XYX()
# print(cl == bl)

# from pydantic import BaseModel
# from enum import Enum

# class Weapons(Enum):
#     S = "sword"
#     b = "bow"
#     A = "axe"


# we = Weapons('sword')

# print(we)


# class Armory(BaseModel):
#     rooms:int
#     weapons : list[Weapons]

# ar = Armory(rooms=2,weapons = ['sword','bow'])
# data = ar.model_dump_json()
# #data= data['weapons']
# print(data)
# print(type(data))



class A:
    def say_hi():
        print('Hello World from A')

class B(A):
    def say_hi():
        print('Hello World from B')

class C(A):
    def say_hi():
        print('Hello World from C')

class D(C,B):
    # def say_hi():
    #     print('Hello World')
    pass
data = D
print(data.say_hi())