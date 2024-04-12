import json

# Load the JSON data
with open('RESULTS/data/ground_true_plan_steps_new.json') as f:
    data = json.load(f)

# print(data['study_subjects']["research_software"])

# Extract statistics
study_subjects = data['study_subjects']["research_software"]
total_subjects = 0
for subject in study_subjects:
    total_subjects = int(subject['id'])

print(f'Total subjects: {total_subjects}')

# Extract plan types
plan_types = []
for subject in study_subjects:
    for plan in subject['plans']:
        plan_types.append(plan['type'])

print(f'Plan types: {plan_types}')

# Extract readme instructions
readme_instructions = []
for subject in study_subjects:
    readme_instructions.append(subject['readme_instructions'])

# print(f'Readme instructions: {readme_instructions}')

plan_types_and_steps = {}

for subject in study_subjects:
    plan_types_and_steps[subject['id']] = {}
    for plan in subject['plans']:
        plan_types_and_steps[subject['id']][plan['type']] = len(plan['steps'])

# Print the plan types and number of steps per type
for id, plan_types in plan_types_and_steps.items():
    print(f'For id {id}:')
    print('| Plan Type | Number of Steps |')
    print('|-----------|-----------------|')
    for plan_type, num_steps in plan_types.items():
        print(f'| {plan_type} | {num_steps} |')