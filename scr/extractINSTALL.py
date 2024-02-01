import requests
import re
import json
from nltk.tokenize import word_tokenize

def fetch_raw_markdown(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def extract_github_urls(markdown_content):
    pattern = re.compile(r'https://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+')
    return pattern.findall(markdown_content)

def fetch_readme_content(repo_url):
    readme_url = repo_url.replace("github.com", "raw.githubusercontent.com") + "/main/README.md"
    response = requests.get(readme_url)
    return response.text if response.status_code == 200 else None

def extract_installation_instructions(readme_content):
    keywords = ["installation", "setup", "install", "how to", "getting started", "quick start"]
    pattern = re.compile("|".join(keywords), re.IGNORECASE)
    sections = re.split(r'#+ ', readme_content)
    installation_sections = [section for section in sections if pattern.search(section)]
    return installation_sections

def tokenize_text(text):
    return word_tokenize(text)

# Main execution
awesome_list_url = "https://raw.githubusercontent.com/jamesmurdza/awesome-ai-devtools/main/README.md"
markdown_content = fetch_raw_markdown(awesome_list_url)
repos_data = []

if markdown_content:
    repos_urls = extract_github_urls(markdown_content)
    for repo_url in repos_urls:
        readme_content = fetch_readme_content(repo_url)
        if readme_content:
            installation_instructions = extract_installation_instructions(readme_content)
            instructions_text = " ".join(installation_instructions)
            tokens = tokenize_text(instructions_text)
            repos_data.append({
                "url": repo_url,
                "text": instructions_text,
                "tokens": tokens
            })
else:
    print("Failed to fetch the markdown content of the awesome list.")

# Output to a JSON file
with open('corpus.json', 'w') as outfile:
    json.dump(repos_data, outfile, indent=4)