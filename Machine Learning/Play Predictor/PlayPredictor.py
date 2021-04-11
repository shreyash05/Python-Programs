import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def PlayPredictor():
	#step 1
	data = pd.read_csv("PlayPredictor.csv")
	print("Dataset loaded successfully with size",len(data))

	#Prepare data
	Features = ["Whether","Temperature"]
	print("Features names are,",Features)


	Whether = data.Wether
	Temperature = data.Temperature
	play = data.Play

	lobj = preprocessing.LabelEncoder()

	WhetherX = lobj.fit_transform(Whether)
	TemperatureX = lobj.fit_transform(Temperature)
	LableX= lobj.fit_transform(play)
	
	print("*"*50)
	print("Encoded whether is")
	print(WhetherX)

	print("*"*50)
	print("Encoded tempersture is")
	print(TemperatureX)

	print("*"*50)
	print("Encoded Lable is")
	print(LableX)

	print("*"*50)

	features = list(zip(WhetherX,TemperatureX))
	Lable = list(play)
	#step 3
	obj = KNeighborsClassifier(n_neighbors = 3)
	obj.fit(features,Lable)

	#Step4
	output = obj.predict([[0,2]])
	print(output)
	output1= lobj.fit_transform(output)
	print(output1)
	if(output1 == 0):
		print("you can play")
	else:
		print("Dont play")	


def main():
	#print("____Marvellous____")
	#print("Enter the path of the file which contains dataset")
	#path = input()



	PlayPredictor()	

if __name__ == '__main__':
	main()
