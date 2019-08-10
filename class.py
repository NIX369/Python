class Planet:
    shape = "round"    # class level attribute

    def __init__(self,name,radius,gravity,system):        # instant level attribute
                                                          # can be accessed only by object ie object_name.attribute
        self.name=name                                    # class level can be accessed by using class name ie class_name.attribute
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        print(f"{self.name} is orbiting in the {self.system} ")

hoth = Planet("Hoth",2000000,8,"Hoth system")
print(f"Name of planet is {hoth.name} ")
print(f"Radius of planet is {hoth.radius} ")
print(f"Gravity here is {hoth.gravity} ")
print(f"It is revolving in the {hoth.system} ")
print(hoth.orbit())
print(Planet.shape)

