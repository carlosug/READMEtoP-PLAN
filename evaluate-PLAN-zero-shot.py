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
add_id_to_messages('RESULTS/PLAN/zero-shot-prompt/short-prompt/groq-responses-llama2.json')
add_id_to_messages('RESULTS/PLAN/zero-shot-prompt/short-prompt/groq-responses-mistral.json')

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
            start_index = content.find("\n  \"no_provided\":")
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

response_files = glob.glob('RESULTS/PLAN/zero-shot-prompt/short-prompt/groq-responses-*.json')
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



#### RESULTS #####
# Evaluating responses for model: LLAMA2
# this are the unique RESPONSE plans: {'1': ['Source', 'Binary', 'Container', 'Package Manager'], '2': ['Binary', 'Source', 'Package Manager', 'Container'], '3': ['Source', 'Binary', 'Package Manager', 'Container'], '4': ['Source', 'Binary', 'Package Manager', 'Container'], '5': ['Binary', 'Source', 'Package Manager', 'Container'], '6': ['Binary', 'Source', 'Package Manager', 'Container'], '7': ['Binary', 'Source', 'Package Manager', 'Container'], '8': ['Binary', 'Source', 'Package Manager', 'Container'], '9': ['Binary', 'Source', 'Package Manager', 'Container'], '10': ['Source', 'Binary', 'Package Manager', 'Container'], '11': ['Binary', 'Source', 'Package Manager', 'Container'], '12': ['Binary', 'Source', 'Package Manager', 'Container'], '13': ['Binary', 'Source', 'Package Manager', 'Container'], '14': ['Binary', 'Source', 'Package Manager', 'Container'], '15': ['Binary', 'Source', 'Package Manager', 'Container'], '16': ['Binary', 'Source', 'Package Manager', 'Container'], '17': ['Binary', 'Source', 'Package Manager', 'Container'], '18': ['Binary', 'Source', 'Package Manager', 'Container'], '19': ['Binary', 'Source', 'Package Manager', 'Container'], '20': ['Binary', 'Source', 'Package Manager', 'Container'], '21': ['Binary', 'Source', 'Package Manager', 'Container'], '22': ['Binary', 'Source', 'Package Manager', 'Container'], '23': ['Binary', 'Source', 'Package Manager', 'Container'], '24': ['Binary', 'Source', 'Container', 'Package Manager'], '25': ['Binary', 'Source', 'Package Manager', 'Container'], '26': ['Binary', 'Source', 'Container', 'Package Manager'], '27': ['Binary', 'Source', 'Package Manager', 'Container'], '28': ['Binary', 'Source', 'Container', 'Package Manager'], '29': ['Binary', 'Source', 'Package Manager', 'Container'], '30': ['Binary', 'Source', 'Package Manager', 'Container'], '31': ['Binary', 'Source', 'Package Manager', 'Container'], '32': ['Binary', 'Source', 'Package Manager', 'Container'], '33': ['Binary', 'Source', 'Package Manager', 'Container']}
# ID        Response plans                Ground Truth plans            
# 1         Source, Binary, Container, Package ManagerSource, Source                
# 2         Binary, Source, Package Manager, ContainerSource                        
# 3         Source, Binary, Package Manager, ContainerSource                        
# 4         Source, Binary, Package Manager, ContainerContainer                     
# 5         Binary, Source, Package Manager, ContainerSource                        
# 6         Binary, Source, Package Manager, ContainerSource                        
# 7         Binary, Source, Package Manager, ContainerSource                        
# 8         Binary, Source, Package Manager, ContainerSource                        
# 9         Binary, Source, Package Manager, ContainerSource                        
# 10        Source, Binary, Package Manager, ContainerBinary, Binary, Binary        
# 11        Binary, Source, Package Manager, ContainerSource                        
# 12        Binary, Source, Package Manager, ContainerSource                        
# 13        Binary, Source, Package Manager, ContainerContainer, Source, Source     
# 14        Binary, Source, Package Manager, ContainerSource                        
# 15        Binary, Source, Package Manager, ContainerSource                        
# 16        Binary, Source, Package Manager, ContainerSource                        
# 17        Binary, Source, Package Manager, Containerpackage manager, package manager, Binary
# 18        Binary, Source, Package Manager, Containerpackage manager, package manager
# 19        Binary, Source, Package Manager, Containerpackage manager, Source       
# 20        Binary, Source, Package Manager, ContainerSource, Source                
# 21        Binary, Source, Package Manager, ContainerSource                        
# 22        Binary, Source, Package Manager, ContainerSource                        
# 23        Binary, Source, Package Manager, Containerpackage manager, package manager
# 24        Binary, Source, Container, Package ManagerSource                        
# 25        Binary, Source, Package Manager, ContainerContainer                     
# 26        Binary, Source, Container, Package ManagerSource                        
# 27        Binary, Source, Package Manager, ContainerSource                        
# 28        Binary, Source, Container, Package ManagerSource                        
# 29        Binary, Source, Package Manager, ContainerSource                        
# 30        Binary, Source, Package Manager, ContainerSource                        
# 31        Binary, Source, Package Manager, Containerpackage manager               
# 32        Binary, Source, Package Manager, ContainerSource                        
# 33        Binary, Source, Package Manager, ContainerSource                        
# Accuracy for LLAMA2: 70.45%
# Precision for LLAMA2: 23.48%
# Recall for LLAMA2: 86.11%
# F1 Score for LLAMA2: 36.90%

