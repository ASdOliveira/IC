import matplotlib.pyplot as plt

def plot(vector):
    plt.axis([0, 1800, 0, 1200])
    plt.plot([vector[i][1] for i in range(len(vector))], [vector[i][2] for i in range(len(vector))], '.b-')
    plt.show()
