# Required pre-processors for program validity
from logging import critical
import MP2_VehicleSensor
import MP2_Vehicle
import random
import time
from MP2_VehicleSensor import UltrasonicSensor, CameraSensor, RadarSensor, TemperatureSensor, SpeedSensor
from loadingModule import loadingAnimation

# COMMON ATTRIBUTES OF SENSORS: System Health, Sensor ID, & Sensor Status
# UNIQUE ATTRIBUTES OF TEMP/SPEED SENSORS: Current Temperature & Current Speed

# Displays the current sensor reading array (updated)
def displayArray(sensorArray, status, metricSwitched):
    print("\nSensor ID:", end=" ")
    for i in range(len(sensorArray)):
        print(f"| {GREEN}{sensorArray[i].sensorID}", end=f"{RESET} |  ")
    print("\n\nStatus:", end="    ")
    for j in range(len(sensorArray)):
        if(sensorArray[j].system_health < 5):
            print(f"| {GREEN}Inactive", end=f"{RESET} |  ")
        else:
            print(f"| {GREEN}{status}", end=f"{RESET} |  ")
    print("\n\nHealth:", end="    ")
    for k in range(len(sensorArray)):
        if(sensorArray[k].system_health >= 50):
            print(f"|   {GREEN}{sensorArray[k].system_health}%", end=f"{RESET}   |  ")
        elif(sensorArray[k].system_health < 50 and sensorArray[k].system_health >= 5):
            print(f"|   {YELLOW}{sensorArray[k].system_health}%", end=f"{RESET}   |  ")
        else:
            print(f"|   {RED}{sensorArray[k].system_health}%", end=f"{RESET}   |  ")
    print("\n\nTemp:", end="      ")
    for a in range(len(sensorArray)):
        if(a == 3):
            if(sensorArray[a].system_health < 5):
                print(f"|   {RED}ISSUE", end=f"{RESET}   |  ")
            else:
                if(sensorArray[a].currentTemp < 100):
                    if(not metricSwitched):
                        print(f"|   {GREEN}{str(sensorArray[a].currentTemp)} F", end=f"{RESET}   |  ")
                    else:
                        print(f"|   {GREEN}{str(round(convertDegree(sensorArray[a].currentTemp)))} C", end=f"{RESET}   |  ")
                else:
                    if(not metricSwitched):
                        print(f"|   {RED}{str(sensorArray[a].currentTemp)} F", end=f"{RESET}   |  ")
                    else:
                        print(f"|   {RED}{str(round(convertDegree(sensorArray[a].currentTemp)))} C", end=f"{RESET}   |  ")
        else:
            print("|   N/A", end="   |  ")
    print("\n\nSpeed:", end="     ")
    for b in range(len(sensorArray)):
        if(b == 4):
            if(sensorArray[b].system_health < 5):
                print(f"|   {RED}ISSUE", end=f"{RESET}   |  ")
            else:
                if(sensorArray[b].currentSpeed < 80):
                    if(not metricSwitched):
                        print(f"| {GREEN}{sensorArray[b].currentSpeed} MP/H", end=f"{RESET} |  ")
                    else:
                        print(f"|   {GREEN}{str(round(convertSpeed(sensorArray[b].currentSpeed)))} KP/H", end=f"{RESET}   |  ")
                else:
                    if(not metricSwitched):
                        print(f"| {RED}{sensorArray[b].currentSpeed} MP/H", end=f"{RESET} |  ")
                    else:
                        print(f"|   {RED}{str(round(convertSpeed(sensorArray[b].currentSpeed)))} KP/H", end=f"{RESET}   |  ")
        else:
            print("|   N/A", end="   |  ")
    print()

