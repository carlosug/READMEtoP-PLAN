__author__ = 'carlosug'

'''
GOAL: evaluate LLM on all tasks (work in progress). Steps:
# first match methods between the responses and annotation for each ID.
# Then, for each matched method, we compare the instructions and calculate the ROUGE scores if instructions are present for both datasets. 
# If no common methods are found for an ID, it prints a message indicating "no common methods found". 
# This approach ensures that we only compare instructions for methods that exist in both datasets

'''





import json
from rouge_score import rouge_scorer

def normalize_method_name(method):
    return method.lower().replace(' ', '_')

def get_instructions_per_method(data, id_number):
    instructions = {}
    if id_number in data:
        for method, steps in data[id_number].items():
            instructions[normalize_method_name(method)] = steps
    return instructions

def calculate_rouge_scores(instructions1, instructions2):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = {}
    for method in instructions1:
        if method in instructions2:
            method_scores = []
            for instruction1, instruction2 in zip(instructions1[method], instructions2[method]):
                if instruction1 and instruction2:
                    rouge_scores = scorer.score(instruction1, instruction2)
                    method_scores.append(rouge_scores)
            scores[method] = method_scores
    return scores

def print_rouge_scores(scores, id_number):
    print(f"ROUGE scores for ID {id_number}:")
    for method, method_scores in scores.items():
        print(f"Method: {method}")
        for score in method_scores:
            print(f"ROUGE-1: {score['rouge1'].fmeasure:.4f}")
            print(f"ROUGE-2: {score['rouge2'].fmeasure:.4f}")
            print(f"ROUGE-L: {score['rougeL'].fmeasure:.4f}")
            print()

data1 = json.load(open('Evaluation/Rouge/post-groq-responses-llama2.json'))
data2 = json.load(open('Evaluation/Rouge/post-annotated.json'))

for id_number in data1:
    instructions1 = get_instructions_per_method(data1, id_number)
    instructions2 = get_instructions_per_method(data2, id_number)
    scores = calculate_rouge_scores(instructions1, instructions2)
    if scores:
        print_rouge_scores(scores, id_number)
    else:
        print(f"No common methods found for ID {id_number}.")
        # Create a dictionary to store the rouge scores
        rouge_scores = {}

        # Iterate over the data1 dictionary
        for id_number in data1:
            instructions1 = get_instructions_per_method(data1, id_number)
            instructions2 = get_instructions_per_method(data2, id_number)
            scores = calculate_rouge_scores(instructions1, instructions2)
            if scores:
                rouge_scores[id_number] = scores

        # Write the rouge_scores dictionary to a JSON file
        with open('rouge_scores-llama2.json', 'w') as f:
            json.dump(rouge_scores, f, indent=4)

# ROUGE scores for ID 1:
# Method: source
# ROUGE-1: 0.1250
# ROUGE-2: 0.0000
# ROUGE-L: 0.1250

# ROUGE-1: 0.2500
# ROUGE-2: 0.0000
# ROUGE-L: 0.2500

# ROUGE-1: 0.1212
# ROUGE-2: 0.0000
# ROUGE-L: 0.0606

# ROUGE scores for ID 2:
# Method: source
# ROUGE-1: 0.1250
# ROUGE-2: 0.0000
# ROUGE-L: 0.1250

# ROUGE scores for ID 3:
# Method: source
# ROUGE-1: 0.1429
# ROUGE-2: 0.0500
# ROUGE-L: 0.1429

# ROUGE-1: 0.2500
# ROUGE-2: 0.0909
# ROUGE-L: 0.2500

# ROUGE scores for ID 4:
# Method: container
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.2778
# ROUGE-2: 0.0588
# ROUGE-L: 0.2222

# ROUGE scores for ID 5:
# Method: source
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.2353
# ROUGE-2: 0.1333
# ROUGE-L: 0.2353

# ROUGE-1: 0.2222
# ROUGE-2: 0.0588
# ROUGE-L: 0.2222

# ROUGE-1: 0.0571
# ROUGE-2: 0.0000
# ROUGE-L: 0.0571

# ROUGE-1: 0.8627
# ROUGE-2: 0.7755
# ROUGE-L: 0.8627

# ROUGE scores for ID 6:
# Method: source
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 7:
# Method: source
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.0976
# ROUGE-2: 0.0000
# ROUGE-L: 0.0488

# ROUGE scores for ID 8:
# Method: source
# ROUGE-1: 0.1111
# ROUGE-2: 0.0000
# ROUGE-L: 0.1111

# ROUGE scores for ID 9:
# Method: source
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE-1: 0.1778
# ROUGE-2: 0.0465
# ROUGE-L: 0.1778

# ROUGE-1: 0.0455
# ROUGE-2: 0.0000
# ROUGE-L: 0.0455

# ROUGE-1: 0.0800
# ROUGE-2: 0.0000
# ROUGE-L: 0.0800

# ROUGE scores for ID 10:
# Method: binary
# ROUGE-1: 0.2564
# ROUGE-2: 0.2162
# ROUGE-L: 0.2564

# ROUGE-1: 0.3125
# ROUGE-2: 0.0000
# ROUGE-L: 0.2500

# ROUGE scores for ID 11:
# Method: source
# ROUGE-1: 0.1538
# ROUGE-2: 0.0000
# ROUGE-L: 0.1538

