# init
basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt")
        basalt += 1
    elif("breccia" in rockToID):
        print("Found a breccia")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith")
        regolith += 1
    return

print("Artemis Rover Rock Scanner Starting")

strPath = "rocks.txt"
fileObject = open(strPath)
line = fileObject.readline()
print(line)

rockList = fileObject.readlines()

for rock in rockList:
    countMoonRocks(rock)

fileObject.close()

print("\nReport:")
print("Number of Basalt: ", basalt)
print("Number of breccia: ", breccia)
print("Number of highland: ", highland)
print("Number of regolith: ", regolith)

print("The max number of one type of rock found was:", max(basalt, breccia, highland,regolith))
print("The minimum number of one type of rock found was:", min(basalt, breccia, highland, regolith))
