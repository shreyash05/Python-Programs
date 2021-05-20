import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def predict_wine_class():
	wine_data = pd.read_csv("wine_predictor.csv")
	wine_contents = ["Malic acid","Alcalinity of ash","Magnesium","Flavanoids","Proline"]
	print("wine contents are,",wine_contents)
	malic_acide = wine_data.malicAcid
	alcalinity = wine_data.alcalinityOfAsh
	magnesium = wine_data.magnesium
	flavanoids = wine_data.flavanoids
	proline = wine_data.proline
	wine_class = wine_data.wineClass	
	knn_object = KNeighborsClassifier()
	wine_features = list(zip(malic_acide,alcalinity,magnesium,flavanoids,proline))
	wine_lable = list(wine_class)
	input_value = knn_object.fit(wine_features,wine_lable)
	output = knn_object.predict([[12.77,16,80,1.25,372]])
	return(output)

def main():
	class_of_wine=predict_wine_class()
	print("Class of wine is:",class_of_wine)	

if __name__ == '__main__':
		main()	