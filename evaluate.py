__author__ = 'carlosug'

'''
evaluate LLM on all  tasks 
'''

import glob
import json
import os
import sys

import json
from rouge_score import rouge_scorer

def read_json_files_into_list(filenames):
    """
    Read the contents of multiple JSON files into a list.

    Parameters:
    - filenames (list): List of file paths to be read.

    Returns:
    - List of strings where each string is the content of a JSON file.
    """
    contents = []
    for filename in filenames:
        with open(filename, 'r', encoding="utf8") as file:
            data = json.load(file)
            contents.append(data["readme_instructions"])  # Assuming "readme_instructions" is the key in your JSON structure
    return contents

# Example usage:
reference_filenames = ["output.json"]  # Replace with your reference file names
prediction_filenames = ["output-responses.json"]  # Replace with your prediction file names

references = read_json_files_into_list(reference_filenames)
predictions = read_json_files_into_list(prediction_filenames)

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

cumulative_scores = {
    'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
}

# Calculate ROUGE scores and accumulate
num_samples = len(predictions)
for prediction, reference in zip(predictions, references):
    scores = scorer.score(reference, prediction)
    for metric, values in scores.items():
        cumulative_scores[metric]['precision'] += values.precision
        cumulative_scores[metric]['recall'] += values.recall
        cumulative_scores[metric]['fmeasure'] += values.fmeasure

# Average the scores
for metric, values in cumulative_scores.items():
    cumulative_scores[metric]['precision'] /= num_samples
    cumulative_scores[metric]['recall'] /= num_samples
    cumulative_scores[metric]['fmeasure'] /= num_samples

print(cumulative_scores)
