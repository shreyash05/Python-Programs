from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

def main():
	dataset = load_iris()

	print("Features of dataset")
	print(dataset.feature_names)

	print("Target names of dataset")
	print(dataset.target_names)

	#print("Iris dataset is:")
	#for icnt in range(len(dataset.target)):
	#	print("ID: %d Feature: %s Label: %s" %(icnt, dataset.data[icnt], dataset.target[icnt]))

	index = [1,51,101]
	test_target = dataset.target[index]
	test_feature = dataset.data[index]

	train_target = np.delete(dataset.target,index)
	train_feature = np.delete(dataset.data,index,axis = 0)

	obj = tree.DecisionTreeClassifier()

	obj.fit(train_feature,train_target)

	result = obj.predict(test_feature)

	print("Result prediction by ML:",result)

	print("Result excepted:",test_target)
if __name__ == '__main__':
		main()	