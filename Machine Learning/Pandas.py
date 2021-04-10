import pandas as pd

def main():
	data = pd.read_csv('iris.csv')
	#print(data)
	#print(data.head())

	df1 = data.iloc[:10:2]
	print(df1)
if __name__ == '__main__':
		main()	