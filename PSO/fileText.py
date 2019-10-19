"File destinated to handle the Log File"
def readDB():
    # Open input file
    infile = open('Log.txt', 'r')
 
    # Read node list
    nodelist = []
    """
    while (x != 'END'):
        #x,y = infile.readline().strip().split()[1:]
        #nodelist.append([float(x), float(y)])
        x,y,z = infile.readline().strip().split()
        nodelist.append([int(x), float(y),float(z)])

    # Close input file"""
    infile.close()
    return nodelist


def writeDB(text):
    try:
        file = open("Log.txt", "a")
        file.write(text + "\n")
        file.close()
    except:
        print("Can't open the Log file")