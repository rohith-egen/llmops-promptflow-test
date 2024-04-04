from promptflow import tool
import difflib

@tool
def compute_similarity(groundtruth: str,  prediction: str):
	diff = difflib.ndiff(groundtruth,  prediction)
	diff_count = 0
	for line in diff:
		if line.startswith("-"):
			diff_count += 1
	return 1 - (diff_count / len(groundtruth))