# Updates the current sensor reading array to make live changes to Health, Temperature, Speed, & Status logistically
def updateArray(sensorArray, count):
    if(not check and sensorArray[4].currentSpeed >= 20):
        sensorArray[4].setSpeed(0)
    if(not check and sensorArray[3].currentTemp < 90):
        sensorArray[3].changeTemperature(90)
    for e in range(len(sensorArray)):
        if(not check):
            sensorArray[e].fixSystemHealth()
        if(sensorArray[e].system_health >= 5):
            flip = random.randint(0, 1)
            if(flip == 0):
                sensorArray[e].decreaseSystemHealth(random.randint(0, 1))
        else:
            count += 1
            if(count >= 5):
                return count
    flip = random.randint(0, 1)
    if(flip == 0):
        if(sensorArray[3].currentTemp < 180):
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp + random.randint(0, 2))
        else:
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp / 2)
        if(sensorArray[4].currentSpeed < 165):
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed + random.randint(0, 3))
        else:
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed - random.randint(10, 25))
    else:
        if(sensorArray[3].currentTemp >= 15):
            krand = random.randint(0, 1)
            if(krand == 1):
                sensorArray[3].changeTemperature(sensorArray[3].currentTemp - random.randint(0, 2))
        else:
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp + random.randint(60, 100))
        if(sensorArray[4].currentSpeed >= 3):
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed - random.randint(0, 3))
        else:
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed + random.randint(5, 15))
    return 0

# ANSI escape sequences for terminal cursor control
def move_cursor_up(lines):
    print(f"\033[{lines}A", end='')

def move_cursor_down(lines):
    print(f"\033[{lines}B", end='')

# Gives a delay gap between each iteration of sensor reading
def delayFunc():
    time.sleep(1)

# Capitalizes the first letter of each detail inputted about vehicle
def fixFormat(userStr):
    newStr = list(userStr.capitalize())
    for r in range(1, len(newStr)):
        if(newStr[r - 1] == " "):
            newStr[r] = newStr[r].upper()
    return "".join(newStr)

# Loading animation for visual effect
def introOutroAnimation(status):
    for seconds in range(0, 3):
        if(status == "Active"):
            print(f"Starting Vehicle to Motion{'.' * (seconds + 1)}   ", end = " ")
        else:
            print(f"Stopping Vehicle from Motion{'.' * (seconds + 1)}   ", end=" ")
        time.sleep(1)

# Updates the average temperature
def updateAveTemp(aveTemp):
    aveTemp += sensorArray[3].currentTemp
    return aveTemp

# Updates the average speed
def updateAveSpeed(aveSpeed):
    aveSpeed += sensorArray[4].currentSpeed
    return aveSpeed

# Converts F -> C in temperature
def convertDegree(currentTemp):
    return (currentTemp - 32) * (5/9)

# Converts MP/H -> KP/H in speed
def convertSpeed(currentSpeed):
    return currentSpeed * 1.609

# Variables
sensorArray = [UltrasonicSensor(), CameraSensor(), RadarSensor(), TemperatureSensor(), SpeedSensor()]
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BRIGHT_MAGENTA = "\033[95m"
BG_YELLOW = "\033[43m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"
status = "Active"
check = False
criticalCount = 0
moderateCount = 0
count = 0
aveSpeed = 0
aveTemp = 0
initialNum = 0
metricSwitched = False

# Introduction
print("\t\t\t\tVigilantTrack: Dynamic Vehicle Health Monitor\n")
print("In this program, you will add one vehicle of your choice to do a sensor reading where you will see the sensor data live (as it is changing).")
print("If all the sensor's health percent were to reach below 5%, the vehicle would stop immediately and give you the next steps.")
print("The vehicle would be in motion and active while the sensor reading is in progress.")
print("Simulation has been SCALED, meaning the health of the sensor goes down faster than in real-life for a quicker analysis and better gist.\n")
print("Advanced Feature Overview:\n> Predictive Maintenance Module\n> Adaptive Sensor Calibration\n> Fault Tolerant Framework\n> Real-time Data Visualization\n> Sensor Fusion Algorithm\n")

# Data inputting
make = fixFormat(input("Enter the make of the vehicle: "))
model = fixFormat(input("Enter the model of the vehicle: "))
electric = fixFormat(input(f"Is the {make} {model} electric (True/False): "))
while(electric != "True" and electric != "False"):
    electric = fixFormat(input("Make sure to enter either True or False: "))
color = fixFormat(input(f"What color is the {make} {model}: "))
while(color.isdigit()):
    color = fixFormat(input("Please enter a valid color. A color cannot be expressed in numbers: "))
