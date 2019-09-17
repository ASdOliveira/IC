import matplotlib.pyplot as plt
vector = []
vector = [[5, 845.0, 655.0], [6, 880.0, 660.0], [4, 945.0, 685.0], [10, 650.0, 1130.0], [9, 580.0, 1175.0]]
plt.plot([vector[0][1], vector[1][1], vector[2][1], vector[3][1],vector[4][1]], [vector[0][2], vector[1][2], vector[2][2], vector[3][2],vector[4][2]], 'ro')
plt.axis([0, 2000, 0, 2000])
plt.show()
#improve the printing way!