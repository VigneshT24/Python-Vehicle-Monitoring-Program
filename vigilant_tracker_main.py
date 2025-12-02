import random
import time
from vigilant_tracker_sensor import UltrasonicSensor, CameraSensor, RadarSensor, TemperatureSensor, SpeedSensor
from loading_animation import loadingAnimation

def displayArray(sensorArray, status, metricSwitched):
    """
    Displays formatted sensor data in a table-like structure with color-coded health indicators.

    Args:
        sensorArray (list): Array of sensor objects containing ID, health, temperature, and speed data
        status (str): Current vehicle status (e.g., "Active", "IDLE")
        metricSwitched (bool): True for metric units (C, KP/H), False for imperial (F, MP/H)
    """
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

def updateArray(sensorArray, count, initialTimer, currentTimer):
    """
    Updates sensor health, temperature, and speed values with random variations to simulate real-time changes.

    Args:
        sensorArray (list): Array of sensor objects to update
        count (int): Counter tracking number of critical sensors (health < 5%)

    Returns:
        int: Updated count of critical sensors, or 0 if none are critical
    """
    if(not check and sensorArray[4].currentSpeed >= 20):
        sensorArray[4].setSpeed(0)
    if(not check and sensorArray[3].currentTemp < 90):
        sensorArray[3].changeTemperature(90)

    # realistic runtime system health updater
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

    # temperature control (realistically random)
    if(flip == 0):
        if(sensorArray[3].currentTemp < 180):
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp + random.randint(0, 2))
        else:
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp / 2)
    else:
        if(sensorArray[3].currentTemp >= 15):
            krand = random.randint(0, 1)
            if(krand == 1):
                sensorArray[3].changeTemperature(sensorArray[3].currentTemp - random.randint(0, 2))
        else:
            sensorArray[3].changeTemperature(sensorArray[3].currentTemp + random.randint(60, 100))

    # speed control (increases in the first half then decreases in the second half)
    flip = 0 if (currentTimer < (initialTimer / 2)) else 1
    if (currentTimer == 0): # the vehicle must start from 0 speed
        sensorArray[4].setSpeed(0)
    if (flip == 0):
        if (sensorArray[4].currentSpeed >= 3):
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed - random.randint(0, 3))
        else:
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed + random.randint(5, 15))
    else:
        if (sensorArray[4].currentSpeed < 165):
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed + random.randint(0, 3))
        else:
            sensorArray[4].setSpeed(sensorArray[4].currentSpeed - random.randint(10, 25))
    return 0

def move_cursor_up(lines):
    """
    Moves terminal cursor up by specified number of lines using ANSI escape codes.

    Args:
        lines (int): Number of lines to move cursor up
    """
    print(f"\033[{lines}A", end='')

def move_cursor_down(lines):
    """
    Moves terminal cursor down by specified number of lines using ANSI escape codes.

    Args:
        lines (int): Number of lines to move cursor down
    """
    print(f"\033[{lines}B", end='')

def delayFunc():
    """
    Pauses program execution for 1 second.
    """
    time.sleep(1)

def fixFormat(userStr):
    """
    Capitalizes the first letter of each word in a string.

    Args:
        userStr (str): Input string to format

    Returns:
        str: Formatted string with each word capitalized
    """
    newStr = list(userStr.capitalize())
    for r in range(1, len(newStr)):
        if(newStr[r - 1] == " "):
            newStr[r] = newStr[r].upper()
    return "".join(newStr)

def introOutroAnimation(status):
    """
    Displays an animated loading message for vehicle state transitions.

    Args:
        status (str): Vehicle status - "Active" for starting, any other value for stopping
    """
    for seconds in range(0, 3):
        if(status == "Active"):
            print(f"\rStarting Vehicle to Motion{'.' * (seconds + 1)}   ", end = " ")
        else:
            print(f"\rStopping Vehicle from Motion{'.' * (seconds + 1)}   ", end=" ")
        time.sleep(1)

def updateAveTemp(aveTemp):
    """
    Adds current temperature reading to cumulative average temperature.

    Args:
        aveTemp (float): Current cumulative temperature sum

    Returns:
        float: Updated cumulative temperature sum
    """
    aveTemp += sensorArray[3].currentTemp
    return aveTemp

