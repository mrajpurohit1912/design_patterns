#Meaning - Singleton desgin pattern is a creational design pattern that ensues a class has only 1 instance throughout the appliacation and provide global point of access to that instance

#usecase - logging, DB connector, configuration settings,file system handlers,network managers

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

class my_dummy_class:
    def __new__(cls):
        pass