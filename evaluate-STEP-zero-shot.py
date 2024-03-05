__author__ = 'carlosug'

'''
evaluate LLM on all tasks (STEP)
'''


### ONE FILE ###
import json
import re




# def add_id_to_messages(json_file_path):
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
#         messages = data['messages']
#         assistant_count = 1
#         for message in messages:
#             if message['role'] == 'assistant':
#                 message['id'] = f"{assistant_count}"  # Assigning a sequential number as value with a comma
#                 assistant_count += 1
#         with open(json_file_path, 'w') as outfile:
#             json.dump(data, outfile, indent=4)

# Add "id" to each assistant message in the JSON file
# add_id_to_messages('scr/data/groq-responses-mistral.json')

# Add "id" to each assistant message in the JSON file
# add_id_to_messages('scr/data/groq-responses-llama2.json')
# add_id_to_messages('scr/data/groq-responses-mistral.json')

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_plans_from_ground_truth(ground_truth):
    plans = {}
    for software in ground_truth['study_subjects']['research_software']:
        software_plans = {}
        for plan in software['plans']:
            plan_type = plan['type']
            steps = {step['text'] for step in plan['steps']}
            if plan_type not in software_plans:
                software_plans[plan_type] = steps
            else:
                software_plans[plan_type].update(steps)
        plans[software['id']] = software_plans
    return plans



def extract_steps_per_plan_from_responses(data):
    plans_by_id = {}
    plan_pattern = re.compile(r'(Binary|Container|Package Manager|Source):((?:\nStep \d+: [^\n]+)+)', re.IGNORECASE)

    for message in data['messages']:
        if message['role'] == 'assistant':
            software_id = message.get('id')
            content = message['content']
            found_plans = plan_pattern.findall(content)
            
            steps_per_plan = {}
            for plan, steps in found_plans:
                steps_list = [step.strip() for step in steps.split('\n') if step.strip()]
                steps_per_plan[plan.title()] = set(steps_list)  # Store steps as a set for easier comparison
            
            if software_id not in plans_by_id:
                plans_by_id[software_id] = steps_per_plan
            else:
                for plan, steps in steps_per_plan.items():
                    if plan in plans_by_id[software_id]:
                        plans_by_id[software_id][plan].update(steps)  # Update the set with new steps
                    else:
                        plans_by_id[software_id][plan] = steps

    return plans_by_id

def calculate_accuracy(ground_truth_plans, response_plans):
    correct_steps = 0
    total_steps = 0
    for software_id, plans in ground_truth_plans.items():
        for plan_type, steps in plans.items():
            total_steps += len(steps)
            if software_id in response_plans and plan_type in response_plans[software_id]:
                correct_steps += len(steps & response_plans[software_id][plan_type])
    return correct_steps / total_steps if total_steps > 0 else 0

# def calculate_rouge_score(ground_truth_plans, response_plans):
#     rouge_scores = []
#     for software_id, plans in ground_truth_plans.items():
#         for plan_type, steps in plans.items():
#             if software_id in response_plans and plan_type in response_plans[software_id]:
#                 # Calculate ROUGE score for each plan
#                 rouge_score = calculate_rouge(steps, response_plans[software_id][plan_type])
#                 rouge_scores.append(rouge_score)
#     return rouge_scores

# def calculate_rouge(ground_truth_steps, response_steps):
#     # Implement ROUGE score calculation logic here
#     # This function should return the ROUGE score for a given set of ground truth steps and response steps
#     pass


def calculate_precision_recall_f1(ground_truth_plans, response_plans):
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    for software_id, plans in ground_truth_plans.items():
        for plan_type, steps in plans.items():
            if software_id in response_plans and plan_type in response_plans[software_id]:
                true_positives += len(steps & response_plans[software_id][plan_type])
                false_positives += len(response_plans[software_id][plan_type] - steps)
                false_negatives += len(steps - response_plans[software_id][plan_type])
            else:
                false_negatives += len(steps)
    
    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    
    return precision, recall, f1

ground_truth = load_data('scr/data/ground_true_plan_steps_new.json')
responses = load_data('scr/data/groq-responses-llama2TEST.json')
# print(responses)

