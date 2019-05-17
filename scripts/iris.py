from mindsdb import Predictor
import argparse


def train():
	Predictor(name='iris_classifier').learn(
    	to_predict='species', # the column we want to learn to predict given all the data in the file
    	from_data="data/iris.csv" # the path to the file where we can learn from, (note: can be url)
	)


def predict(sepal_length, sepal_width, petal_length, petal_width):
	result = Predictor(name='iris_classifier').predict(when={'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width})
	print(f"The predicted species is {result[0]['species']} with confidence {result[0]['species_confidence']}")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--type", help="train or predict", required=True)
	parser.add_argument("--sepal_length", help="Sepal length")
	parser.add_argument("--sepal_width", help="Sepal width")
	parser.add_argument("--petal_length", help="Petal length")
	parser.add_argument("--petal_width", help="Petal width")
	args = parser.parse_args()
	if args.type == 'predict':
		predict(args.sepal_length, args.sepal_width, args.petal_length, args.petal_width)
	else: 
		train()