# Evaluating responses for model: MISTRAL
# this are the unique RESPONSE plans: {'1': ['Source', 'Binary'], '2': [], '3': ['Source', 'Binary'], '4': ['Source', 'Container'], '5': ['Binary', 'Source', 'Package Manager'], '6': ['Package Manager'], '7': ['Source', 'Package Manager'], '8': ['Package Manager'], '9': ['Binary', 'Source', 'Package Manager'], '10': ['Source', 'Binary'], '11': ['Source', 'Package Manager'], '12': ['Source', 'Package Manager'], '13': ['Source', 'Container'], '14': ['Package Manager', 'Container'], '15': ['Source', 'Package Manager'], '16': ['Source', 'Package Manager'], '17': ['Source', 'Package Manager', 'Container'], '18': ['Source', 'Package Manager', 'Container'], '19': ['Source', 'Package Manager'], '20': ['Package Manager'], '21': ['Source'], '22': ['Source', 'Package Manager'], '23': ['Package Manager'], '24': ['Source', 'Package Manager'], '25': ['Container'], '26': ['Source', 'Package Manager'], '27': [], '28': ['Source'], '29': ['Source', 'Package Manager'], '30': ['Source', 'Package Manager'], '31': ['Source', 'Package Manager'], '32': ['Binary', 'Source', 'Package Manager'], '33': ['Source']}
# ID        Response plans                Ground Truth plans            
# 1         Source, Binary                Source, Source                
# 2                                       Source                        
# 3         Source, Binary                Source                        
# 4         Source, Container             Container                     
# 5         Binary, Source, Package ManagerSource                        
# 6         Package Manager               Source                        
# 7         Source, Package Manager       Source                        
# 8         Package Manager               Source                        
# 9         Binary, Source, Package ManagerSource                        
# 10        Source, Binary                Binary, Binary, Binary        
# 11        Source, Package Manager       Source                        
# 12        Source, Package Manager       Source                        
# 13        Source, Container             Container, Source, Source     
# 14        Package Manager, Container    Source                        
# 15        Source, Package Manager       Source                        
# 16        Source, Package Manager       Source                        
# 17        Source, Package Manager, Containerpackage manager, package manager, Binary
# 18        Source, Package Manager, Containerpackage manager, package manager
# 19        Source, Package Manager       package manager, Source       
# 20        Package Manager               Source, Source                
# 21        Source                        Source                        
# 22        Source, Package Manager       Source                        
# 23        Package Manager               package manager, package manager
# 24        Source, Package Manager       Source                        
# 25        Container                     Container                     
# 26        Source, Package Manager       Source                        
# 27                                      Source                        
# 28        Source                        Source                        
# 29        Source, Package Manager       Source                        
# 30        Source, Package Manager       Source                        
# 31        Source, Package Manager       package manager               
# 32        Binary, Source, Package ManagerSource                        
# 33        Source                        Source                        
# Accuracy for MISTRAL: 54.55%
# Precision for MISTRAL: 40.68%
# Recall for MISTRAL: 66.67%
# F1 Score for MISTRAL: 50.53%



