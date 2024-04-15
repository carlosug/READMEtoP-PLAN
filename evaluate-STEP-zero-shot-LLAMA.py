__author__ = 'carlosug'

'''
evaluate LLM LLAMA on tasks (STEP)
'''
# credits and code adapted from: https://raw.githubusercontent.com/jd-coderepos/proc-tm/main/rouge_scorer.py

import json
import re
from rouge_score import rouge_scorer

GROQ = "RESULTS/STEP/zero-shot-prompt/groq-responses-llama2.json" # dataset with LLAMA responses
ANNOTATED = "Evaluation/preprocessing/pre-annotated.json" # ground truth dataset with all atributes


# Preprocessing the GROQ responses
# 1. Add "id" to each "role: assistant" message 
# 2. Extract only the steps and installation instructions from the "role:assistant" message
def extract_steps_per_plan_from_responses(json_file_path_response):
    with open(json_file_path_response, 'r') as file:
        data = json.load(file)
    
    plans_by_id = {}
    plan_pattern = re.compile(r'(Binary|Container|Package Manager|Source):((?:\nStep \d+: [^\n]+)+)', re.IGNORECASE)
# adding ids to each role assistant message
    for message in data['messages']:
        if message['role'] == 'assistant':
            software_id = message.get('id')
            content = message['content']
            found_plans = plan_pattern.findall(content)
            
            steps_per_plan = {}
            for plan, steps in found_plans:
                # Split steps by newline and filter out empty strings
                steps_list = [step.strip() for step in steps.split('\n') if step.strip()]
                steps_per_plan[plan.title()] = steps_list
            
            if software_id not in plans_by_id:
                plans_by_id[software_id] = steps_per_plan
            else:
                # Merge steps if plan already exists (shouldn't happen in well-formed data)
                for plan, steps in steps_per_plan.items():
                    if plan in plans_by_id[software_id]:
                        plans_by_id[software_id][plan].extend(steps)
                        # Remove duplicate steps
                        plans_by_id[software_id][plan] = list(set(plans_by_id[software_id][plan]))
                    else:
                        plans_by_id[software_id][plan] = steps

    return plans_by_id

# 3. Generate the JSON file obtained from the preprocessing steps 1,2
# note: This new JSON file is utilized to compare with ANNOTATED variable
json_file_path_response = GROQ
plans_by_id = extract_steps_per_plan_from_responses(json_file_path_response)
with open('Evaluation/Rouge/post-groq-responses-llama2.json', 'w') as outfile:
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

# 7. JSON files to evaluate ROUGE:
# Given two files: llm_responses, annotations,
# with the same number (n) of lines,
#  calculate score for each of this lines, or, the average over the whole file.
filenames = ["Evaluation/Rouge/post-annotated.json"]
annotations = read_files_into_list(filenames)

filenames = ["Evaluation/Rouge/post-groq-responses-llama2.json"]
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

print(cumulative_scores)

# 10. Write the scores to a JSON file
with open('Evaluation/Rouge/scores-llama2.json', 'w') as outfile:
    json.dump(cumulative_scores, outfile, indent=4)

### RESULTS ###
# ❯ python evaluate-STEP-zero-shot-LLAMA.py  
# {'rouge1': {'precision': 0.41158878504672897, 'recall': 0.6762899262899262, 'fmeasure': 0.5117359981408319}, 'rouge2': {'precision': 0.23485415108451757, 'recall': 0.3859864781807007, 'fmeasure': 0.29202511043943274}, 'rougeL': {'precision': 0.2848598130841121, 'recall': 0.4680589680589681, 'fmeasure': 0.35417150825005805}, 'rougeLsum': {'precision': 0.40822429906542057, 'recall': 0.6707616707616708, 'fmeasure': 0.5075528700906344}}