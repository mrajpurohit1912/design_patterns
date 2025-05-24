"""
what is singlton pattern?
-> Singleton patten ensure that class has only one instance throughout the whole application and provides a global point of access to that instance
->It is a creational design pattern — i.e., it's concerned with how objects are created

use cases of singleton pattern
-> Logging(centralized logging service)
-> Configuration
-> Thread Pool
-> Database connection management
-> Caching
-> File System access or control(e.g printer spoolers)
"""

class Singlton:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance
    
ob1 = Singlton()
ob1.data = 10
print(f"{ob1}:{ob1.data}")

ob2 = Singlton()
ob2.data = 5
print(f"{ob2}:{ob2.data}")

print(ob1.data)