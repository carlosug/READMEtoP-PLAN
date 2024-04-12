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

data1 = json.load(open('Evaluation/Rouge/post-groq-responses-MISTRAL.json'))
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
        with open('rouge_scores-mistral.json', 'w') as f:
            json.dump(rouge_scores, f, indent=2)

# ROUGE scores for ID 1:
# No common methods found for ID 1.
# No common methods found for ID 2.
# ROUGE scores for ID 3:
# Method: source
# ROUGE-1: 0.8657
# ROUGE-2: 0.7692
# ROUGE-L: 0.8657

# ROUGE-1: 0.8800
# ROUGE-2: 0.7826
# ROUGE-L: 0.8800

# ROUGE scores for ID 4:
# Method: container
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 5:
# Method: source
# ROUGE-1: 0.9474
# ROUGE-2: 0.9412
# ROUGE-L: 0.9474

# ROUGE-1: 0.8571
# ROUGE-2: 0.8000
# ROUGE-L: 0.8571

# ROUGE-1: 0.6250
# ROUGE-2: 0.5714
# ROUGE-L: 0.6250

# ROUGE-1: 0.9524
# ROUGE-2: 0.9474
# ROUGE-L: 0.9524

# ROUGE-1: 0.4848
# ROUGE-2: 0.4516
# ROUGE-L: 0.4848

# ROUGE-1: 0.9804
# ROUGE-2: 0.9796
# ROUGE-L: 0.9804

# ROUGE-1: 0.7937
# ROUGE-2: 0.7869
# ROUGE-L: 0.7937

# No common methods found for ID 6.
# ROUGE scores for ID 7:
# Method: source
# ROUGE-1: 0.6154
# ROUGE-2: 0.5455
# ROUGE-L: 0.6154

# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 8:
# Method: source
# ROUGE-1: 0.3636
# ROUGE-2: 0.1000
# ROUGE-L: 0.2727

# ROUGE scores for ID 9:
# Method: source
# ROUGE-1: 0.5385
# ROUGE-2: 0.4167
# ROUGE-L: 0.4615

# ROUGE-1: 0.0645
# ROUGE-2: 0.0000
# ROUGE-L: 0.0645

# ROUGE scores for ID 10:
# Method: binary
# ROUGE-1: 0.3600
# ROUGE-2: 0.1250
# ROUGE-L: 0.2400

# ROUGE-1: 0.2069
# ROUGE-2: 0.0741
# ROUGE-L: 0.1379

# No common methods found for ID 11.
# ROUGE scores for ID 12:
# Method: source
# ROUGE-1: 0.1333
# ROUGE-2: 0.0000
# ROUGE-L: 0.1333

# ROUGE-1: 0.1053
# ROUGE-2: 0.0000
# ROUGE-L: 0.1053

# ROUGE scores for ID 13:
# Method: container
# ROUGE-1: 0.3846
# ROUGE-2: 0.3333
# ROUGE-L: 0.3846

# ROUGE-1: 0.2500
# ROUGE-2: 0.0909
# ROUGE-L: 0.2500

# ROUGE-1: 0.1600
# ROUGE-2: 0.0870
# ROUGE-L: 0.1600

# ROUGE-1: 0.6939
# ROUGE-2: 0.6809
# ROUGE-L: 0.6939

# Method: source
# ROUGE-1: 0.2105
# ROUGE-2: 0.0000
# ROUGE-L: 0.2105

# ROUGE-1: 0.4706
# ROUGE-2: 0.4000
# ROUGE-L: 0.4706

# ROUGE-1: 0.3529
# ROUGE-2: 0.1250
# ROUGE-L: 0.3529

# ROUGE-1: 0.8889
# ROUGE-2: 0.8571
# ROUGE-L: 0.8889

# No common methods found for ID 14.
# ROUGE scores for ID 15:
# Method: source
# ROUGE-1: 0.1333
# ROUGE-2: 0.0000
# ROUGE-L: 0.1333

# ROUGE scores for ID 16:
# Method: source
# ROUGE-1: 0.2353
# ROUGE-2: 0.0000
# ROUGE-L: 0.2353

# ROUGE-1: 0.1818
# ROUGE-2: 0.0000
# ROUGE-L: 0.1818

# ROUGE scores for ID 17:
# Method: binary
# ROUGE-1: 0.2041
# ROUGE-2: 0.0000
# ROUGE-L: 0.1633

# ROUGE scores for ID 18:
# Method: package_manager
# ROUGE-1: 0.0714
# ROUGE-2: 0.0000
# ROUGE-L: 0.0714

# ROUGE scores for ID 19:
# Method: source
# ROUGE-1: 0.1250
# ROUGE-2: 0.0000
# ROUGE-L: 0.1250

# ROUGE scores for ID 20:
# Method: package_manager
# ROUGE-1: 0.0000
# ROUGE-2: 0.0000
# ROUGE-L: 0.0000

# ROUGE scores for ID 21:
# Method: source
# ROUGE-1: 0.5000
# ROUGE-2: 0.4516
# ROUGE-L: 0.5000

# ROUGE-1: 1.0000
# ROUGE-2: 1.0000
# ROUGE-L: 1.0000

# ROUGE-1: 0.6122
# ROUGE-2: 0.5532
# ROUGE-L: 0.5714

# ROUGE-1: 0.8696
# ROUGE-2: 0.6818
# ROUGE-L: 0.8261

# ROUGE scores for ID 22:
# Method: source
# ROUGE-1: 0.1053
# ROUGE-2: 0.0000
# ROUGE-L: 0.1053

# ROUGE-1: 0.0667
# ROUGE-2: 0.0000
# ROUGE-L: 0.0667

# ROUGE scores for ID 23:
# Method: package_manager
# ROUGE-1: 0.3333
# ROUGE-2: 0.2000
# ROUGE-L: 0.3333

# ROUGE-1: 0.3478
# ROUGE-2: 0.2857
# ROUGE-L: 0.3478

# ROUGE scores for ID 24:
# Method: source
# ROUGE-1: 0.3810
# ROUGE-2: 0.3158
# ROUGE-L: 0.3810

# ROUGE-1: 0.1111
# ROUGE-2: 0.0000
# ROUGE-L: 0.1111

# ROUGE scores for ID 25:
# Method: container
# ROUGE-1: 0.4800
# ROUGE-2: 0.4348
# ROUGE-L: 0.4800

# No common methods found for ID 26.
# ROUGE scores for ID 27:
# Method: source
# ROUGE-1: 0.6957
# ROUGE-2: 0.6667
# ROUGE-L: 0.6957

# ROUGE-1: 0.8182
# ROUGE-2: 0.8000
# ROUGE-L: 0.8182

# ROUGE-1: 0.5556
# ROUGE-2: 0.5294
# ROUGE-L: 0.5556

# ROUGE-1: 0.3750
# ROUGE-2: 0.2667
# ROUGE-L: 0.3750

# ROUGE scores for ID 28:
# Method: source
# ROUGE-1: 0.9231
# ROUGE-2: 0.9091
# ROUGE-L: 0.9231

# ROUGE scores for ID 29:
# Method: source
# ROUGE-1: 0.9333
# ROUGE-2: 0.9231
# ROUGE-L: 0.9333

# No common methods found for ID 30.
# No common methods found for ID 31.
# ROUGE scores for ID 32:
# Method: source
# ROUGE-1: 0.6939
# ROUGE-2: 0.3830
# ROUGE-L: 0.4898

# ROUGE scores for ID 33:
# Method: source
# ROUGE-1: 0.6667
# ROUGE-2: 0.6250
# ROUGE-L: 0.6667