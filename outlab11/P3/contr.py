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
	classes=np.zeros((len(topics),4))
	for x in range(len(count_for_topics)):
		classes[x][0]=count_for_topics[x]["Essential"]
		classes[x][1]=count_for_topics[x]['Dont care one way or another']
		classes[x][2]=count_for_topics[x]['Nice to have']
		classes[x][3]=count_for_topics[x]['Utterly useless']
	classes=classes/len(data[1:])
	graph=np.zeros(len(topics))
	for x in range(len(topics)):
		for i in range(0,4):
			if(classes[x][i]!=0):
				graph[x]+=np.log2(classes[x][i])
	# p=np.multiply(dont_care,np.log2(dont_care)) +np.multiply(useless,np.log2(useless)) +np.multiply(nice,np.log2(nice)) +np.multiply(essentials,np.log2(essentials)) 
	graph=graph*-1
	g=[(graph[x],topics[x]) for x in range(len(topics))]
	g=sorted(g)
	# print(g[0][1])
	# plt.xticks(ind)
	q=plt.bar(np.arange(len(topics)),[g[x][0] for x in range(len(g))])
	plt.show()