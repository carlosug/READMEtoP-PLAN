import json

data = json.load(open('Evaluation/Rouge/post-groq-responses-llama2.json'))
data2 = json.load(open('Evaluation/Rouge/post-annotated.json'))

# Rouge metric
# rouge = Rouge()

# Initialize counters
total_steps = 0
correct_steps = 0
rouge_scores = []


methods = {'Binary', 'Package Manager', 'Container', 'Source'}

for id_, steps in data.items():
    step_counts = {method: 0 for method in methods}
    for method, step_list in steps.items():
        for step in step_list:
            step_counts[method] += 1
    print(f"LLAMA2 ID {id_}: {step_counts}")


methods = {'Binary', 'package manager', 'Container', 'Source'}

for id_, steps in data2.items():
    step_counts = {method: 0 for method in methods}
    for method, step_list in steps.items():
        for step in step_list:
            step_counts[method] += 1
    print(f"ANNOTATED ID {id_}: {step_counts}")

# # Iterate over instructions
# for key, value in data1.items():
#     if key in data2:
#         instructions1 = value['Source']
#         instructions2 = data2[key]['Source']

#         # Count total steps
#         total_steps += len(instructions1)

#         # Check if steps are in correct order
#         if instructions1 == instructions2:
#             correct_steps += len(instructions1)

#         # Calculate Rouge scores
#         scores = rouge.get_scores(' '.join(instructions1), ' '.join(instructions2))
#         rouge_scores.append(scores[0]['rouge-1']['f'])

# # Calculate metrics
# steps_detected = correct_steps / total_steps
# percent_correct_order = (correct_steps / total_steps) * 100
# mean_rouge_score = sum(rouge_scores) / len(rouge_scores)

# # Print results
# print("Steps detected/total steps identified:", steps_detected)
# print("% of steps in correct order:", percent_correct_order)
# print("Mean Rouge score:", mean_rouge_score)

