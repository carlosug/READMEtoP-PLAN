This folder contains full prompt responses for each model.

Parameters:
- PLAN:
    + Each USER request processed individually! I.e., each repo contains one response from the ASSISTANT.
- STEP:
    + Each USER request processed individually! I.e., each repo contains one response from the ASSISTANT.


### Prompts

| Prompt_ID | Type | Trigger Sentence  | Definitions |
| ----- | ----------------- | ---------------------- | --- |
| 101| zero-shot | Given the following README, extract the installation instructions for
each installation method. These methods are plans containing
instructions as steps for installing research software, to be executed
in a sequential order, and under defined conditions.  Write those instructions in sequential order such as: Step1: ..., Step2:
……StepN - …. Exclude code commands in the list. If the README does not
contain a sequence of instructions, then simply write "No steps
provided". Be concise. {README}```  | These methods are:. |


