from lifxlan import Light, RED
from dotenv import load_dotenv
import os
import time
from pyautogui import locateCenterOnScreen
import pygame
load_dotenv()

mac_address = os.getenv('MAC_ADDRESS')
device_ip = os.getenv('DEVICE_IP')
bulb = Light(mac_address, device_ip)

def main():
    print("Starting Goal Horn program...")

    if(not find_lights()):
    # If the light is not found, the program will exit
       return
    print("Light found!")

    scan_for_goal()

def find_lights():
    """
    This function will find the lights on the network and return the mac address and ip address of the light.
    Currently only works with one light.
    """
    print("Discovering lights...")
    trys = 0
    while trys < 10:
        try:
            bulb.set_power("on")
            return 1
        except:
            print("Error finding bulb...")
            time.sleep(1)
            trys += 1
            if trys < 10:
                print("Trying again", 10-trys, "more times...")
                time.sleep(4)
    return 0

def scan_for_goal():
    """
    This function will scan for a goal and play the horn.
    """
    print("Scanning for goal...")
    while True:
        try:
            if(locateCenterOnScreen("assets/goal.jpg", confidence=.7, region=(500, 60, 800, 130))):
                print("Goal found!")
                handle_goal()
        except:
            print("No Goal Found")
        time.sleep(1)

def handle_goal():
    """
    This function will play the goal horn and change the color of the light.
    """
    play_horn()
    original_color = bulb.get_color()
    print("Changing light color ")
    try:
        bulb.set_color(RED, rapid=True)
    except:
        print("Error changing color")
    print("Waiting 20 seconds...")
    time.sleep(20)
    print("Changing light color back to original color")
    try:
        bulb.set_color(original_color, rapid=True)
    except:
        print("Error changing color")

def play_horn():
    """
    This function will play the goal horn.
    """
    print("Playing goal horn...")
    pygame.mixer.init()
    pygame.mixer.music.load('assets/dontStopTheParty.mp3')
    pygame.mixer.music.play()

if __name__=="__main__":
    main()