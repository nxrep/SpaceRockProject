# shorter and easier expandable version of tutorial code

# init
rockTypes={
    "basalt":0,
    "breccia":0,
    "highland":0,
    "regolith":0
}

# main
print("Artemis Rover Rock Scanner Starting")

strPath = "rocks2.txt"
fileObject = open(strPath)
rockList = fileObject.readlines()

for rock in rockList:
    rockTypes[rock.lower().strip()]+=1

fileObject.close()

rockTypesSorted=dict(sorted(rockTypes.items(),key=lambda x:x[1], reverse=True))

print("\nArtemis Moon Rocks Report:")
print(f"Total rocks found: {sum(rockTypes.values())}")
print(f"Number of different rocks {len(rockTypes)} \n")

for rock in rockTypesSorted:
    print(f"Number of {rock}: {rockTypesSorted[rock]}")