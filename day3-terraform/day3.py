regions = ["canadacentral", "canadaeast" , "eastus"]

with open("regions.txt", "w") as f:
    for region in regions:
        f.write(region + "\n")


with open("regions.txt") as f:
    for line in f:
        print(line.strip())
