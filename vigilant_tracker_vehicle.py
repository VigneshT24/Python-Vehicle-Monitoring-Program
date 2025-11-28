class Vehicle:
    """
    Represents a vehicle with its specifications and operational state.

    This class encapsulates all essential vehicle information including physical
    characteristics (make, model, color), specifications (year, electric status),
    and operational state (moving status). Provides methods to modify vehicle
    attributes during runtime.

    Attributes:
        make (str): Manufacturer of the vehicle (e.g., "Toyota", "Tesla", "Ford")
        model (str): Specific model name (e.g., "Camry", "Model 3", "F-150")
        electric (bool): Electric vehicle status (True=Electric, False=Gas/Hybrid)
        color (str): Exterior color of the vehicle (e.g., "Red", "Blue", "Black")
        year (int): Manufacturing year of the vehicle (e.g., 2020, 2023)
        moving (bool): Current motion status (True=In motion, False=Stationary)
    """
    make = None
    model = None
    electric = None
    color = None
    year = None
    moving = None

    def __init__(self, make, model, electric, color, year, moving):
        """
        Initializes a Vehicle object with specified attributes.

        Args:
            make (str): Manufacturer/brand of the vehicle
            model (str): Model name of the vehicle
            electric (bool): Whether the vehicle is electric-powered
            color (str): Exterior color of the vehicle
            year (int): Year the vehicle was manufactured
            moving (bool): Initial motion state of the vehicle
        """
        self.make = make
        self.model = model
        self.electric = electric
        self.color = color
        self.year = year
        self.moving = moving

    def changeMake(self, make):
        """
        Updates the vehicle's manufacturer.

        Args:
            make (str): New manufacturer name (e.g., "Honda", "BMW")
        """
        self.make = make

    def changeModel(self, model):
        """
        Updates the vehicle's model name.

        Args:
            model (str): New model designation (e.g., "Accord", "3 Series")
        """
        self.model = model

    def changeElectric(self, electric):
        """
        Updates the vehicle's electric powertrain status.

        Args:
            electric (bool): New electric status (True for electric, False for gas/hybrid)
        """
        self.electric = electric

    def changeColor(self, color):
        """
        Updates the vehicle's exterior color.

        Args:
            color (str): New color designation (e.g., "Silver", "White")
        """
        self.color = color

    def changeYear(self, year):
        """
        Updates the vehicle's manufacturing year.

        Args:
            year (int): New year value (e.g., 2021, 2024)
        """
        self.year = year

    def changeMoving(self):
        """
        Toggles the vehicle's motion state between moving and stationary.

        Flips the current moving boolean value (True ↔ False).
        Used to start/stop the vehicle or update its operational status.
        """
        self.moving = not self.moving