def readfromtxt():
    with open("requests.txt", "r") as f:
        return f.read()

print(readfromtxt())
