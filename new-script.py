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

def calculate_mean_rouge_scores(scores):
    method_means = {}
    rouge1_total = 0
    rouge2_total = 0
    rougeL_total = 0
    total_methods = len(scores)

    for method, method_scores in scores.items():
        if method_scores:
            rouge1_mean = sum(score['rouge1'].fmeasure for score in method_scores) / len(method_scores)
            rouge2_mean = sum(score['rouge2'].fmeasure for score in method_scores) / len(method_scores)
            rougeL_mean = sum(score['rougeL'].fmeasure for score in method_scores) / len(method_scores)
            method_means[method] = {'rouge1_mean': rouge1_mean, 'rouge2_mean': rouge2_mean, 'rougeL_mean': rougeL_mean}
            rouge1_total += rouge1_mean
            rouge2_total += rouge2_mean
            rougeL_total += rougeL_mean
    
    total_mean_rouge1 = rouge1_total / total_methods
    total_mean_rouge2 = rouge2_total / total_methods
    total_mean_rougeL = rougeL_total / total_methods

    return method_means, {'rouge1_mean': total_mean_rouge1, 'rouge2_mean': total_mean_rouge2, 'rougeL_mean': total_mean_rougeL}

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

def print_mean_rouge_scores(method_means, total_mean, id_number):
    print(f"Mean ROUGE scores for ID {id_number}:")
    for method, scores in method_means.items():
        print(f"Method: {method}")
        print(f"ROUGE-1 Mean: {scores['rouge1_mean']:.4f}")
        print(f"ROUGE-2 Mean: {scores['rouge2_mean']:.4f}")
        print(f"ROUGE-L Mean: {scores['rougeL_mean']:.4f}")
        print()
    
    print(f"Total Mean ROUGE scores for ID {id_number}:")
    print(f"ROUGE-1 Mean: {total_mean['rouge1_mean']:.4f}")
    print(f"ROUGE-2 Mean: {total_mean['rouge2_mean']:.4f}")
    print(f"ROUGE-L Mean: {total_mean['rougeL_mean']:.4f}")
    print()

data1 = json.load(open('Evaluation/Rouge/post-groq-responses-llama2.json'))
data2 = json.load(open('Evaluation/Rouge/post-annotated.json'))

for id_number in data1:
    instructions1 = get_instructions_per_method(data1, id_number)
    instructions2 = get_instructions_per_method(data2, id_number)
    scores = calculate_rouge_scores(instructions1, instructions2)
    if scores:
        method_means, total_mean = calculate_mean_rouge_scores(scores)
        print_mean_rouge_scores(method_means, total_mean, id_number)
    else:
        print(f"No common methods found for ID {id_number}.")
