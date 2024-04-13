__author__ = 'carlosug'

'''
evaluate LLM MISTRAL on tasks (STEP) with ROUGE:
- PRECISION: the percentage of words or phrases in the LLM response instructions that **match** with the annotated instructions. 
- RECALL: the percentage of words or phrases in the LLM response instructions that **are also present** in the annotated instructions.
- ROUGE-L ignores newlines and computes the LCS for the entire text. ROUGE-Lsum splits the text into sentences based on newlines and computes the LCS for each pair of sentences and take the average score for all sentences.


'''


# credits and code adapted from: https://raw.githubusercontent.com/jd-coderepos/proc-tm/main/rouge_scorer.py

import json
import re
from rouge_score import rouge_scorer
import json

GROQ = "RESULTS/STEP/zero-shot-prompt/groq-responses-mistral.json" # dataset with MISTRAL responses
ANNOTATED = "Evaluation/preprocessing/pre-annotated.json" # ground truth dataset with all atributes



# Preprocessing the GROQ responses
# 1. Add "id" to each "role: assistant" message 
# 2. Extract only the steps and installation instructions from the "role:assistant" message
def extract_steps_per_plan_from_responses(json_file_path_response):
    with open(json_file_path_response, 'r') as file:
        data = json.load(file)
    
    plans_by_id = {}
    plan_pattern = re.compile(r'(Binary|Container|Package Manager|Source):\s*((?:\n\d+\.\s[^\n]+)+)', re.IGNORECASE)
    # adding ids to each role assistant message
    for message in data['messages']:
        if message['role'] == 'assistant':
            software_id = message.get('id')
            content = message['content']
            found_plans = plan_pattern.findall(content) # regrex to parse only the steps per method/plan
            
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

# 3. Generate the JSON file obtained from the preprocessing steps 1,2
# note: This new JSON file is utilized to compare with ANNOTATED variable
json_file_path_response = GROQ
plans_by_id = extract_steps_per_plan_from_responses(json_file_path_response)
with open('Evaluation/Rouge/post-groq-responses-MISTRAL.json', 'w') as outfile:
    json.dump(plans_by_id, outfile, indent=4)


# 4. Preprocess the ANNOTATED JSON file
# extract only plans and types per unique plans
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

# 5. Extract steps from ground truth (ANNOTATED)
json_file_path_ground = ANNOTATED
plans = extract_plans_from_ground_truth(json_file_path_ground)
with open('Evaluation/Rouge/post-annotated.json', 'w') as outfile: # generate the post-annotated file
    json.dump(plans, outfile, indent=4)


# 6. convert plans dict into a list and print them out
# # credits and code adapted from: https://raw.githubusercontent.com/jd-coderepos/proc-tm/main/rouge_scorer.py

def read_files_into_list(filenames):
    """
    Read the contents of the JSON file into a list.
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

# 7. JSON files to evaluate ROUGE:
# Given two files: llm_responses, annotations,
# with the same number (n) of lines,
#  calculate score for each of this lines, or, the average over the whole file.
filenames = ["Evaluation/Rouge/post-annotated.json"]
annotations = read_files_into_list(filenames)

filenames = ["Evaluation/Rouge/post-groq-responses-MISTRAL.json"]
llm_responses = read_files_into_list(filenames)

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'])

cumulative_scores = {
    'rouge1': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rouge2': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeL': {'precision': 0, 'recall': 0, 'fmeasure': 0},
    'rougeLsum': {'precision': 0, 'recall': 0, 'fmeasure': 0}
}

# 8. Calculate ROUGE scores and accumulate
num_samples = len(llm_responses)
for pred, real in zip(llm_responses, annotations):
    scores = scorer.score(real, pred)
    for metric, values in scores.items():
        cumulative_scores[metric]['precision'] += values.precision
        cumulative_scores[metric]['recall'] += values.recall
        cumulative_scores[metric]['fmeasure'] += values.fmeasure

# 9. Average the scores
for metric, values in cumulative_scores.items():
    cumulative_scores[metric]['precision'] /= num_samples
    cumulative_scores[metric]['recall'] /= num_samples
    cumulative_scores[metric]['fmeasure'] /= num_samples

# 10. Write the scores to a JSON file
print(cumulative_scores)
with open('Evaluation/Rouge/scores-mistral.json', 'w') as outfile:
    json.dump(cumulative_scores, outfile, indent=4)



### RESULTS ###
# {'rouge1': {'precision': 0.6109906001446131, 'recall': 0.519041769041769, 'fmeasure': 0.5612753238126867}, 'rouge2': {'precision': 0.36324167872648333, 'recall': 0.30854333128457284, 'fmeasure': 0.33366566965769356}, 'rougeL': {'precision': 0.41142443962400577, 'recall': 0.3495085995085995, 'fmeasure': 0.3779475257389572}, 'rougeLsum': {'precision': 0.6073752711496746, 'recall': 0.515970515970516, 'fmeasure': 0.5579541680504816}}





