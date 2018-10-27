import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
if __name__=="__main__":
	data=np.genfromtxt("3dpd.out",delimiter=",")
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(data[:,0],data[:,1],data[:,2])
	plt.show()	
