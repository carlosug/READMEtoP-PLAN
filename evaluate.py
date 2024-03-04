__author__ = 'carlosug'

'''
evaluate LLM on all tasks (work in progress)
'''

import json





# def add_id_to_messages(json_file_path):
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
#         messages = data['messages']
#         for idx, message in enumerate(messages):
#             if message['role'] == 'assistant':
#                 message['id'] = '(idx + 0)/2'  # Adding 1 to start IDs from 1
#                 # message['id'[+1]] = + 1
#         with open(json_file_path, 'w') as outfile:
#             json.dump(data, outfile, indent=4)

# # Add "id" to each assistant message in the JSON file
# add_id_to_messages('scr/groq-responses-llama2-copy.json')

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_plans_from_ground_truth(ground_truth):
    plans = {}
    for software in ground_truth['study_subjects']['research_software']:
        plans[software['id']] = [plan['type'] for plan in software['plans']]
    return plans

import re

def extract_plans_from_responses(responses):
    plans_by_id = {}
    for message in responses['messages']:
        if message['role'] == 'assistant':
            software_id = message['id']
            content = message['content'].lower()
            start_index = content.find("\n\nthe other installation methods") # for LLAMA responses
            modified_content = content[:start_index] # for LLAMA responses
            print(modified_content[0:400]) # for LLAMA responses
            found_plans = re.findall(r'\b(source|binary|container|package manager)\b', modified_content)
            unique_plans = set(method.title() for method in found_plans)
            if software_id not in plans_by_id:
                plans_by_id[software_id] = list(unique_plans)
            else:
                plans_by_id[software_id].extend(unique_plans)
                plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
    return plans_by_id

# def extract_plans_from_responses(responses):
#     plans_by_id = {}
#     for message in responses['messages']:
#         if message['role'] == 'assistant':
#             software_id = message['id']
#             content = message['content'].lower()
#             found_plans = re.findall(r'\b(source|binary|container|package manager)\b', content)
#             unique_plans = set(method.title() for method in found_plans)
#             if software_id not in plans_by_id:
#                 plans_by_id[software_id] = list(unique_plans)
#             else:
#                 plans_by_id[software_id].extend(unique_plans)
#                 plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
#     return plans_by_id

def calculate_accuracy(ground_truth_plans, response_plans):
    correct = 0
    total = sum(len(plans) for plans in ground_truth_plans.values())
    for software_id, plans in ground_truth_plans.items():
        if software_id in response_plans:
            correct += len(set(plans) & set(response_plans[software_id]))
    return correct / total if total > 0 else 0

def calculate_precision_recall_f1(ground_truth_plans, response_plans):
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    for software_id, plans in ground_truth_plans.items():
        if software_id in response_plans:
            true_positives += len(set(plans) & set(response_plans[software_id]))
            false_positives += len(set(response_plans[software_id]) - set(plans))
        false_negatives += len(set(plans) - set(response_plans[software_id])) if software_id in response_plans else len(plans)
    
    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    
    return precision, recall, f1



ground_truth = load_data('scr/data/ground_true_plan_steps_new.json')
# responses = load_data('scr/groq-responses-mistralEVAL.json')
responses_LLAMA = load_data('scr/groq-responses-llama2-copy.json')
responses_MISTRAL = load_data('scr/groq-responses-mistralEVAL.json')
ground_truth_plans = extract_plans_from_ground_truth(ground_truth)
# print(ground_truth_plans)
response_plans = extract_plans_from_responses(responses_LLAMA)
print(response_plans)

print(f"{'ID':<10}{'Response plans':<30}{'Ground Truth plans':<30}")
for software_id in ground_truth_plans:
    gt_plans = ', '.join(ground_truth_plans[software_id])
    resp_plans = ', '.join(response_plans[software_id]) if software_id in response_plans else 'N/A'
    print(f"{software_id:<10}{resp_plans:<30}{gt_plans:<30}")
    
accuracy = calculate_accuracy(ground_truth_plans, response_plans)
print(f'Accuracy: {accuracy:.2%}')
precision, recall, f1 = calculate_precision_recall_f1(ground_truth_plans, response_plans)
print(f'Precision: {precision:.2%}')
print(f'Recall: {recall:.2%}')
print(f'F1 Score: {f1:.2%}')

# import glob
# import json
# import os
# import sys

# import json
# from rouge_score import rouge_scorer

# def read_json_files_into_list(filenames):
#     """
#     Read the contents of multiple JSON files into a list.

#     Parameters:
#     - filenames (list): List of file paths to be read.

#     Returns:
#     - List of strings where each string is the content of a JSON file.
#     """
#     contents = []
#     for filename in filenames:
#         with open(filename, 'r', encoding="utf8") as file:
#             data = json.load(file)
#             contents.append(data["readme_instructions"])  # Assuming "readme_instructions" is the key in your JSON structure
#     return contents

# # Example usage:
# reference_filenames = ["output.json"]  # Replace with your reference file names
# prediction_filenames = ["output-responses.json"]  # Replace with your prediction file names

# references = read_json_files_into_list(reference_filenames)
# predictions = read_json_files_into_list(prediction_filenames)

# scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

# cumulative_scores = {
#     'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
# }

# # Calculate ROUGE scores and accumulate
# num_samples = len(predictions)
# for prediction, reference in zip(predictions, references):
#     scores = scorer.score(reference, prediction)
#     for metric, values in scores.items():
#         cumulative_scores[metric]['precision'] += values.precision
#         cumulative_scores[metric]['recall'] += values.recall
#         cumulative_scores[metric]['fmeasure'] += values.fmeasure

# # Average the scores
# for metric, values in cumulative_scores.items():
#     cumulative_scores[metric]['precision'] /= num_samples
#     cumulative_scores[metric]['recall'] /= num_samples
#     cumulative_scores[metric]['fmeasure'] /= num_samples

# print(cumulative_scores)
