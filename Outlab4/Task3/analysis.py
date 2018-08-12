import numpy as np 
import csv
def read_from_csv(path):
	reader=csv.reader(open(path))
	data=list(reader)
	array=[]
	for row in range(1,len(data)):
		try:
			array.append([float(x) for x in data[row]])
	return np.array(array)
if __name__=="__main__":
	# data=pd.read_csv("info_day.csv")
	x=read_from_csv("info_day.csv")
	std=np.std(x,axis=0)
	mean=np.mean(x,axis=0)
	fields=["Temperature", "Humidity","Light","CO2" ]
	print("Field\t\tMean\t\tStd. Dev. ")
	for i in range(len(fields)):
		printer=fields[i]+"\t"+str(mean[i])+"\t"+str(std[i])
		print(printer)
		

