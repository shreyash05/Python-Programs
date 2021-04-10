from sklearn import tree 
#Rough 1
#Smooth 0
#Tennis 1
#Cricket 2
def main():
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
	result = dobj.predict([[40,1]])

	print("Ball is",result)
if __name__ == '__main__':
		main()	