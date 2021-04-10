from sklearn.datasets import load_iris
from sklearn.model_section import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

def MarvellousDecision():
	dataset = leaod_iris()

	data = dataset.data
	target = dataset.target

	data_train, data_test, target_train,target_test = target_split(data,targrt,test_size = 0.5)
	 cobj = tree.DecisionTreeClassifier()
	 
	 cobj.fit(data_train,target_train)

	 output = cobj.predict(data_test)

	 Accuracy = accuracy_score(target_test,output)

	 return Accuracy


def MarvellousKNN():
	dataset = leaod_iris()

	data = dataset.data
	target = dataset.target

	data_train, data_test, target_train,target_test = target_split(data,targrt,test_size = 0.5)
	 cobj = KNeighborsClassifier()
	 
	 cobj.fit(data_train,target_train)

	 output = cobj.predict(data_test)

	 Accuracy = accuracy_score(target_test,output)

	 return Accuracy

	 def nmain():
	 	ret = MarvellousDecision()
	 	print("Accuracy of decision tree algorithm is ",ret*100,"%")
		ret1 = MarvellousDecision()
	 	print("Accuracy of KNN algorithm is ",ret1*100,"%")

if __name__ == '__main__':
	 		main()	 	