ground_truth_plans = extract_plans_from_ground_truth(ground_truth)
print(ground_truth_plans.items())
# print(ground_truth_plans)
response_plans = extract_steps_per_plan_from_responses(responses)
print(response_plans.items())


accuracy = calculate_accuracy(ground_truth_plans, response_plans)
precision, recall, f1 = calculate_precision_recall_f1(ground_truth_plans, response_plans)
# rouge = calculate_rouge_score(ground_truth_plans, response_plans)

print(f'Accuracy: {accuracy:.2%}')
print(f'Precision: {precision:.2%}')
print(f'Recall: {recall:.2%}')
print(f'F1 Score: {f1:.2%}')
# print(f'Rouge: {rouge:.2%}')



### OTHER APPROACH

# ### ONE FILE ###
# import json
# import re
# from rouge_score import rouge_scorer




# # def add_id_to_messages(json_file_path):
# #     with open(json_file_path, 'r') as file:
# #         data = json.load(file)
# #         messages = data['messages']
# #         assistant_count = 1
# #         for message in messages:
# #             if message['role'] == 'assistant':
# #                 message['id'] = f"{assistant_count}"  # Assigning a sequential number as value with a comma
# #                 assistant_count += 1
# #         with open(json_file_path, 'w') as outfile:
# #             json.dump(data, outfile, indent=4)

# # Add "id" to each assistant message in the JSON file
# # add_id_to_messages('scr/data/groq-responses-mistral.json')

# # Add "id" to each assistant message in the JSON file
# # add_id_to_messages('scr/data/groq-responses-llama2.json')
# # add_id_to_messages('scr/data/groq-responses-mistral.json')

# def read_json_lines(file_path):
#     with open(file_path, 'r') as file:
#         return [json.loads(line) for line in file]

# def extract_plans_from_ground_truth(ground_truth_lines):
#     plans = {}
#     for line in ground_truth_lines:
#         for software in line['study_subjects']['research_software']:
#             software_plans = {}
#             for plan in software['plans']:
#                 plan_type = plan['type']
#                 steps = {step['text'] for step in plan['steps']}
#                 if plan_type not in software_plans:
#                     software_plans[plan_type] = steps
#                 else:
#                     software_plans[plan_type].update(steps)
#             plans[software['id']] = software_plans
#     return plans

# def extract_steps_per_plan_from_responses(response_lines):
#     plans_by_id = {}
#     plan_pattern = re.compile(r'(Binary|Container|Package Manager|Source):((?:\nStep \d+: [^\n]+)+)', re.IGNORECASE)

#     for line in response_lines:
#         for message in line['messages']:
#             if message['role'] == 'assistant':
#                 software_id = message.get('id')
#                 content = message['content']
#                 found_plans = plan_pattern.findall(content)
                
#                 steps_per_plan = {}
#                 for plan, steps in found_plans:
#                     steps_list = [step.strip() for step in steps.split('\n') if step.strip()]
#                     steps_per_plan[plan.title()] = set(steps_list)  # Store steps as a set for easier comparison
                
#                 if software_id not in plans_by_id:
#                     plans_by_id[software_id] = steps_per_plan
#                 else:
#                     for plan, steps in steps_per_plan.items():
#                         if plan in plans_by_id[software_id]:
#                             plans_by_id[software_id][plan].update(steps)  # Update the set with new steps
#                         else:
#                             plans_by_id[software_id][plan] = steps

#     return plans_by_id



# reference_filenames = ["scr/data/ground_true_plan_steps_new.json"]
# prediction_filenames = ["scr/data/groq-responses-llama2TEST.json"]

# ground_truth_lines = read_json_lines(reference_filenames[0])
# response_lines = read_json_lines(prediction_filenames[0])

# ground_truth_plans = extract_plans_from_ground_truth(ground_truth_lines)
# # print(ground_truth_lines)
# response_plans = extract_steps_per_plan_from_responses(response_lines)
# print(response_lines)
# scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)

# cumulative_scores = {
#     'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
#     'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
# }

