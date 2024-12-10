from lifxlan import Light

def main():
    print("Discovering lights...")
    bulb = Light("d0:73:d5:3d:2d:05", "192.168.1.237")
    bulb.set_power("on")

def findLights():
    return 0

if __name__=="__main__":
    main()