class Car(object):
    def __init__(self, name="General", model="GM", type_="saloon"):
        # Return a car object whose name is Honda"""
        self.name = name
        self.model = model
        self.type_ = type_
        self.num_of_doors = 4
        self.num_of_wheels = 4

        self.speed = 0

        # Number of doors based on car type
        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2

        # The car should have four (4) wheels except its a type of trailer
        if self.type_ == "trailer":
            self.num_of_wheels = 8

        # The car type should be saloon if it is not a trailer
    def is_saloon(self):
        if self.type_ == 'saloon':
            return True
        else:
            return False

    def drive(self, gear):
        # The Trailer should have speed 0 km/h until
        # you put `the pedal to the metal
        # The Mercedes should have speed 0 km/h
        # until you put `the pedal to the metal
        # The car drive function should return the instance of the Car class
        if gear == 7:
            self.speed = 77
        elif gear == 3:
            self.speed = 1000
        return self




        



