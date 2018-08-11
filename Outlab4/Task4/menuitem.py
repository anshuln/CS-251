class MenuItem():
	def __init__(self,name='',cost=0,rating=0):
		self.name=name
		self.cost=cost
		self.rating=rating

	def __eq__(self,item2):
		return self.name==item2.name and self.cost==item2.cost and self.rating==item2.rating
	def __str__(self):
		return "Item : "+self.name + ", Cost : "+str(self.cost)+", Rating : "+str(self.rating)
	def __lt__(self,other):
		return self.rating<other.rating
	def __hash__(self):
		return hash(self.rating)	
