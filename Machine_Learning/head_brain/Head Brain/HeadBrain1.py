import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrain(Name):
	dataset = pd.read_csv(Name)
	print("Size of dataset is",dataset.shape)

	X = dataset["Head Size(cm^3)"].values
	Y = dataset["Brain Weight(grams)"].values
	X = X.reshape((-1,1))
	obj = LinearRegression()
	obj.fit(X,Y)

	y_Predict = obj.predict(X)
	#Dataset = pd.read_csv("Test.csv")
	#X_new = dataset["Head size"].values
	#output = obj.predict(X_new) 
	#print("Expected Result is:",output)
	rsquare = obj.score(X,Y)

	plt.plot(x,y,color='r',label = "Regressio Line")
	plt.scatter(X,Y,color = 'b',label  = "scatter plot")

	plt.xlabel("Head size")
	plt.ylabel("Brain wight")

	plt.legend()
	plt.show()
def main():
	#print("Enter file name of dtatset:")
	#name = input()

	MarvellousHeadBrain("MarvellousHeadBrain.csv")


if __name__ == '__main__':
	main()	