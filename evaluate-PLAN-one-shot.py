__author__ = 'carlosug'

'''
evaluate LLM on all tasks (work in progress)
'''


#### ONE FILE ###
# import json





# # def add_id_to_messages(json_file_path):
# #     with open(json_file_path, 'r') as file:
# #         data = json.load(file)
# #         messages = data['messages']
# #         for idx, message in enumerate(messages):
# #             if message['role'] == 'assistant':
# #                 message['id'] = '(idx + 0)/2'  # Adding 1 to start IDs from 1
# #                 # message['id'[+1]] = + 1
# #         with open(json_file_path, 'w') as outfile:
# #             json.dump(data, outfile, indent=4)

# # # Add "id" to each assistant message in the JSON file
# # add_id_to_messages('RESULTS/groq-responses-llama2-copy.json')

# def load_data(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# def extract_plans_from_ground_truth(ground_truth):
#     plans = {}
#     for software in ground_truth['study_subjects']['research_software']:
#         plans[software['id']] = [plan['type'] for plan in software['plans']]
#     return plans

# import re

# def extract_plans_from_responses(responses):
#     plans_by_id = {}
#     for message in responses['messages']:
#         if message['role'] == 'assistant':
#             software_id = message['id']
#             content = message['content'].lower()
#             start_index = content.find("\n  \"no_provided\":") # for LLAMA responses
#             modified_content = content[:start_index] # for LLAMA responses
#             # print(modified_content[0:8]) # for LLAMA responses
#             found_plans = re.findall(r'\b(source|binary|container|package manager)\b', modified_content)
#             unique_plans = set(method.title() for method in found_plans)
#             if software_id not in plans_by_id:
#                 plans_by_id[software_id] = list(unique_plans)
#             else:
#                 plans_by_id[software_id].extend(unique_plans)
#                 plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
#                 print(unique_plans)
#     return plans_by_id

# # def extract_plans_from_responses(responses):
# #     plans_by_id = {}
# #     for message in responses['messages']:
# #         if message['role'] == 'assistant':
# #             software_id = message['id']
# #             content = message['content'].lower()
# #             found_plans = re.findall(r'\b(source|binary|container|package manager)\b', content)
# #             unique_plans = set(method.title() for method in found_plans)
# #             if software_id not in plans_by_id:
# #                 plans_by_id[software_id] = list(unique_plans)
# #             else:
# #                 plans_by_id[software_id].extend(unique_plans)
# #                 plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
# #     return plans_by_id

# def calculate_accuracy(ground_truth_plans, response_plans):
#     correct = 0
#     total = sum(len(plans) for plans in ground_truth_plans.values())
#     for software_id, plans in ground_truth_plans.items():
#         if software_id in response_plans:
#             correct += len(set(plans) & set(response_plans[software_id]))
#     return correct / total if total > 0 else 0

# def calculate_precision_recall_f1(ground_truth_plans, response_plans):
#     true_positives = 0
#     false_positives = 0
#     false_negatives = 0
#     for software_id, plans in ground_truth_plans.items():
#         if software_id in response_plans:
#             true_positives += len(set(plans) & set(response_plans[software_id]))
#             false_positives += len(set(response_plans[software_id]) - set(plans))
#         false_negatives += len(set(plans) - set(response_plans[software_id])) if software_id in response_plans else len(plans)
    
#     precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
#     recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
#     f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    
#     return precision, recall, f1




# ground_truth = load_data('RESULTS/data/ground_true_plan_steps_new.json')
# # responses = load_data('RESULTS/groq-responses-mistralEVAL.json')

# # predicts
# # responses_LLAMA = load_data('RESULTS/data/groq-responses-llama2-one-shot.json')
# responses_MISTRAL = load_data('RESULTS/data/groq-responses-mistral-one-shot.json')



# ground_truth_plans = extract_plans_from_ground_truth(ground_truth)
# print(f"this are the unique TRUTH plans:",ground_truth_plans)
# # print(ground_truth_plans)
# response_plans = extract_plans_from_responses(responses_MISTRAL)
# print(f"this are the unique RESPONSE plans:",response_plans)

# print(f"{'ID':<10}{'Response plans':<30}{'Ground Truth plans':<30}")
# for software_id in ground_truth_plans:
#     gt_plans = ', '.join(ground_truth_plans[software_id])
#     resp_plans = ', '.join(response_plans[software_id]) if software_id in response_plans else 'N/A'
#     print(f"{software_id:<10}{resp_plans:<30}{gt_plans:<30}")
    
