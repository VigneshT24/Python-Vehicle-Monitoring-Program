import time
import sys

def loadingAnimation():
    for seconds in range(0, 3):
        print(f"\rLoading Data{'.' * (seconds + 1)}   ", end = " ")
        time.sleep(1)
