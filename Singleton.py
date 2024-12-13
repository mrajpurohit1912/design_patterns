# # def greet(*args):
# #     # for name in args:
# #     #     print(f'Hello world {name}')
# #     return args
# # tp = ('mahavir','fadfd','gwfadsf')
# # ans = greet(tp)
# # print(ans)
# # print(type(ans))


# def print_off(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")


# print_off(name='Mahavir',age=85,location='Mumbai')

# class Singlton(object):
#     def __new__(cls,*args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super().__new__(cls,*args,**kwargs)
#         return cls._instance

# o1 = Singlton()
# print(f"Object - 1 ==>", o1)
# o1.data = 10

# o2 = Singlton()
# print(f"Object - 2 ==> ",o2)
# print(f"Object - 2 data ==>",o2.data)
# o2.data = 5

# print(f"Object - 1 data ==>",o1.data)