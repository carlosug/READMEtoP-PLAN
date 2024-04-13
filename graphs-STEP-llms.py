import json
import matplotlib.pyplot as plt
import glob

instructionsAnnotations = json.load(open('Evaluation/Rouge/post-annotated.json'))

# Initialize counters
methods = {'Binary', 'Package Manager', 'Container', 'Source'}

def normalize_method(method):
    if method.lower() == 'package manager':
        return 'Package Manager'
    return method.capitalize()

# Get the list of files matching the pattern
response_files = glob.glob('Evaluation/Rouge/post-groq-responses-*.json')

for response_file in response_files:
    instructionsResponses = json.load(open(response_file))
    ratios_per_id = []

    for id_, steps in instructionsResponses.items():
        system_step_counts = {method: 0 for method in methods}
        for method, step_list in steps.items():
            normalized_method = normalize_method(method)
            for step in step_list:
                system_step_counts[normalized_method] += 1
        
        reference_step_counts = {method: 0 for method in methods}
        if id_ in instructionsAnnotations:
            for method, step_list in instructionsAnnotations[id_].items():
                normalized_method = normalize_method(method)
                for step in step_list:
                    reference_step_counts[normalized_method] += 1
        
        ratios = {}
        for method in methods:
            system_count = system_step_counts[method]
            reference_count = reference_step_counts.get(method, 0)
            if reference_count > 0:
                ratio = system_count / reference_count
            else:
                ratio = 0
            ratios[method] = ratio
        ratios_per_id.append(ratios)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, ratios in enumerate(ratios_per_id):
        id_label = f"ID {i+1}"
        bars = ax.barh(id_label, ratios.values(), label=id_label)

    ax.set_xlabel('Ratio (System Detected / Reference)')
    ax.set_ylabel('ID')
    ax.set_title(f'Ratio of System Detected Steps to Reference Steps ({response_file})')
    ax.axvline(x=1, linestyle='--', color='gray')  # Adding a vertical line at ratio = 1

    # Fit legend to adjust to the size of the plot and set the font size
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')

    plt.show()

