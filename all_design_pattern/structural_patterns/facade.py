"""
What is facade design pattern?
-> it is a structural design pattern that provides a interface to a larger and more complex system of classes,libraries and framwork.it acts as a wrapper that hides the complexities of the system and exposes only when it is necessary to the client

What is the usecase of it?
1.Clients interect with one simplified API insted of multiple complex system
2.Changes in subsystem do not affect the client code.
3.Easier to update the system without affecting clients.
4.Internals of the system remain hidden.
"""

"""Example 1"""

# class DVDPlayer:
#     def on(self):print(f"DVD player on")
#     def play(self):print(f"DVD player playing movie")

# class Projector:
#     def on(self):print(f"Projector on")
#     def WideScreenMode(self):print(f"Projector in wide screen mode")

# class Amplifier:
#     def on(self):print(f"Amplifier on")
#     def setVolume(self,volume):print(f"Amlifier volume set to {volume}")

# class Lights:
#     def dim(self):print("Lights dimmed")


# class HomeTheaterFacade:
#     def __init__(self,dvd,projector,amp,lights):
#         self.dvd = dvd
#         self.projector = projector
#         self.amp = amp
#         self.ligths = lights
    
#     def watchMovie(self):
#         print(f"Get ready to watch movie")
#         self.ligths.dim()
#         self.projector.on()
#         self.projector.WideScreenMode()
#         self.amp.on()
#         self.amp.setVolume(10)
#         self.dvd.on()
#         self.dvd.play()

# if __name__ == "__main__":
#     dvd = DVDPlayer()
#     projector = Projector()
#     amp = Amplifier()
#     lights = Lights()

#     hometheater = HomeTheaterFacade(dvd,projector,amp,lights)
#     hometheater.watchMovie()

#############################################################

"""Example 2"""

class Cutter:
    @property
    def cutVegetable(self):
        print(f"Cut vegetables")

class Boliler:
    @property
    def boilVegetable(self):
        print(f"Boil vegetables")

class Frier:
    @property
    def fryVegetable(self):
        print(f"Fry vegetables")



class Cooking:
    def __init__(self,cutter,boiler,frier):
        self.cutter = cutter
        self.boiler = boiler
        self.frier = frier

    def makeDish(self):
        self.cutter.cutVegetable
        self.boiler.boilVegetable
        self.frier.fryVegetable

        print(f"Dish is ready")


if __name__ == "__main__":
    cutter = Cutter()
    boiler = Boliler()
    frier = Frier()

    cook = Cooking(cutter,boiler,frier)

    cook.makeDish()
   