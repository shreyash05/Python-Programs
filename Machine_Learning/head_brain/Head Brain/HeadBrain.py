import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def MeanData(arr):
	size = len(arr)
	sum = 0

	for i in range(size):
		sum = sum+arr[i]

	return (sum/size)	


def MarvellousHeadBrain(Name):
	dataset = pd.read_csv(Name)
	print("Size of dataset is",dataset.shape)

	X = dataset["Head Size(cm^3)"].values
	Y = dataset["Brain Weight(grams)"].values

	print("Length of X is:",len(X))
	print("Length of Y is:",len(Y))

	#print("Mean of X is:",MeanData(X))
	#print("Mean of X is:",np.Mean(X))

	Mean_X = MeanData(X)
	Mean_Y = MeanData(Y)

	print("Mean of independent variable is",Mean_X)
	print("Mean of dependent variable is",Mean_Y)
	# m = (Sum(X-Xb)*(Y-Yb))/Sum(X-Xb)^2

	numerator = 0
	denomenator = 0

	for i in range(len(X)):
		numerator = numerator+(X[i]-Mean_X)*(Y[i]-Mean_Y)
		denomenator = denomenator + (X[i]-Mean_X)**2

		m = numerator/denomenator
	print("Value of m is:",m)

	# Y = mX+c
	# C= Y-mX
	# C= Mean_X - (m*Mean_X)
	C = Mean_Y - (m*Mean_X)
	print("Value of C is:",C)

	X_Start = np.min(X) - 200
	X_End = np.max(X) + 200

	x = np.linspace(X_Start,X_End)
	y = m*x+C

	plt.plot(x,y,color='r',label = "Regressio Line")
	plt.scatter(X,Y,color = 'b',label  = "scatter plot")

	plt.xlabel("Head size")
	plt.ylabel("Brain wight")

	plt.legend()
	plt.show()

	#R Square casalculation
	Numerator = 0
	Denomenator = 0
	for i in range(len(X)):
		Numerator = Numerator + (((m*X[i]+C)-Mean_Y)**2)
		Denomenator = Denomenator + ((Y[i]-Mean_Y)**2)

	RSquare = Numerator/Numerator
	print("Value of RSquare is:",RSquare)
def main():
	#print("Enter file name of dtatset:")
	#name = input()

	MarvellousHeadBrain("MarvellousHeadBrain.csv")


if __name__ == '__main__':
	main()	