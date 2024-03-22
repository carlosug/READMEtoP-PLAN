
# PLAN
import os
import json
import notebooks.configGroq as configGroq

from groq import Groq
api_key2 = configGroq.API_KEY
api_key2
client = Groq(
    api_key=api_key2,
)
# MODEL = "google/gemma-7b-it"

MODELLAMA="llama2-70b-4096"
MODELMISTRAL="mixtral-8x7b-32768"
# client = openai.OpenAI()
def get_completion(prompt, model=MODELLAMA):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
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
        Given a  <\"\"\"{readme_instructions}\"\"\",your task is to identify and list the unique installation methods. \
         These methods are plans containing instructions for installing research software, to be executed in a specific order and under defined conditions. \
            There are four installation methods:
            \n\n   Binary: Download and run precompiled files. For example, GitHub releases. \
            \n    Container: Use isolated environments. For example,, Docker, Podman, or Singularity. \
            \n    Package Manager: Install via tools and indexed repositories. For example, Conda, Homebrew, or Pip \
            \n    Source: Install using command-line, following instructions. For example, clone from repository or download files.
            \n\nIf no method is mentioned, write \"No method provided.\" Exclude code commands. Be concise.\
        """
        # prompt += """labels: binary, source, packagemanager, container."""
        # prompt += """Classify the following \"\"\"{readme_instructions}\"\"\" in one or multiple installation methods \
        # There are 4 possible installation methods which are: source, packagemanager, container and binary. \
        # A readme can describe a single, or multiple types of installation. \
        # """
        import time

        def rate_limited_get_completion(prompt):
            """
            This function wraps the get_completion call to handle rate limiting by Groq API.
            Groq has a rate limit of 20 requests per minute and 25 requests per 10 minutes.
            """
            MINUTE_LIMIT = 1  # Adjusted to allow a maximum of 1 requests per minute
            global request_timestamps
            if 'request_timestamps' not in globals():
                request_timestamps = []
            current_time = time.time()
            request_timestamps = [timestamp for timestamp in request_timestamps if current_time - timestamp < 60]  # Keep only the last minute of requests
            
            if len(request_timestamps) >= MINUTE_LIMIT:
                sleep_time = 90 - (current_time - request_timestamps[-MINUTE_LIMIT])
                print(f"Rate limit reached. Sleeping for {sleep_time:.2f} seconds.")
                time.sleep(sleep_time)
            
            response = get_completion(prompt)
            request_timestamps.append(time.time())  # Log the time of this request
            return response

        response = rate_limited_get_completion(prompt)
        
        # Append the extracted instructions to the results list in a valid JSON format
        # results.append({"id": readme['id'], "response": response})


        
        # Append the extracted instructions to the results list
        results.append({"id":readme['id'],"response":response, "answers":readme_types})

    return results


# Example usage:
# Assuming your JSON file has an array of readmes
json_file_path = '../scr/output.json'
result_list = extract_installation_instructions_from_json(json_file_path)

# # Print the results
# for result in result_list:
#     for key, value in result.items():
#         print(f"{key}:")
#         print(value)
#         print()



with open("groq-responses-llama2-automatic.json", "w") as json_file:
    json.dump(result_list, json_file, indent=2)

print("LLM responses saved to groq-responses-llama2-automatic.json")
