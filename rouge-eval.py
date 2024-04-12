# This script first loads the data from the two JSON files.
# It then finds the common IDs between the two datasets.
# For each common ID, it normalizes the method names and finds the common methods (e.g. CAPITAL letters).
# If there are common methods, it gets the instructions for each method and
# calculates the ROUGE scores if the number of instructions match. 
#If the number of instructions do not match, it prints a message.
#If there are no common methods, it also prints a message.
import json
from rouge_score import rouge_scorer

def normalize_method_name(method):
    return method.lower().replace(' ', '_')

def get_instructions_per_method(data, id_number):
    instructions = []
    if id_number in data:
        for method, steps in data[id_number].items():
            instructions.extend(steps)
    return instructions

def calculate_rouge_scores(instructions1, instructions2):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = []
    for instruction1, instruction2 in zip(instructions1, instructions2):
        if instruction1 and instruction2:
            rouge_scores = scorer.score(instruction1, instruction2)
            scores.append(rouge_scores)
    return scores

def print_rouge_scores(scores, id_number):
    print(f"ROUGE scores for ID {id_number}:")
    for score in scores:
        print(f"ROUGE-1: {score['rouge1'].fmeasure:.4f}")
        print(f"ROUGE-2: {score['rouge2'].fmeasure:.4f}")
        print(f"ROUGE-L: {score['rougeL'].fmeasure:.4f}")
        print()

data1 = json.load(open('Evaluation/Rouge/post-groq-responses-llama2.json'))
data2 = json.load(open('Evaluation/Rouge/post-annotated.json'))

methods = {'binary', 'package manager', 'container', 'source'}

for id_number in data1:
    instructions1 = get_instructions_per_method(data1, id_number)
    instructions2 = get_instructions_per_method(data2, id_number)
    if len(instructions1) != len(instructions2):
        print(f"Number of instructions for ID {id_number} do not match.")
    else:
        scores = calculate_rouge_scores(instructions1, instructions2)
        print_rouge_scores(scores, id_number)
