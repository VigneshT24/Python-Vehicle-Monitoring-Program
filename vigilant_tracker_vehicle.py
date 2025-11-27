class Vehicle:
    make = None
    model = None
    electric = None
    color = None
    year = None
    moving = None

    def __init__(self, make, model, electric, color, year, moving):
        self.make = make
        self.model = model
        self.electric = electric
        self.color = color
        self.year = year
        self.moving = moving

    def changeMake(self, make):
        self.make = make

    def changeModel(self, model):
        self.model = model

    def changeElectric(self, electric):
        self.electric = electric

    def changeColor(self, color):
        self.color = color

    def changeYear(self, year):
        self.year = year

    def changeMoving(self):
        self.moving = not self.moving

