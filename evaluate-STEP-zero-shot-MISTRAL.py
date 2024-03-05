import json
import re
from rouge_score import rouge_scorer

DATA = "RESULTS/STEP/zero-shot-prompt/groq-responses-mistral.json"
REF= "RESULTS/data/ground_true_plan_steps_new.json"

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
add_id_to_messages(DATA)



def extract_steps_per_plan_from_responses(json_file_path_response):
    with open(json_file_path_response, 'r') as file:
        data = json.load(file)
    
    plans_by_id = {}
    plan_pattern = re.compile(r'(Binary|Container|Package Manager|Source):\s*((?:\n\d+\.\s[^\n]+)+)', re.IGNORECASE)

    for message in data['messages']:
        if message['role'] == 'assistant':
            software_id = message.get('id')
            content = message['content']
            found_plans = plan_pattern.findall(content)
            
            steps_per_plan = {}
            for plan, steps in found_plans:
                steps_list = [step.strip() for step in steps.split('\n') if step.strip()]
                steps_per_plan[plan.title()] = steps_list
            
            if software_id not in plans_by_id:
                plans_by_id[software_id] = steps_per_plan
            else:
                for plan, steps in steps_per_plan.items():
                    if plan in plans_by_id[software_id]:
                        plans_by_id[software_id][plan].extend(steps)
                        plans_by_id[software_id][plan] = list(set(plans_by_id[software_id][plan]))
                    else:
                        plans_by_id[software_id][plan] = steps

    return plans_by_id

# Example usage
json_file_path_response = DATA
plans_by_id = extract_steps_per_plan_from_responses(json_file_path_response)
with open('groq-responses-MISTRAL-log.json', 'w') as outfile:
    json.dump(plans_by_id, outfile, indent=4)



def extract_plans_from_ground_truth(json_file_path_ground):
    with open(json_file_path_ground, 'r') as file:
        data = json.load(file)
    plans = {}
    for software in data['study_subjects']['research_software']:
        software_plans = {}
        for plan in software['plans']:
            plan_type = plan['type']
            steps = [step['text'] for step in plan['steps']]  # Change set to list for JSON serialization
            if plan_type not in software_plans:
                software_plans[plan_type] = steps
            else:
                software_plans[plan_type].extend(steps)  # Use extend instead of update
        plans[software['id']] = software_plans
    return plans

# Example usage
json_file_path_ground = REF
plans = extract_plans_from_ground_truth(json_file_path_ground)
with open('ref-log.json', 'w') as outfile:
    json.dump(plans, outfile, indent=4)

# # convert plans dict into a list and print them out

def read_files_into_list(filenames):
    """
    Read the contents of multiple files into a list.

    Parameters:
    - filenames (list): List of file paths to be read.

    Returns:
    - List of strings where each string is the content of a file.
    """
    contents = []
    for filename in filenames:
        with open(filename, 'r') as file:
            contents.append(file.read())
    return contents

# Example usage:
filenames = ["ref-log.json"]
refs = read_files_into_list(filenames)

filenames = ["groq-responses-MISTRAL-log.json"]
preds = read_files_into_list(filenames)

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

cumulative_scores = {
    'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
}

# Calculate ROUGE scores and accumulate
num_samples = len(preds)
for pred, ref in zip(preds, refs):
    scores = scorer.score(ref, pred)
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



### RESULTS ###
# {'rouge1': {'precision': 0.6109906001446131, 'recall': 0.519041769041769, 'fmeasure': 0.5612753238126867}, 'rouge2': {'precision': 0.36324167872648333, 'recall': 0.30854333128457284, 'fmeasure': 0.33366566965769356}, 'rougeL': {'precision': 0.41142443962400577, 'recall': 0.3495085995085995, 'fmeasure': 0.3779475257389572}, 'rougeLsum': {'precision': 0.6073752711496746, 'recall': 0.515970515970516, 'fmeasure': 0.5579541680504816}}





