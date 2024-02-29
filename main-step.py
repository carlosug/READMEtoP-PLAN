# STEP

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
            temperature=0.1
        )
        return response.choices[0].message.content

    def extract_installation_instructions_from_json(json_file):
        with open(json_file, 'r') as file:
            readmes = json.load(file)

        results = []

        for readme in readmes:
            readme_instructions = readme.get('readme_instructions', '')
            
            # Use the get_completion function to get the installation instructions
            prompt = f""" 
            You will be provided with a Readme. It contains a sequence of instructions per installation method to install a software \
            There are 4 types of methods which are source, packagemanager, container and binary. \
            Perform the following actions. For each Readme:
            1. Extract the installation instructions for each method  \
            2. For each installation method return a list, where each element of the list is an instruction, in sequential order \
            2. The output should be in JSON format. 
            Do not add code commands in the list. Be concise. \

            Readme:
            ```{readme_instructions}``` 
            """
            prompt += """\n# The format must in a strict JSON format, like: {"plan": [{"type": "installation method in the readme" ], "steps": [{"text": "description of the step per installation instruction", "n_steps": ["count of total steps"]}]} """
            
            response = get_completion(prompt)
            
            # Append the extracted instructions to the results list
            results.append([readme['id'],response])

        return results


    json_file_path = './scr/output.json'
    result_list = extract_installation_instructions_from_json(json_file_path)

    # # Print the results
    # for result in result_list:
    #     for key, value in result.items():
    #         print(f"{key}:")
    #         print(value)
    #         print()



    with open("step-responses.json", "w") as json_file:
        json.dump(result_list, json_file, indent=2)

    print("Responses saved to step-responses.json")