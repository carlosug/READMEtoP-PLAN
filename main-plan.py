# PLAN

__author__ = 'carlosug'

'''
INSTALLME: teach LLMs to read README INSTALLME
'''

import openai
from openai import OpenAI
import json
import config
api_key = config.API_KEY

client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1",
    api_key=api_key
)
MODEL = "google/gemma-7b-it"


if __name__ == '__main__':

    def get_completion(prompt, model=MODEL):
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=2
        )
        return response.choices[0].message.content

    def extract_installation_instructions_from_json(json_file):
        with open(json_file, 'r') as file:
            readmes = json.load(file)

        results = []

        for readme in readmes:
            readme_instructions = readme.get('readme_instructions', '')
            readme_plans = readme.get('plans', [])

            readme_types = []
            for plan in readme_plans:
                # Extracting the 'type' field from each plan
                readme_type = plan.get('type', '')
                readme_types.append(readme_type)
                
            
            # Use the get_completion function to get the installation instructions
            prompt = f""" 
            Given a  <\"\"\"{readme_instructions}\"\"\", detect the TYPE of PLAN for the installation of a research software. \
            There are 4 TYPE of PLAN: source, packagemanager, container and binary.
            """
            # prompt += """labels: binary, source, packagemanager, container."""
            # prompt += """Classify the following \"\"\"{readme_instructions}\"\"\" in one or multiple installation methods \
            # There are 4 possible installation methods which are: source, packagemanager, container and binary. \
            # A readme can describe a single, or multiple types of installation. \
            # """
            response = get_completion(prompt)
            
            # Append the extracted instructions to the results list
            results.append({"id":readme['id'],"response":response, "answers":readme_types, "prompt":prompt})

        return results


    # Example usage:
    json_file_path = './scr/output.json'
    result_list = extract_installation_instructions_from_json(json_file_path)

    # # Print the results
    # for result in result_list:
    #     for key, value in result.items():
    #         print(f"{key}:")
    #         print(value)
    #         print()



    with open("plan-responses.json", "w") as json_file:
        json.dump(result_list, json_file, indent=2)

    print("LLM responses saved to plan-responses.json")