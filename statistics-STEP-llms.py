__author__ = 'carlosug'

'''
GOAL: basic statistic for each llm model response. 
It reports the steps detected by the LLMs, and compare with annotations.
This script iterates through each ID, calculates the number of steps detected by the LLMs for each method,
and compares it with the number of steps identified in the annotations.
 Then, it prints the ratio of detected steps to annotated steps for each method, and ID per LLM.
'''

import json

# Load instructionsResponses and instructionsAnnotations
response_files = ['Evaluation/Rouge/post-groq-responses-MISTRAL.json', 'Evaluation/Rouge/post-groq-responses-llama2.json']
instructionsAnnotations = json.load(open('Evaluation/Rouge/post-annotated.json'))

# Initialize counters
methods = {'Binary', 'Package Manager', 'Container', 'Source'}

def normalize_method(method):
    if method.lower() == 'package manager':
        return 'Package Manager'
    return method.capitalize()

# Collect data into a list of dictionaries
data = []

for response_file in response_files:
    instructionsResponses = json.load(open(response_file))
    for id_, steps in instructionsResponses.items():
        system_step_counts = {method: 0 for method in methods}
        for method, step_list in steps.items():
            normalized_method = normalize_method(method)
            for step in step_list:
                system_step_counts[normalized_method] += 1
        
        reference_step_counts = {method: 0 for method in methods}
        if id_ in instructionsAnnotations:
            for method, step_list in instructionsAnnotations[id_].items():
                normalized_method = normalize_method(method)
                for step in step_list:
                    reference_step_counts[normalized_method] += 1
        
        for method in methods:
            system_count = system_step_counts[method]
            reference_count = reference_step_counts.get(method, 0)
            if reference_count > 0:
                ratio = system_count / reference_count
            else:
                ratio = 0
            data.append({
                'ID': id_,
                'Method': method,
                'LLM Detected': system_count,
                'Annotations': reference_count,
                'Ratio': ratio,
                'LLM': 'MISTRAL' if 'MISTRAL' in response_file else 'LLAMA2'
            })

# Print the table header
print("| ID | Method           | LLM Detected | Annotations | Ratio | LLM     |")
print("|----|------------------|--------------|-------------|-------|---------|")

current_id = None

# Print each row of the table with horizontal dotted lines between IDs
for entry in data:
    if entry['ID'] != current_id:
        if current_id is not None:
            print("|----|------------------|--------------|-------------|-------|---------|")
            print("|    |                  |              |             |       |         |")
        print(f"| {entry['ID']}  | {entry['Method']:^16} | {entry['LLM Detected']:13} | {entry['Annotations']:11} | {entry['Ratio']:<5.2f} | {entry['LLM']:^7} |")
        current_id = entry['ID']
    else:
        print(f"|    | {entry['Method']:^16} | {entry['LLM Detected']:13} | {entry['Annotations']:11} | {entry['Ratio']:<5.2f} | {entry['LLM']:^7} |")

# Add a final horizontal dotted line
print("|----|------------------|--------------|-------------|-------|---------|")
