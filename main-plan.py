import re
import json

text = """
Here are the installation instructions extracted from the provided README:

[
  {
    "type": "PackageManager",
    "steps": [
      {
        "text": "1. To download and install SICStus Prolog (it is needed), follow the instructions at <https://sicstus.sics.se/download4.html>."
      },
      {
        "text": "2. Then, you can download DALI and test it by running an example DALI MAS: ",
        "seq_order": 2
      }
    ]
  },
  {
    "type": "Binary",
    "steps": [
      {
        "text": "1. To download and install SICStus Prolog (it is needed), follow the instructions at <https://sicstus.sics.se/download4.html>."
      },
      {
        "text": "2. Then, you can download DALI from <https://github.com/AAAI-DISIM-UnivAQ/DALI.git>."
      },
      {
        "text": "3. Unzip the repository, go to the folder 'DALI/Examples/basic', and test if DALI works by double-clicking 'startmas.bat' file (this will launch an example DALI MAS).",
        "seq_order": 3
      }
    ]
  }
]

Confidence: 95%
"""

# Use regular expression to extract the JSON part
json_match = re.search(r'\[.*?\]', text, re.DOTALL)
if json_match:
    json_text = json_match.group(0)
    json_data = json.loads(json_text)
    print(json_data)
else:
    print("No JSON format dictionary found.")
