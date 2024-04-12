import json
from rouge_score import rouge_scorer

def normalize_method_name(method):
    return method.lower().replace(' ', '_')

def get_instructions_per_method(data, id_number):
    instructions = {}
    if id_number in data:
        for method, steps in data[id_number].items():
            instructions[normalize_method_name(method)] = steps
    return instructions

def calculate_rouge_scores(instructions1, instructions2):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = {}
    for method in instructions1:
        if method in instructions2:
            method_scores = []
            for instruction1, instruction2 in zip(instructions1[method], instructions2[method]):
                if instruction1 and instruction2:
                    rouge_scores = scorer.score(instruction1, instruction2)
                    method_scores.append(rouge_scores)
            scores[method] = method_scores
    return scores

def print_rouge_scores(scores, id_number):
    print(f"ROUGE scores for ID {id_number}:")
    for method, method_scores in scores.items():
        print(f"Method: {method}")
        for score in method_scores:
            print(f"ROUGE-1: {score['rouge1'].fmeasure:.4f}")
            print(f"ROUGE-2: {score['rouge2'].fmeasure:.4f}")
            print(f"ROUGE-L: {score['rougeL'].fmeasure:.4f}")
            print()

data1 = json.load(open('Evaluation/Rouge/post-groq-responses-llama2.json'))
data2 = json.load(open('Evaluation/Rouge/post-annotated.json'))

for id_number in data1:
    instructions1 = get_instructions_per_method(data1, id_number)
    instructions2 = get_instructions_per_method(data2, id_number)
    scores = calculate_rouge_scores(instructions1, instructions2)
    if scores:
        print_rouge_scores(scores, id_number)
    else:
        print(f"No common methods found for ID {id_number}.")
