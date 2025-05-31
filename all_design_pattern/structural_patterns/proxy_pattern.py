"""
What is proxy design pattern?
-> The procxy design patten is a structural design pattern providea a placeholder(proxy) for another object to control access to it.it act as inteface to something else.typically to add  an extra layer of functonallity (like security,caching,logging or access control) without changing the orignal object

what is the use case of it?
1.Access control / Authorization
-> Control who can access the real object(e.g sensitive data,secured serivce)

2.Lazy Initilaization/Virtual Proxy
->Delay creation of expensive objects until they are needed

3.Logging/Monitoring
->Intercepts requests to log usage or meaure performace

4.Caching Proxy
->Stores results of expenisve calls and reuse them

5.Remote Proxy
-> used to represent an object that exists in different address space(e.g in RPC or RMI)

"""


from abc import ABC,abstractmethod

class Image(ABC):
    @abstractmethod
    def display():
        pass

class RealImage(Image):
    def __init__(self,filename):
        self.filename = filename
        self.load_from_disk()

    def display(self):
        print(f"Diplaying {self.filename}")

    def load_from_disk(self):
        print(f"Loading from {self.filename} from disk")

class proxy(Image):
    def __init__(self,filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)

        self.real_image.display()

if __name__ == "__main__":
    image1 = proxy('image1')
    image2 = proxy('image2')

    image1.display()
    image1.display()
    image2.display()