import csv
import matplotlib.pyplot as plt 
import numpy as np 
if __name__=="__main__":
	file=open("survey_data.csv","r")
	r=csv.reader(file)
	data=list(r)
	topics=data[0]
	topics=topics[1:]
	count_for_topics=[]
	for x in topics:
		# ‘’, ‘’, ‘’, ‘’
		dict={'Essential':0,'Dont care one way or another':0,'Nice to have':0,'Utterly useless':0}
		count_for_topics.append(dict)
	# print(data)
	for x in data[1:]:
		# print(x)
		for i in range(1,len(topics)+1):
			count_for_topics[i-1][x[i]]+=1
	essentials=[]
	dont_care=[]
	nice=[]
	useless=[]
	for x in count_for_topics:
		essentials.append(x["Essential"])
		dont_care.append(x['Dont care one way or another'])
		nice.append(x['Nice to have'])
		useless.append(x['Utterly useless'])
		print(x["Essential"]+x['Dont care one way or another']+x['Nice to have']+x['Utterly useless'])
	ind = np.arange(len(topics))
	width = 0.5
	p1 = plt.bar(ind, essentials, width,color='r')
	p2 = plt.bar(ind, dont_care, width,bottom=essentials,color='b')
	p3 = plt.bar(ind, nice, width,bottom=np.array(dont_care)+np.array(essentials),color='g')
	p4 = plt.bar(ind,useless,width,bottom=np.array(nice)+np.array(essentials)+np.array(dont_care),color='c')
	plt.xticks(ind, topics)
	plt.yticks(np.arange(0, 16, 1))
	plt.show()
	print(essentials)
	print(dont_care)
	print(nice)
	print(useless)