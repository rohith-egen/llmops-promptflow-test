from promptflow import tool
from difflib import SequenceMatcher

@tool
def similar(groundtruth: str,  prediction: str):
	return SequenceMatcher(None, groundtruth,prediction).ratio()