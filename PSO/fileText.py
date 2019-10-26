"File destinated to handle the Log File"
def readDB(filename,size):
    # Open input file
    infile = open(filename + ".txt", 'r')
 
    # Read node list
    nodelist = []
    for i in range(0,size):

        x = infile.readline().strip()
        nodelist.append([float(x),i])
   
    infile.close()
    return nodelist


def writeDB(file,text):
    try:
        file = open(file +".txt", "a")
        file.write(text + "\n")
        file.close()
    except:
        print("Can't open the Log file")