# # Assuming predictions and references are lists of strings for simplicity
# predictions = [str(plan) for plan in response_plans.values()]
# references = [str(plan) for plan in ground_truth_plans.values()]
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



# # ALL ONE-SHOT FILES --------------------------------

# import glob
# import json
# import os
# import sys
# import re

# def add_id_to_messages(json_file_path):
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
#         messages = data['messages']
#         assistant_count = 1
#         for message in messages:
#             if message['role'] == 'assistant':
#                 message['id'] = f"{assistant_count}"  # Assigning a sequential number as value with a comma
#                 assistant_count += 1
#         with open(json_file_path, 'w') as outfile:
#             json.dump(data, outfile, indent=4)

# # Add "id" to each assistant message in the JSON file
# # add_id_to_messages('scr/data/groq-responses-mistral.json')

# # Add "id" to each assistant message in the JSON file
# add_id_to_messages('scr/data/groq-responses-llama2.json')
# add_id_to_messages('scr/data/groq-responses-mistral.json')

# def load_data(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# def extract_plans_from_ground_truth(ground_truth):
#     plans = {}
#     for software in ground_truth['study_subjects']['research_software']:
#         plans[software['id']] = [plan['type'] for plan in software['plans']]
#     return plans

# def extract_plans_from_responses(responses):
#     plans_by_id = {}
#     for message in responses['messages']:
#         if message['role'] == 'assistant':
#             software_id = message['id']
#             content = message['content'].lower()
#             start_index = content.find("\n  \"no_provided\":")
#             modified_content = content[:start_index]
#             # print(modified_content[0:8]) 
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
# #             start_pattern = 'list:\n{"plans":'
# #             end_pattern = '],"no_provided":'
# #             start_index = content.find(start_pattern)
# #             end_index = content.find(end_pattern, start_index)
# #             if start_index != -1 and end_index != -1:
# #                 # Adjust the slicing to correctly capture the content up to the end_pattern
# #                 modified_content = content[start_index:end_index] + ']}'
# #             else:
# #                 modified_content = '{}'
# #             print(modified_content)  # For debugging
# #             found_plans = re.findall(r'\b(source|binary|container|package manager)\b', modified_content)
# #             unique_plans = set(method.title() for method in found_plans)
# #             if software_id not in plans_by_id:
# #                 plans_by_id[software_id] = list(unique_plans)
# #             else:
# #                 plans_by_id[software_id].extend(unique_plans)
# #                 plans_by_id[software_id] = list(set(plans_by_id[software_id]))  # Remove duplicates
# #     return plans_by_id

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




# ground_truth = load_data('scr/data/ground_true_plan_steps_new.json')
# # responses = load_data('scr/groq-responses-mistralEVAL.json')

# import glob

# ground_truth_plans = extract_plans_from_ground_truth(ground_truth)

# response_files = glob.glob('scr/data/groq-responses-*.json')
# # print(response_files)
# for response_file in response_files:
#     model_name = response_file.split('-')[-1].split('.')[0]
#     # print(model_name)
#     print(f"\nEvaluating responses for model: {model_name.upper()}")
#     response_plans = extract_plans_from_responses(load_data(response_file))
#     print(f"this are the unique RESPONSE plans:",response_plans)

#     accuracy = calculate_accuracy(ground_truth_plans, response_plans)
#     precision, recall, f1 = calculate_precision_recall_f1(ground_truth_plans, response_plans)

#     print(f"{'ID':<10}{'Response plans':<30}{'Ground Truth plans':<30}")
#     for software_id in ground_truth_plans:
#         gt_plans = ', '.join(ground_truth_plans[software_id])
#         resp_plans = ', '.join(response_plans[software_id]) if software_id in response_plans else 'N/A'
#         print(f"{software_id:<10}{resp_plans:<30}{gt_plans:<30}")

#     print(f'Accuracy for {model_name.upper()}: {accuracy:.2%}')
#     print(f'Precision for {model_name.upper()}: {precision:.2%}')
#     print(f'Recall for {model_name.upper()}: {recall:.2%}')
#     print(f'F1 Score for {model_name.upper()}: {f1:.2%}')