# accuracy = calculate_accuracy(ground_truth_plans, response_plans)
# print(f'Accuracy: {accuracy:.2%}')
# precision, recall, f1 = calculate_precision_recall_f1(ground_truth_plans, response_plans)
# print(f'Precision: {precision:.2%}')
# print(f'Recall: {recall:.2%}')
# print(f'F1 Score: {f1:.2%}')

# CURRENT RESULTS -------------------------------- LLAMA >>>
# Accuracy: 68.18%
# Precision: 46.15%
# Recall: 83.33%
# F1 Score: 59.41%

# CURRENT RESULTS -------------------------------- MISTRAL >>>
# Accuracy: 54.55%
# Precision: 40.68%
# Recall: 66.67%
# F1 Score: 50.53%




# ALL ONE-SHOT FILES --------------------------------

import glob
import json
import os
import sys
import re

def add_id_to_messages(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        messages = data['messages']
        assistant_count = 1
        for message in messages:
            if message['role'] == 'assistant':
                message['id'] = f"{assistant_count}"  # Assigning a sequential number as value with a comma
                assistant_count += 1
        with open(json_file_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

# Add "id" to each assistant message in the JSON file
# add_id_to_messages('RESULTS/data/groq-responses-mistral.json')

# Add "id" to each assistant message in the JSON file
add_id_to_messages('RESULTS/PLAN/one-shot-prompt/groq-responses-llama2.json')
add_id_to_messages('RESULTS/PLAN/one-shot-prompt/groq-responses-mistral.json')

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_plans_from_ground_truth(ground_truth):
    plans = {}
    for software in ground_truth['study_subjects']['research_software']:
        plans[software['id']] = [plan['type'] for plan in software['plans']]
    return plans

def extract_plans_from_responses(responses):
    plans_by_id = {}
    for message in responses['messages']:
        if message['role'] == 'assistant':
            software_id = message['id']
            content = message['content'].lower()
            start_index = content.find("no_provided") # TODO: trim only corrected answer in JSON response for LLAMA -fixed manually now
            modified_content = content[:start_index]
            # print(modified_content[0:8]) 
            found_plans = re.findall(r'\b(source|binary|container|package manager)\b', modified_content)
            unique_plans = set(method.title() for method in found_plans)
            if software_id not in plans_by_id:
                plans_by_id[software_id] = list(unique_plans)
            else:
                plans_by_id[software_id].extend(unique_plans)
                plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
                print(unique_plans)
    return plans_by_id


# def extract_plans_from_responses(responses):
#     plans_by_id = {}
#     for message in responses['messages']:
#         if message['role'] == 'assistant':
#             software_id = message['id']
#             content = message['content'].lower()
#             start_pattern = 'list:\n{"plans":'
#             end_pattern = '],"no_provided":'
#             start_index = content.find(start_pattern)
#             end_index = content.find(end_pattern, start_index)
#             if start_index != -1 and end_index != -1:
#                 # Adjust the slicing to correctly capture the content up to the end_pattern
#                 modified_content = content[start_index:end_index] + ']}'
#             else:
#                 modified_content = '{}'
#             print(modified_content)  # For debugging
#             found_plans = re.findall(r'\b(source|binary|container|package manager)\b', modified_content)
#             unique_plans = set(method.title() for method in found_plans)
#             if software_id not in plans_by_id:
#                 plans_by_id[software_id] = list(unique_plans)
#             else:
#                 plans_by_id[software_id].extend(unique_plans)
#                 plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
#     return plans_by_id

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




ground_truth = load_data('RESULTS/data/ground_true_plan_steps_new.json')
# responses = load_data('RESULTS/groq-responses-mistralEVAL.json')

import glob

ground_truth_plans = extract_plans_from_ground_truth(ground_truth)

response_files = glob.glob('RESULTS/PLAN/one-shot-prompt/groq-responses-*.json')
# print(response_files)
for response_file in response_files:
    model_name = response_file.split('-')[-1].split('.')[0]
    # print(model_name)
    print(f"\nEvaluating responses for model: {model_name.upper()}")
    response_plans = extract_plans_from_responses(load_data(response_file))
    print(f"this are the unique RESPONSE plans:",response_plans)

    accuracy = calculate_accuracy(ground_truth_plans, response_plans)
    precision, recall, f1 = calculate_precision_recall_f1(ground_truth_plans, response_plans)

    print(f"{'ID':<10}{'Response plans':<30}{'Ground Truth plans':<30}")
    for software_id in ground_truth_plans:
        gt_plans = ', '.join(ground_truth_plans[software_id])
        resp_plans = ', '.join(response_plans[software_id]) if software_id in response_plans else 'N/A'
        print(f"{software_id:<10}{resp_plans:<30}{gt_plans:<30}")

    print(f'Accuracy for {model_name.upper()}: {accuracy:.2%}')
    print(f'Precision for {model_name.upper()}: {precision:.2%}')
    print(f'Recall for {model_name.upper()}: {recall:.2%}')
    print(f'F1 Score for {model_name.upper()}: {f1:.2%}')




### RESULTS ###
# Evaluating responses for model: LLAMA2
# this are the unique RESPONSE plans: {'1': ['Package Manager', 'Binary', 'Container', 'Source'], '2': ['Package Manager', 'Binary', 'Container', 'Source'], '3': ['Package Manager', 'Binary', 'Container', 'Source'], '4': ['Package Manager', 'Binary', 'Container', 'Source'], '5': ['Package Manager', 'Binary', 'Container', 'Source'], '6': ['Package Manager', 'Binary', 'Container', 'Source'], '7': ['Package Manager', 'Binary', 'Container', 'Source'], '8': ['Package Manager', 'Binary', 'Container', 'Source'], '9': ['Package Manager', 'Binary', 'Container', 'Source'], '10': ['Package Manager', 'Binary', 'Container', 'Source'], '11': ['Package Manager', 'Binary', 'Container', 'Source'], '12': ['Package Manager', 'Binary', 'Container', 'Source'], '13': ['Package Manager', 'Binary', 'Container', 'Source'], '14': ['Package Manager', 'Binary', 'Container', 'Source'], '15': ['Package Manager', 'Binary', 'Container', 'Source'], '16': ['Package Manager', 'Binary', 'Container', 'Source'], '17': ['Package Manager', 'Binary', 'Container', 'Source'], '18': ['Package Manager', 'Binary', 'Container', 'Source'], '19': ['Package Manager', 'Binary', 'Container', 'Source'], '20': ['Package Manager', 'Binary', 'Container', 'Source'], '21': ['Package Manager', 'Binary', 'Container', 'Source'], '22': ['Package Manager', 'Binary', 'Container', 'Source'], '23': ['Package Manager', 'Binary', 'Container', 'Source'], '24': ['Package Manager', 'Binary', 'Container', 'Source'], '25': ['Package Manager', 'Binary', 'Container', 'Source'], '26': ['Package Manager', 'Binary', 'Container', 'Source'], '27': ['Package Manager', 'Binary', 'Container', 'Source'], '28': ['Package Manager', 'Binary', 'Container', 'Source'], '29': ['Package Manager', 'Binary', 'Container', 'Source'], '30': ['Package Manager', 'Binary', 'Container', 'Source'], '31': ['Package Manager', 'Binary', 'Container', 'Source'], '32': ['Package Manager', 'Binary', 'Container', 'Source'], '33': ['Package Manager', 'Binary', 'Container', 'Source']}
# ID        Response plans                Ground Truth plans            
# 1         Package Manager, Binary, Container, SourceSource, Source                
# 2         Package Manager, Binary, Container, SourceSource                        
# 3         Package Manager, Binary, Container, SourceSource                        
# 4         Package Manager, Binary, Container, SourceContainer                     
# 5         Package Manager, Binary, Container, SourceSource                        
# 6         Package Manager, Binary, Container, SourceSource                        
# 7         Package Manager, Binary, Container, SourceSource                        
# 8         Package Manager, Binary, Container, SourceSource                        
# 9         Package Manager, Binary, Container, SourceSource                        
# 10        Package Manager, Binary, Container, SourceBinary, Binary, Binary        
# 11        Package Manager, Binary, Container, SourceSource                        
# 12        Package Manager, Binary, Container, SourceSource                        
# 13        Package Manager, Binary, Container, SourceContainer, Source, Source     
# 14        Package Manager, Binary, Container, SourceSource                        
# 15        Package Manager, Binary, Container, SourceSource                        
# 16        Package Manager, Binary, Container, SourceSource                        
# 17        Package Manager, Binary, Container, Sourcepackage manager, package manager, Binary
# 18        Package Manager, Binary, Container, Sourcepackage manager, package manager
# 19        Package Manager, Binary, Container, Sourcepackage manager, Source       
# 20        Package Manager, Binary, Container, SourceSource, Source                
# 21        Package Manager, Binary, Container, SourceSource                        
# 22        Package Manager, Binary, Container, SourceSource                        
# 23        Package Manager, Binary, Container, Sourcepackage manager, package manager
# 24        Package Manager, Binary, Container, SourceSource                        
# 25        Package Manager, Binary, Container, SourceContainer                     
# 26        Package Manager, Binary, Container, SourceSource                        
# 27        Package Manager, Binary, Container, SourceSource                        
# 28        Package Manager, Binary, Container, SourceSource                        
# 29        Package Manager, Binary, Container, SourceSource                        
# 30        Package Manager, Binary, Container, SourceSource                        
# 31        Package Manager, Binary, Container, Sourcepackage manager               
# 32        Package Manager, Binary, Container, SourceSource                        
# 33        Package Manager, Binary, Container, SourceSource                        
# Accuracy for LLAMA2: 70.45%
# Precision for LLAMA2: 23.48%
# Recall for LLAMA2: 86.11%
# F1 Score for LLAMA2: 36.90%

# Evaluating responses for model: MISTRAL
# this are the unique RESPONSE plans: {'1': ['Binary', 'Container'], '2': ['Package Manager', 'Source'], '3': ['Package Manager', 'Source'], '4': ['Container', 'Source'], '5': ['Package Manager', 'Source'], '6': ['Package Manager', 'Source'], '7': ['Package Manager', 'Source'], '8': ['Package Manager', 'Source'], '9': ['Package Manager', 'Source'], '10': ['Binary', 'Source'], '11': ['Package Manager', 'Source'], '12': ['Package Manager', 'Source'], '13': ['Container', 'Source'], '14': ['Package Manager', 'Source'], '15': ['Package Manager', 'Source'], '16': ['Package Manager', 'Source'], '17': ['Package Manager', 'Source'], '18': ['Package Manager', 'Source'], '19': ['Package Manager', 'Source'], '20': ['Package Manager', 'Source'], '21': ['Package Manager', 'Source'], '22': ['Package Manager', 'Source'], '23': ['Package Manager'], '24': ['Package Manager', 'Source'], '25': ['Container'], '26': ['Package Manager', 'Source'], '27': ['Package Manager', 'Source'], '28': ['Package Manager', 'Source'], '29': ['Package Manager', 'Source'], '30': ['Package Manager', 'Source'], '31': ['Package Manager', 'Source'], '32': ['Package Manager', 'Source'], '33': ['Package Manager', 'Source']}
# ID        Response plans                Ground Truth plans            
# 1         Binary, Container             Source, Source                
# 2         Package Manager, Source       Source                        
# 3         Package Manager, Source       Source                        
# 4         Container, Source             Container                     
# 5         Package Manager, Source       Source                        
# 6         Package Manager, Source       Source                        
# 7         Package Manager, Source       Source                        
# 8         Package Manager, Source       Source                        
# 9         Package Manager, Source       Source                        
# 10        Binary, Source                Binary, Binary, Binary        
# 11        Package Manager, Source       Source                        
# 12        Package Manager, Source       Source                        
# 13        Container, Source             Container, Source, Source     
# 14        Package Manager, Source       Source                        
# 15        Package Manager, Source       Source                        
# 16        Package Manager, Source       Source                        
# 17        Package Manager, Source       package manager, package manager, Binary
# 18        Package Manager, Source       package manager, package manager
# 19        Package Manager, Source       package manager, Source       
# 20        Package Manager, Source       Source, Source                
# 21        Package Manager, Source       Source                        
# 22        Package Manager, Source       Source                        
# 23        Package Manager               package manager, package manager
# 24        Package Manager, Source       Source                        
# 25        Container                     Container                     
# 26        Package Manager, Source       Source                        
# 27        Package Manager, Source       Source                        
# 28        Package Manager, Source       Source                        
# 29        Package Manager, Source       Source                        
# 30        Package Manager, Source       Source                        
# 31        Package Manager, Source       package manager               
# 32        Package Manager, Source       Source                        
# 33        Package Manager, Source       Source                        
# Accuracy for MISTRAL: 65.91%
# Precision for MISTRAL: 45.31%
# Recall for MISTRAL: 80.56%
# F1 Score for MISTRAL: 58.00%