__author__ = 'carlosug'

'''
GOAL: evaluate LLM on all tasks (work in progress). Steps:
"""Computes rouge scores between two text blobs.

Implementation replicates the functionality in the original ROUGE package. See:

Lin, Chin-Yew. ROUGE: a Package for Automatic Evaluation of Summaries. In
Proceedings of the Workshop on Text Summarization Branches Out (WAS 2004),
Barcelona, Spain, July 25 - 26, 2004.

Default options are equivalent to running:
ROUGE-1.5.5.pl -e data -n 2 -a settings.xml

Or with use_stemmer=True:
ROUGE-1.5.5.pl -m -e data -n 2 -a settings.xml

In these examples settings.xml lists input files and formats.
"""
'''

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
    rougeLsum_total = 0
    total_methods = len(scores)

    for method, method_scores in scores.items():
        if method_scores:
            rouge1_mean = sum(score['rouge1'].fmeasure for score in method_scores) / len(method_scores)
            rouge2_mean = sum(score['rouge2'].fmeasure for score in method_scores) / len(method_scores)
            rougeL_mean = sum(score['rougeL'].fmeasure for score in method_scores) / len(method_scores)
            rougeLsum_mean = sum(score['rougeLsum'].fmeasure for score in method_scores) / len(method_scores)
            method_means[method] = {'rouge1_mean': rouge1_mean, 'rouge2_mean': rouge2_mean, 'rougeL_mean': rougeL_mean, 'rougeLsum_mean': rougeLsum_mean}
            rouge1_total += rouge1_mean
            rouge2_total += rouge2_mean
            rougeL_total += rougeL_mean
            rougeLsum_total += rougeLsum_mean
    
    total_mean_rouge1 = rouge1_total / total_methods
    total_mean_rouge2 = rouge2_total / total_methods
    total_mean_rougeL = rougeL_total / total_methods
    total_mean_rougeLsum = rougeLsum_total / total_methods

    return method_means, {'rouge1_mean': total_mean_rouge1, 'rouge2_mean': total_mean_rouge2, 'rougeL_mean': total_mean_rougeL, 'rougeLsum_mean': total_mean_rougeLsum}

def calculate_rouge_scores(instructionsLLMs, instructionsAnnotations):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)
    scores = {}
    for method in instructionsLLMs:
        if method in instructionsAnnotations:
            method_scores = []
            for instruction1, instruction2 in zip(instructionsLLMs[method], instructionsAnnotations[method]):
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
        print(f"ROUGE-LSum Mean: {scores['rougeLsum_mean']:.4f}")
        print()
    
    print(f"Total Mean ROUGE scores for ID {id_number}:")
    print(f"ROUGE-1 Mean: {total_mean['rouge1_mean']:.4f}")
    print(f"ROUGE-2 Mean: {total_mean['rouge2_mean']:.4f}")
    print(f"ROUGE-L Mean: {total_mean['rougeL_mean']:.4f}")
    print(f"ROUGE-LSum Mean: {total_mean['rougeLsum_mean']:.4f}")
    print()

def calculate_total_mean(scores):
    total_mean = {'rouge1_mean': 0, 'rouge2_mean': 0, 'rougeL_mean': 0, 'rougeLsum_mean': 0}
    total_methods = 0

    for method, method_scores in scores.items():
        for score in method_scores:
            total_mean['rouge1_mean'] += score['rouge1'].fmeasure
            total_mean['rouge2_mean'] += score['rouge2'].fmeasure
            total_mean['rougeL_mean'] += score['rougeL'].fmeasure
            total_mean['rougeLsum_mean'] += score['rougeLsum'].fmeasure
            total_methods += 1

    total_mean['rouge1_mean'] /= total_methods
    total_mean['rouge2_mean'] /= total_methods
    total_mean['rougeL_mean'] /= total_methods
    total_mean['rougeLsum_mean'] /= total_methods

    return total_mean

responses = json.load(open('Evaluation/Rouge/post-groq-responses-MISTRAL.json'))
annotations = json.load(open('Evaluation/Rouge/post-annotated.json'))

total_scores = {}

for id_number in responses:
    instructionsLLMs = get_instructions_per_method(responses, id_number)
    instructionsAnnotations = get_instructions_per_method(annotations, id_number)
    scores = calculate_rouge_scores(instructionsLLMs, instructionsAnnotations)
    if scores:
        method_means, total_mean = calculate_mean_rouge_scores(scores)
        print_mean_rouge_scores(method_means, total_mean, id_number)
        for method, method_scores in scores.items():
            if method in total_scores:
                if method in total_scores:
                    total_scores[method].extend(method_scores)
                else:
                    total_scores[method] = method_scores
            else:
                total_scores[method] = method_scores
    else:
        print(f"No common methods found for ID {id_number}.")

total_mean = calculate_total_mean(total_scores)
print("Total Mean ROUGE scores for all IDs and methods:")
print(f"ROUGE-1 Mean: {total_mean['rouge1_mean']:.4f}")
print(f"ROUGE-2 Mean: {total_mean['rouge2_mean']:.4f}")
print(f"ROUGE-L Mean: {total_mean['rougeL_mean']:.4f}")
print(f"ROUGE-LSUM Mean: {total_mean['rougeLsum_mean']:.4f}")
