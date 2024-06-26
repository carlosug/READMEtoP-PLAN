## Information
Folder generated by the following scripts:

+ [`evaluate-STEP-zero-shot-LLAMA.py`](../evaluate-STEP-zero-shot-LLAMA.py)
+ [`evaluate-STEP-zero-shot-MISTRAL.py`](../evaluate-STEP-zero-shot-MISTRAL.py)


### Folder structure
- **Preprocessing**: contains annotated dataset
- **Rouge** (output generated from previous scripts):
    + [`post-annotated.json`](/Evaluation/Rouge/post-annotated.json): processed annotated dataset with the `evaluate scripts` abovementioned
    + [`post-groq-responses-llama2.json`](/Evaluation/Rouge/post-groq-responses-llama2.json): processed dataset with LLM responses
     + [`post-groq-responses-mistral.json`](/Evaluation/Rouge/post-groq-responses-mistral.json): processed dataset with LLM responses
     + ['scores-llama2.json'](/Evaluation/Rouge/scores-llama2.json): Rouge evaluation
     + ['scores-mistral.json'](/Evaluation/Rouge/scores-llama2.json): Rouge evaluation
     + ['rouge_scores-llama2-ids.json'](/Evaluation/Rouge/rouge_scores-llama2-ids.json): Ids Rouge evaluation
     + ['rouge_scores-mistral-ids.json'](/Evaluation/Rouge/rouge_scores-mistral-ids): Ids Rouge evaluation


> :warning: Please note that this repo is under development. The following scripts are being developed for improvements of results.  

For each readme:

- **1.** calculate steps detected/total identified: [`statistics-STEP-llms.py`](../statistics-STEP-llms.py) and [`graphs-STEP-llms.py`](../graphs-STEP-llms.py)

- **2.** % of steps in correct order: [`qualitative_error_analysis.md`](../qualitative_error_analysis.md) and

- **3.** calculate rouge for each instruction por cada Readme method:[`rouge-eval(llama).py`](../rouge-eval(llama).py) with the results output [`rouge_scores-llama2.json`](../rouge_scores-llama2.json); and [`rouge-eval(mistral).py`](../rouge-eval(llama).py) with the results output [`rouge_scores-mistral.json`](../rouge_scores-llama2.json). The report with the mean is computed with [`rouge_scores-GLOBAL.py`](../rouge_scores-GLOBAL.py) 