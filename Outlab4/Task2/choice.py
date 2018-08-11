import random
import pickle
import sys
def fill_choice(file):
	l=[]
	alpha="QWERTYUIOPASDFGHJKLZXCVBNM"
	while(len(l)<100):
		j=random.randint(1,5000)
		while j in [x[0] for x in l]:
			j=random.randint(1,5000)
		name=alpha[random.randint(0,25)]+alpha[random.randint(0,25)]+alpha[random.randint(0,25)]
		l.append([j,name])
	pickle.dump(l,open(file,"wb"))

def ask_choice(file):
	numbers=pickle.load(open(file,"rb"))
	a=int(input("Enter a number between 5000 and 7000\n"))
	while(a not in range(5000,7001)):
		a=int(input("Enter a number between 5000 and 7000\n"))
		print(a)
	buff=[]
	for i in range(0,len(numbers)):
		for j in range(i+1,len(numbers)):
			if(numbers[i][0]+numbers[j][0] == a):
				print(numbers[i][1]+" "+str(numbers[i][0])+" "+numbers[j][1]+" "+str(numbers[j][0]))
				return
			elif(numbers[i][0]+numbers[j][0] < a):
				buff=[i,j]
	if(len(buff)):
		print(numbers[buff[0]][1],numbers[buff[0]][0],numbers[buff[1]][1],numbers[buff[1]][0])
	else:
		print("No numbers found")

if __name__=="__main__":

	file=sys.argv[1]
	fill_choice(file)
	ask_choice(file)

