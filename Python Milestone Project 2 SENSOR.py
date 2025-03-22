import random

class VehicleSensor: # Super 1
    system_health = None
    sensorStatus = None
    sensorID = None

    def __init__(self):
        self.system_health = random.randint(1, 100)
        self.sensorStatus = False

    def changeStatus(self):
        self.sensorStatus = not self.sensorStatus

    def fixSystemHealth(self):
        if(self.system_health < 55):
            self.system_health += 50

    def decreaseSystemHealth(self, value):
        self.system_health -= value

class UltrasonicSensor(VehicleSensor): # Derived 1
    uSensorRange = None

    def __init__(self):
        super().__init__()
        self.sensorID = "HCSR" + str(random.randint(10, 100))
        self.uSensorRange = "4m"

class CameraSensor(VehicleSensor): # Derived 2
    cSensorRange = None

    def __init__(self):
        super().__init__()
        self.sensorID = "OV" + str(random.randint(1000, 10000))
        self.cSensorRange = "75m"

class RadarSensor(VehicleSensor): # Derived 3
    rSensorRange = None

    def __init__(self):
        super().__init__()
        self.sensorID = "RCWL-" + str(random.randint(1000, 10000))
        self.rSensorRange = "10m"

class TemperatureSensor(VehicleSensor): # Derived 4
    currentTemp = None

    def __init__(self):
        super().__init__()
        self.sensorID = "A" + str(random.randint(1000, 10000))
        self.currentTemp = random.randint(5, 121)

    def fixTemperature(self):
        if(self.currentTemp > 100):
            self.currentTemp -= 35

    def changeTemperature(self, newTemp):
        self.currentTemp = newTemp

class SpeedSensor(VehicleSensor): # Derived 5
    currentSpeed = None

    def __init__(self):
        super().__init__()
        self.sensorID = "DS" + str(random.randint(10, 100)) + "B" + str(random.randint(10, 100))
        self.currentSpeed = random.randint(0, 161)

    def setSpeed(self, currentSpeed):
        self.currentSpeed = currentSpeed