while True:
    try:
        year = int(input(f"What year is the {make} {model}: "))
        while(year < 1880 or year > 2025):
            year = int(input(f"Please enter a valid year for {make} {model}: "))
        break
    except ValueError:
        print("You entered string instead of numbers. Please enter the year again.\n")
        continue

# Loading animation for visual effect
loadingAnimation()

# Vehicle detail printed in an arrowhead format
print(f"\n\nVEHICLE DATA:\n\t\t\t[Vehicle Make: {make}]\n\n\t\t\t\t\t\t[Vehicle Model: {model}]\n\n\t\t\t\t\t\t\t\t\t[Electric: {electric}]\n\n\t\t\t\t\t\t[Vehicle Color: {color}]\n\n\t\t\t[Vehicle Year: {year}]\n\n")

# Gather the time limit for sensor reading
while True:
    try:
        num = int(input("How long do you want the sensor reading to measure for in seconds (>0): "))
        initialNum = num
        while(num == 0):
            num = int(input("Input must not be 0. Only seconds greater than 0 are accepted: "))
        try:
            needMetric = (input("Type 'True' for metric convertion (KP/H, C) or press enter for default (MP/H, F): ")).lower()
            if(needMetric == "true"):
                metricSwitched = True
        except ValueError:
            print("Type either 'True' or 'False'. No other input is accepted.")
        break
    except ValueError:
        print("Cannot input string instead of numbers. Try again\n")

introOutroAnimation(status)

# Iterations of displaying and updating sensor data for num seconds
print(f"\n\n{BLUE}{year} {make} {model} (before complete){RESET}:")
print("\t   UltraSonic     Camera     Radar     Temperature     Speed")
while(num > 0):
    print(f"\r{BOLD}{BRIGHT_MAGENTA}{BG_YELLOW}{int(num / 60)} minute(s) and {num % 60} second(s) remain{RESET}", end=" ")
    updateArray(sensorArray, count)
    count = updateArray(sensorArray, count)
    aveTemp = updateAveTemp(aveTemp)
    aveSpeed = updateAveSpeed(aveSpeed)
    if(count >= 5):
        allSensorsDown = displayArray(sensorArray, status, metricSwitched)
        break
    else:
        displayArray(sensorArray, status, metricSwitched)
        check = True
        delayFunc()
        num -= 1
        if(num != 0):
            move_cursor_up(10)

# End statistics w/ after summary
if(count < 5):
    print("\n")
    status = "IDLE"
    aveTemp /= initialNum
    aveSpeed /= initialNum
    introOutroAnimation(status)
    print("\n")
    sensorArray[4].setSpeed(0)
    if(sensorArray[3].currentTemp >= 100):
        sensorArray[3].changeTemperature(sensorArray[3].currentTemp - random.randint(30, 60))
    print(f"\n\n{BLUE}{year} {make} {model} (after complete){RESET}:")
    displayArray(sensorArray, status, metricSwitched)
    for u in range(len(sensorArray)):
        if(sensorArray[u].system_health < 5):
            criticalCount += 1
        elif(sensorArray[u].system_health >= 5 and sensorArray[u].system_health < 50):
            moderateCount += 1
    print(f"\n\nAll sensor reading tests are complete for the {year} {make} {model}.")
    print(f"\n{BLUE}Conditions:{RESET}")
    print(f"* {criticalCount} sensor(s) in a critical condition (% < 5 [RED]).\n* {moderateCount} sensor(s) in a moderate condition (% >= 5 & < 50 [YELLOW]).\n* {5 - (criticalCount + moderateCount)} sensor(s) in a good condition (% >= 50 [GREEN])")
    print(f"\n{BLUE}Averages:{RESET}")
    if(not metricSwitched):
        print(f"* Ave Speed - {round(aveSpeed, 2)} MP/H")
        print(f"* Ave Temperature - {round(aveTemp, 2)} F")
    else:
        print(f"* Ave Speed - {round(convertSpeed(aveSpeed), 2)} KP/H")
        print(f"* Ave Temperature - {round(convertDegree(aveTemp), 2)} C")
elif(count >= 5):
    move_cursor_down(10)
    print(f"\nThe system health of all sensor's are critical. Replace the sensor's with new ones and then re-run for further sensor reading and safe utilization of the {year} {make} {model}.")

