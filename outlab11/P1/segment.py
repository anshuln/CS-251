import PIL
import numpy as np 
import sys

def euclidean(point,mean_lake,mean_veg,mean_built,mean_sea):
	d=[(np.linalg.norm(point,mean_sea),0),(np.linalg.norm(point,mean_lake),75),(np.linalg.norm(point,mean_built),255),(np.linalg.norm(point,mean_veg),128)]
	return sorted(d)[0][1]

def man_dist(p1,p2):
	return(np.sum(np.abs(p2-p1)))

def manhattan(point,mean_lake,mean_veg,mean_built,mean_sea):
	d=[(man_dist(point,mean_sea),0),(man_dist(point,mean_lake),75),(man_dist(point,mean_built),255),(man_dist(point,mean_veg),128)]
	return sorted(d)[0][1]

if __name__=="__main__":
	if(len(sys.argv)>2):
		print("Unknown option")
	else:
		
		mean_lake=np.zeros((3,1))
		mean_veg=np.zeros((3,1))
		mean_built=np.zeros((3,1))

		sea_r=np.empty(1)
		sea_b=np.empty(1)
		sea_g=np.empty(1)
		for x in ['sea1.png','sea2.png','sea3.png']:
			I = np.asarray(PIL.Image.open(x))
			sea_r.append(I[:,:,0].ravel())
			sea_b.append(I[:,:,1].ravel())
			sea_g.append(I[:,:,2].ravel())
		mean_sea = np.array([np.mean(sea_r),np.mean(sea_b),np.mean(sea_g)])
		sea_r=np.empty(1)
		sea_b=np.empty(1)
		sea_g=np.empty(1)
		for x in ['vegetation1.png','vegetation2.png','vegetation3.png','vegetation4.png']:
			I = np.asarray(PIL.Image.open(x))
			sea_r.append(I[:,:,0].ravel())
			sea_b.append(I[:,:,1].ravel())
			sea_g.append(I[:,:,2].ravel())
		mean_veg=np.array([np.mean(sea_r),np.mean(sea_b),np.mean(sea_g)])
		sea_r=np.empty(1)
		sea_b=np.empty(1)
		sea_g=np.empty(1)
		x = 'builtup.png'
		I = np.asarray(PIL.Image.open(x))
		sea_r.append(I[:,:,0].ravel())
		sea_b.append(I[:,:,1].ravel())
		sea_g.append(I[:,:,2].ravel())
		mean_built=np.array([np.mean(sea_r),np.mean(sea_b),np.mean(sea_g)])
		sea_r=np.empty(1)
		sea_b=np.empty(1)
		sea_g=np.empty(1)
		x = 'lake.png'
		I = np.asarray(PIL.Image.open(x))
		sea_r.append(I[:,:,0].ravel())
		sea_b.append(I[:,:,1].ravel())
		sea_g.append(I[:,:,2].ravel())
		mean_lake=np.array([np.mean(sea_r),np.mean(sea_b),np.mean(sea_g)])
		
		I = np.asarray(PIL.Image.open('mumbai.png'))
		result=np.zeros((I.shape[0],I.shape[1]))
		for i in range(result.shape[0]):
			for j in range(result.shape[1]):
				if sys.argv[1]=='eu':
					result[i][j]=euclid(I[i][j],mean_lake,mean_veg,mean_built,mean_sea)
				else:
					result[i][j]=manhattan(I[i][j],mean_lake,mean_veg,mean_built,mean_sea)
		if sys.argv[1]=="eu":
			scipy.misc.imsave('segmented_eu.png',result)
		else:
			scipy.misc.imsave('segmented_man.png',result)




