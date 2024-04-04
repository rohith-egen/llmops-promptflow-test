from promptflow import tool


@tool
def similar(groundtruth: str, prediction: str):
	groundtruth = groundtruth + ' ' * (len(prediction) - len(groundtruth))
	prediction = prediction + ' ' * (len(groundtruth) - len(prediction))
	return sum(1 if i == j else 0
			for i, j in zip(groundtruth, prediction)) / float(len(groundtruth))