# ROUGE-1: 0.7273
# ROUGE-2: 0.7143
# ROUGE-L: 0.7273

# ROUGE-1: 0.5882
# ROUGE-2: 0.5625
# ROUGE-L: 0.5882

# ROUGE-1: 0.6923
# ROUGE-2: 0.6667
# ROUGE-L: 0.6923

# ROUGE scores for ID 12:
# Method: source
# ROUGE-1: 0.1667
# ROUGE-2: 0.0000
# ROUGE-L: 0.1667

# ROUGE-1: 0.8182
# ROUGE-2: 0.7000
# ROUGE-L: 0.8182

# ROUGE scores for ID 13:
# Method: container
# ROUGE-1: 0.3704
# ROUGE-2: 0.3200
# ROUGE-L: 0.3704

# ROUGE-1: 0.2353
# ROUGE-2: 0.0625
# ROUGE-L: 0.1765

# ROUGE-1: 0.2308
# ROUGE-2: 0.0833
# ROUGE-L: 0.1538

# ROUGE-1: 0.6909
# ROUGE-2: 0.6415
# ROUGE-L: 0.6909

# Method: source
# ROUGE-1: 0.2353
# ROUGE-2: 0.0000
# ROUGE-L: 0.2353

# ROUGE-1: 0.4444
# ROUGE-2: 0.3750
# ROUGE-L: 0.4444

# ROUGE-1: 0.3889
# ROUGE-2: 0.2353
# ROUGE-L: 0.3889

# ROUGE-1: 0.6667
# ROUGE-2: 0.6000
# ROUGE-L: 0.6667

# ROUGE-1: 0.0833
# ROUGE-2: 0.0000
# ROUGE-L: 0.0833

# ROUGE-1: 0.1538
# ROUGE-2: 0.0000
# ROUGE-L: 0.1538

# ROUGE-1: 0.2500
# ROUGE-2: 0.0000
# ROUGE-L: 0.1250

# ROUGE-1: 0.2353
# ROUGE-2: 0.0408
# ROUGE-L: 0.1176

# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 14:
# Method: source
# ROUGE-1: 0.1111
# ROUGE-2: 0.0000
# ROUGE-L: 0.1111

# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 15:
# Method: source
# ROUGE-1: 0.2353
# ROUGE-2: 0.1333
# ROUGE-L: 0.2353

# ROUGE scores for ID 16:
# Method: source
# ROUGE-1: 0.2105
# ROUGE-2: 0.0000
# ROUGE-L: 0.2105

# ROUGE-1: 0.1818
# ROUGE-2: 0.0000
# ROUGE-L: 0.1818

# ROUGE scores for ID 17:
# Method: package_manager
# ROUGE-1: 0.2000
# ROUGE-2: 0.0000
# ROUGE-L: 0.2000

# ROUGE scores for ID 18:
# Method: package_manager
# ROUGE-1: 0.9189
# ROUGE-2: 0.9143
# ROUGE-L: 0.9189

# ROUGE-1: 0.5143
# ROUGE-2: 0.4848
# ROUGE-L: 0.5143

# ROUGE-1: 0.3571
# ROUGE-2: 0.1538
# ROUGE-L: 0.2857

# ROUGE scores for ID 19:
# Method: package_manager
# ROUGE-1: 0.5000
# ROUGE-2: 0.3077
# ROUGE-L: 0.4286

# ROUGE-1: 0.4706
# ROUGE-2: 0.2500
# ROUGE-L: 0.4118

# ROUGE-1: 0.5714
# ROUGE-2: 0.5263
# ROUGE-L: 0.5714

# Method: source
# ROUGE-1: 0.2143
# ROUGE-2: 0.0000
# ROUGE-L: 0.2143

# No common methods found for ID 20.
# ROUGE scores for ID 21:
# Method: source
# ROUGE-1: 0.7595
# ROUGE-2: 0.7273
# ROUGE-L: 0.7595

# ROUGE-1: 0.9524
# ROUGE-2: 0.9474
# ROUGE-L: 0.9524

# ROUGE-1: 0.6000
# ROUGE-2: 0.5417
# ROUGE-L: 0.5600

# ROUGE-1: 0.6038
# ROUGE-2: 0.4706
# ROUGE-L: 0.5283

# No common methods found for ID 22.
# ROUGE scores for ID 23:
# Method: package_manager
# ROUGE-1: 0.2667
# ROUGE-2: 0.1538
# ROUGE-L: 0.2667

# ROUGE-1: 0.4286
# ROUGE-2: 0.3846
# ROUGE-L: 0.4286

# No common methods found for ID 24.
# ROUGE scores for ID 25:
# Method: container
# ROUGE-1: 0.2667
# ROUGE-2: 0.0000
# ROUGE-L: 0.2667

# No common methods found for ID 26.
# No common methods found for ID 27.
# No common methods found for ID 28.
# No common methods found for ID 29.
# No common methods found for ID 30.
# ROUGE scores for ID 31:
# Method: package_manager
# ROUGE-1: 0.5161
# ROUGE-2: 0.4138
# ROUGE-L: 0.3226

# ROUGE-1: 0.1935
# ROUGE-2: 0.0000
# ROUGE-L: 0.1290

# No common methods found for ID 32.
# No common methods found for ID 33.