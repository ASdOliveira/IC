from datetime import datetime

def readDB():
    # Open input file
    infile = open('berlin52.tsp', 'r')

    # Read instance header
    Name = infile.readline().strip().split()[1] # NAME
    FileType = infile.readline().strip().split()[1] # TYPE
    Comment = infile.readline().strip().split()[1] # COMMENT
    Dimension = infile.readline().strip().split()[1] # DIMENSION
    EdgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
    infile.readline()

    # Read node list
    intDimension = Dimension
    nodelist = []
    N = int(intDimension)
    for i in range(0, int(intDimension)):
        #x,y = infile.readline().strip().split()[1:]
        #nodelist.append([float(x), float(y)])
        x,y,z = infile.readline().strip().split()
        nodelist.append([int(x), float(y),float(z)])

    # Close input file
    infile.close()
    return nodelist


def writeDB(text):
    try:
        file = open("Log.txt", "a")
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        file.write(timestampStr + "  "+ text + "\n")
        file.close()
    except:
        print("lascou")