def updateAveSpeed(aveSpeed):
    """
    Adds current speed reading to cumulative average speed.

    Args:
        aveSpeed (float): Current cumulative speed sum

    Returns:
        float: Updated cumulative speed sum
    """
    aveSpeed += sensorArray[4].currentSpeed
    return aveSpeed

def convertDegree(currentTemp):
    """
    Converts temperature from Fahrenheit to Celsius.

    Args:
        currentTemp (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (currentTemp - 32) * (5/9)

def convertSpeed(currentSpeed):
    """
    Converts speed from miles per hour to kilometers per hour.

    Args:
        currentSpeed (float): Speed in MP/H

    Returns:
        float: Speed in KP/H
    """
    return currentSpeed * 1.609

def reprompt_for_errors(user_response):
    """
    Confirms user input and allows them to re-enter if incorrect.

    Args:
        user_response (str, int, or bool): The original input from the user to confirm

    Returns:
        str: The confirmed or corrected user input
    """
    while True:
        # Ask for confirmation
        confirmation = input(f"You entered: '{user_response.capitalize() if isinstance(user_response, str) else user_response}'. "
                             f"Is this correct? (yes/no): ").lower().strip()

        # Validate yes/no response
        if confirmation == "yes" or confirmation == "y":
            return user_response
        elif confirmation == "no" or confirmation == "n":
            # Ask user to re-enter
            user_response = input("Please re-enter your response: ").strip()
        else:
            # Invalid response, ask again
            print("Invalid input. Please enter 'yes' or 'no'.")

# ========================================
# GLOBAL VARIABLES
# ========================================
sensorArray = [UltrasonicSensor(), CameraSensor(), RadarSensor(), TemperatureSensor(), SpeedSensor()]

# ANSI Color Codes for Terminal Output
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BRIGHT_MAGENTA = "\033[95m"
BG_YELLOW = "\033[43m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Program State Variables
status = "Active"
check = False
criticalCount = 0
moderateCount = 0
count = 0
aveSpeed = 0
aveTemp = 0
initialNum = 0
metricSwitched = False

# ========================================
# PROGRAM INTRODUCTION
# ========================================
print("\t\t\t\tVigilantTrack: Dynamic Vehicle Health Monitor\n")
print("In this program, you will add one vehicle of your choice to do a sensor reading where you will see the sensor data live (as it is changing).")
print("If all the sensor's health percent were to reach below 5%, the vehicle would stop immediately and give you the next steps.")
print("The vehicle would be in motion and active while the sensor reading is in progress.")
print("Simulation has been SCALED, meaning the health of the sensor goes down faster than in real-life for a quicker analysis and better gist.\n")
print("Advanced Feature Overview:\n> Predictive Maintenance Module\n> Adaptive Sensor Calibration\n> Fault Tolerant Framework\n> Real-time Data Visualization\n> Sensor Fusion Algorithm\n")


# ========================================
# USER INPUT: VEHICLE DETAILS
# ========================================
make = fixFormat(input("Enter the make of the vehicle: "))
make = reprompt_for_errors(make).capitalize()
model = fixFormat(input("Enter the model of the vehicle: "))
model = reprompt_for_errors(model).capitalize()
electric = fixFormat(input(f"Is the {make} {model} electric (True/False): "))
while(electric != "True" and electric != "False"):
    electric = fixFormat(input("Make sure to enter either True or False: "))
electric = reprompt_for_errors(electric)
color = fixFormat(input(f"What color is the {make} {model}: "))
while(color.isdigit()):
    color = fixFormat(input("Please enter a valid color. A color cannot be expressed in numbers: "))
color = reprompt_for_errors(color).capitalize()
while True:
    try:
        year = int(input(f"What year is the {make} {model}: "))
        while(year < 1880 or year > 2025):
            year = int(input(f"Please enter a valid year for {make} {model}: "))
        year = reprompt_for_errors(year)
        break
    except ValueError:
        print("You entered string instead of numbers. Please enter the year again.\n")
        continue

# ========================================
# DISPLAY VEHICLE DATA
# ========================================
loadingAnimation()

# Vehicle detail printed in an arrowhead format
print(f"\n\nVEHICLE DATA:\n\t\t\t[Vehicle Make: {make}]\n\n\t\t\t\t\t\t[Vehicle Model: {model}]\n\n\t\t\t\t\t\t\t\t\t[Electric: {electric}]\n\n\t\t\t\t\t\t[Vehicle Color: {color}]\n\n\t\t\t[Vehicle Year: {year}]\n\n")

# ========================================
# USER INPUT: SENSOR READING CONFIGURATION
# ========================================
# Get duration and metric performance
while True:
    try:
        num = int(input("How long do you want the sensor reading to measure for in seconds (>0): "))
        initialNum = num
        while(initialNum == 0):
            initialNum = int(input("Input must not be 0. Only seconds greater than 0 are accepted: "))
        try:
            needMetric = (input("Type 'True' for metric convertion (KP/H, C) or press enter for default (MP/H, F): ")).lower()
            if(needMetric == "true"):
                metricSwitched = True
        except ValueError:
            print("Type either 'True' or 'False'. No other input is accepted.")
        break
    except ValueError:
        print("Cannot input string instead of numbers. Try again\n")

# ========================================
# SENSOR MONITORING LOOP
# ========================================
introOutroAnimation(status)

# Display header
print(f"\n\n{BLUE}{year} {make} {model} (before complete){RESET}:")
print("\t   UltraSonic     Camera     Radar     Temperature     Speed")

# Real-time sensor monitoring
while (num > 0):
    # Display countdown timer
    print(f"\r{BOLD}{BRIGHT_MAGENTA}{BG_YELLOW}{int(num / 60)} minute(s) and {num % 60} second(s) remain{RESET}",end=" ")
    # Update sensor data
    count = updateArray(sensorArray, count, initialNum, num)
    aveTemp = updateAveTemp(aveTemp)
    aveSpeed = updateAveSpeed(aveSpeed)
    # Check if all sensors are critical
    if (count >= 5):
        allSensorsDown = displayArray(sensorArray, status, metricSwitched)
        break
    else:
        # Display current sensor readings
        displayArray(sensorArray, status, metricSwitched)
        check = True
        delayFunc()
        num -= 1
        # Move cursor up for live animation effect
        if (num != 0):
            move_cursor_up(10)

# ========================================
# POST-MONITORING SUMMARY
# ========================================
# Normal completion (sensors still functional)
if(count < 5):
    print("\n")
    status = "IDLE"

    # Calculate averages
    aveTemp /= initialNum
    aveSpeed /= initialNum

    # Stop vehicle animation
    introOutroAnimation(status)
    print("\n")

    # Reset sensor values to idle state
    sensorArray[4].setSpeed(0)
    if(sensorArray[3].currentTemp >= 100):
        sensorArray[3].changeTemperature(sensorArray[3].currentTemp - random.randint(30, 60))

    # Display final sensor state
    print(f"\n\n{BLUE}{year} {make} {model} (after complete){RESET}:")
    displayArray(sensorArray, status, metricSwitched)

    # Count sensors by condition
    for u in range(len(sensorArray)):
        if(sensorArray[u].system_health < 5):
            criticalCount += 1
        elif(sensorArray[u].system_health >= 5 and sensorArray[u].system_health < 50):
            moderateCount += 1

    # Display summary statistics
    print(f"\n\nAll sensor reading tests are completed for the {year} {make} {model}.")
    print(f"\n{BLUE}Conditions:{RESET}")
    print(f"* {criticalCount} sensor(s) in a critical condition (% < 5 [RED]).\n* {moderateCount} sensor(s) in a moderate condition (% >= 5 & < 50 [YELLOW]).\n* {5 - (criticalCount + moderateCount)} sensor(s) in a good condition (% >= 50 [GREEN])")
    print(f"\n{BLUE}Averages:{RESET}")
    if(not metricSwitched):
        print(f"* Ave Speed - {round(aveSpeed, 2)} MP/H")
        print(f"* Ave Temperature - {round(aveTemp, 2)} F")
    else:
        print(f"* Ave Speed - {round(convertSpeed(aveSpeed), 2)} KP/H")
        print(f"* Ave Temperature - {round(convertDegree(aveTemp), 2)} C")

# Critical failure (all sensors failed)
elif(count >= 5):
    move_cursor_down(10)
    print(f"\nThe system health of all sensor's are critical. Replace the sensor's with new ones and then re-run for further sensor reading and safe utilization of the {year} {make} {model}.")