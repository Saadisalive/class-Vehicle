#create class
class Vechicle:

    #Create init method
    def __init__(self,max_speed,muilage):

        self.max_speed = max_speed
        self.milage = muilage

modelX = Vechicle(240,18)

print("Model max speed:",modelX.max_speed)
print("Model milage:",modelX.milage)