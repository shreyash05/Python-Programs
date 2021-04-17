import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from statistics import *
class AdvertisementAgency:
	def __init__(self):
		self.dataset = pd.read_csv("Advertising.csv")
		self.X = self.dataset.TV
		self.Y = self.dataset.radio
		self.mean_X = mean(self.X)
		self.mean_Y = mean(self.Y)
		
	def slope_of_advertisement_data(self):

		numerator = 0
		denomenator = 0
		size = len(self.X)
		for i in range(size):
			numerator = numerator+(self.X[i]-self.mean_X)*(self.Y[i]-self.mean_Y)
			denomenator = denomenator + (self.X[i]-self.mean_X)**2
			slope = numerator/denomenator
		print("slope of line is:",slope)	
		return slope

	def constant_value_of_advertisement_data(self,slope):
		constant = self.mean_Y - (slope*self.mean_X)
		print("Value of constant is:",constant)
		return constant

	def r_square_value_of_advertisement_data(self):
		numerator = 0
		denomenator = 0
		size = len(self.Y)
		for i in range(size):
			numerator = numerator+(self.mean_Y-self.Y[i])**2
			denomenator = denomenator+(self.Y[i]-self.mean_Y)**2

			rsquare = numerator/denomenator
		print("R suare value is :",rsquare) 	

	def plot_advertisment_data(self,slope,constant):
		xstart = np.min(self.X)
		xend = np.max(self.X)

		x = np.linspace(xstart,xend)
		y = slope*x+constant

		plt.plot(x,y,color='r',label = "Regressio Line")
		plt.scatter(self.X,self.Y,color = 'b',label  = "scatter plot")

		plt.xlabel("Head size")
		plt.ylabel("Brain wight")

		plt.legend()
		plt.show()	



def main():
	obj = AdvertisementAgency()
	ret = obj.slope_of_advertisement_data()
	ret1 = obj.constant_value_of_advertisement_data(ret)
	obj.r_square_value_of_advertisement_data()
	obj.plot_advertisment_data(ret,ret1)
	#slope_of_advertisement_agency()
	#constant_value_of_advertisement_Agency()
if __name__ == '__main__':
		main()	
