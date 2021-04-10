from sklearn import tree 
#Rough 1
#Smooth 0
#Tennis 1
#Cricket 2
def MarvellousML(wight,surface):
	#Step 1 & 2
	Features = [[35,"1"],[47,"1"],[90,"0"],
				[48,"1"],[90,"0"],[35,"1"],
				[92,"0"],[35,"1"],[35,"1"],
				[35,"1"],[96,"0"],[43,"1"],
				[110,"0"],[35,"1"],[95,"0"]]

	Labele = ["1","1","2","1","2","1","2","1","1","1","2","1","2","1","2"]			

	#step 3
	dobj = tree.DecisionTreeClassifier()

	#Step 4
	dobj.fit(Features,Labele)

	#Step 5
	result = dobj.predict([[wight,surface]])
	print("Ball is",result)
	if result==['1']:
		print("Your object looks like tennis ball")
	else:
		print("Your object looks like cricket ball")
	

def main():
	print("------------- Suoervised MAchine Learning ---------------")
	print("Enter wight of object")
	wight = int(input())

	print("Enter surface type")
	surface = input()

	if surface.lower() == "rough":
		surface = 1

	elif surface.lower() == "smooth":
		surface = 0

	else:
		print("Invalide input")

	MarvellousML(wight,surface)		
	
	
if __name__ == '__main__':
		main()	


