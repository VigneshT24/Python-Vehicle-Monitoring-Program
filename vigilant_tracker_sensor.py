import random


class VehicleSensor:  # Super 1
    """
    Base class for all vehicle sensors with common health monitoring functionality.

    This parent class provides the core attributes and methods shared by all sensor types,
    including system health tracking, status management, and maintenance operations.

    Attributes:
        system_health (int): Health percentage of the sensor (0-100%)
        sensorStatus (bool): Current operational status (True=Active, False=Inactive)
        sensorID (str): Unique identifier for the sensor (set by derived classes)
    """
    system_health = None
    sensorStatus = None
    sensorID = None

    def __init__(self):
        """
        Initializes a vehicle sensor with random health and inactive status.

        Sets initial system health to a random value between 1-100% and
        defaults the sensor to inactive status until activated.
        """
        self.system_health = random.randint(1, 100)
        self.sensorStatus = False

    def changeStatus(self):
        """
        Toggles the sensor's operational status between active and inactive.

        Flips the current sensorStatus boolean value (True ↔ False).
        """
        self.sensorStatus = not self.sensorStatus

    def fixSystemHealth(self):
        """
        Performs maintenance to restore sensor health if below threshold.

        Increases system health by 50% if current health is below 55%,
        simulating a repair or recalibration operation.
        """
        if (self.system_health < 55):
            self.system_health += 50

    def decreaseSystemHealth(self, value):
        """
        Degrades sensor health by a specified amount.

        Args:
            value (int): Amount to decrease system health by (in percentage points)
        """
        self.system_health -= value


class UltrasonicSensor(VehicleSensor):  # Derived 1
    """
    Ultrasonic proximity sensor for short-range object detection.

    Used for parking assistance, blind spot detection, and collision avoidance.
    Inherits health monitoring from VehicleSensor and adds range specifications.

    Attributes:
        uSensorRange (str): Detection range of the ultrasonic sensor
        sensorID (str): Unique ID in format "HCSR##" (10-100)
    """
    uSensorRange = None

    def __init__(self):
        """
        Initializes an ultrasonic sensor with 4-meter detection range.

        Generates a unique sensor ID in the format "HCSR##" where ## is a
        random number between 10-100, mimicking HC-SR04 sensor naming.
        """
        super().__init__()
        self.sensorID = "HCSR" + str(random.randint(10, 100))
        self.uSensorRange = "4m"


class CameraSensor(VehicleSensor):  # Derived 2
    """
    Camera sensor for visual monitoring and lane detection.

    Used for lane keeping assist, traffic sign recognition, and general
    visual monitoring. Provides longer range detection than ultrasonic sensors.

    Attributes:
        cSensorRange (str): Detection range of the camera sensor
        sensorID (str): Unique ID in format "OV####" (1000-10000)
    """
    cSensorRange = None

    def __init__(self):
        """
        Initializes a camera sensor with 75-meter detection range.

        Generates a unique sensor ID in the format "OV####" where #### is a
        random number between 1000-10000, mimicking OmniVision camera naming.
        """
        super().__init__()
        self.sensorID = "OV" + str(random.randint(1000, 10000))
        self.cSensorRange = "75m"


class RadarSensor(VehicleSensor):  # Derived 3
    """
    Radar sensor for medium-range object detection and speed measurement.

    Used for adaptive cruise control, collision warning systems, and
    detecting objects in various weather conditions.

    Attributes:
        rSensorRange (str): Detection range of the radar sensor
        sensorID (str): Unique ID in format "RCWL-####" (1000-10000)
    """
    rSensorRange = None

    def __init__(self):
        """
        Initializes a radar sensor with 10-meter detection range.

        Generates a unique sensor ID in the format "RCWL-####" where #### is a
        random number between 1000-10000, mimicking RCWL radar module naming.
        """
        super().__init__()
        self.sensorID = "RCWL-" + str(random.randint(1000, 10000))
        self.rSensorRange = "10m"


class TemperatureSensor(VehicleSensor):  # Derived 4
    """
    Temperature sensor for engine and system thermal monitoring.

    Monitors vehicle temperature to prevent overheating and ensure optimal
    operating conditions. Critical for engine health and safety.

    Attributes:
        currentTemp (int): Current temperature reading in Fahrenheit
        sensorID (str): Unique ID in format "A####" (1000-10000)
    """
    currentTemp = None

    def __init__(self):
        """
        Initializes a temperature sensor with random starting temperature.

        Generates a unique sensor ID in the format "A####" and sets initial
        temperature to a random value between 5-121°F.
        """
        super().__init__()
        self.sensorID = "A" + str(random.randint(1000, 10000))
        self.currentTemp = random.randint(5, 121)

    def fixTemperature(self):
        """
        Reduces temperature if overheating is detected.

        Decreases temperature by 35°F if current reading exceeds 100°F,
        simulating cooling system activation or thermal management.
        """
        if (self.currentTemp > 100):
            self.currentTemp -= 35

    def changeTemperature(self, newTemp):
        """
        Updates the current temperature reading.

        Args:
            newTemp (int/float): New temperature value in Fahrenheit
        """
        self.currentTemp = newTemp


class SpeedSensor(VehicleSensor):  # Derived 5
    """
    Speed sensor for vehicle velocity measurement.

    Monitors current vehicle speed for speedometer display, cruise control,
    and safety systems. Essential for speed-related features and diagnostics.

    Attributes:
        currentSpeed (int): Current speed reading in miles per hour (MP/H)
        sensorID (str): Unique ID in format "DS##B##" (10-100 for each ##)
    """
    currentSpeed = None

    def __init__(self):
        """
        Initializes a speed sensor with random starting speed.

        Generates a unique sensor ID in the format "DS##B##" where each ## is
        a random number between 10-100, and sets initial speed to 0-161 MP/H.
        """
        super().__init__()
        self.sensorID = "DS" + str(random.randint(10, 100)) + "B" + str(random.randint(10, 100))
        self.currentSpeed = random.randint(0, 161)

    def setSpeed(self, currentSpeed):
        """
        Updates the current speed reading.

        Args:
            currentSpeed (int/float): New speed value in miles per hour (MP/H)
        """
        self.currentSpeed = currentSpeed