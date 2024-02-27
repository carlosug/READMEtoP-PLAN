# Benchmark for installation instructions of Research/Scientific Software Repositories
---
This folder aims to keep track of the experiements related to the research question:

* can machines interpret and execute installation plans for Research/Scientific Software?

### 1. Selection criteria:
The repositories will be selected on community-curated list of software packages. Automated extraction of README files:
<!-- + Github repositories with specific topics -->
+ Most recent ML papers with repositories in [paperwithcodes]
<!-- + bioinformatics software documentation ([e.g](https://blog.bioconductor.org/posts/2022-10-22-awesome-lists/)) and/or [bio.tools](https://bio.tools/api/t/?documentationType=%22Installation+instructions%22&tool=%22Web%20service%22&programming%20language=%22python%22);
+ part of [awesome-healthcare list](https://github.com/kakoni/awesome-healthcare) or;
+ part of [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools);
+ part of [awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience);
+ part of [biological image analysis](https://github.com/hallvaaw/awesome-biological-image-analysis)
* part of [Awesome-genome-visualization](https://github.com/cmdcolin/awesome-genome-visualization) -->

---

### 2. Study Subjects inspected manually
The following versions of research software projects using Python were selected as study subjects:

<!-- # Select a representative sample of research software repositories from various domains and languages. This can be done manually or through automated means such as web scraping or API access. -->

| # | Repositories | Number | Topic |
| - | ----------------- | ----------- | ----------------------------- |
| 1 | [github](https://github.com/jenkinsci/jenkins) | [X]() | [LLM]() |  |  |
| 2 | [Paperwithcode](https://paperswithcode.com/api/v1/repositories/) | [X]() | [ML]() |  |  |
| 3 | [bio.tools](https://bio.tools/api/t/?documentationType=%22Installation+instructions%22&tool=%22Web%20service%22&programming%20language=%22python%22) | [X]() | [Bioinformatics]() |  |  |
| 4 | [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) | [250]() | [LLMs]() |  |  |
| 5 | [Awesome-genome-visualization](https://github.com/cmdcolin/awesome-genome-visualization)| [150](https://github.com/stanfordnlp/CoreNLP/commit/f7782ff5f235584b0fc559f266961b5ab013556a) | [Genomics]() |  |  |


<!-- ### Available software repositories
A list of research software registries (also known as catalog, index, warehouse, repository, hub, platform, and other terms) can be found here: [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries) 

* [Research software directory]()
* [4TUResearchData repository]()
* [Codewithpapers](https://paperswithcode.com/) -->




<!-- ### Benchmark file
**installationtype.csv**
Annotated benchmark, curated by hand. It contains following fields (associated with [CodeMeta properties](https://raw.githubusercontent.com/codemeta/codemeta/2.0/codemeta.jsonld):
* SoftwareSourceCode: repository URL end-point
* annotator: person who annotated
* **readme**
* SoftwareApplication: software type installation
* downloadUrl
* installUrl
* operatingSystem
* programmingLanguage
* softwareRequirements
* **buildInstructions** -->

---
<!-- ### 3. Classify research software installation options (`Method`) and level of difficulty: -->

### Definitions: 

1. **Installation Methods**: indicates a procedure o **Plan** which contains instructions as **Steps** for installing a research software that must be performed in a precise order and under specific conditions. In context of the study, there four general different methods (see below).

2. **`Plan`**: a sequence/collection of instatiated **Step(s)** that a machine executes to fulfil its objective in installation. A installation Method (similar to installation procedure or option) is an instance of the `Plan`. A installation method is an instance of the **Plan** concept. In our study, a README can describe one, or more Plans. We define four general `p-plan:Plan`:

| Plan | Name  | README text |
| ----- | ----------------- | ---------------------- |
| 0| source |  ```Install from Source``` or ```Native Installation``` |
| 1| container | ```Installation with Docker``` or ```Isolated Docker option``` |
| 2| package manager | ```with Pip``` or `with conda` |
| 3| binary | ```Install from source``` |
<!-- - **Level of difficulty**: a position on scale that quantify the relative difficulty of completing a task related to installation process in the R/S software. It measures how complex a task is to execute and incluces several `Factors` determine its level. -->

<!-- ```Factor(s)```: type of software, clarity of instructions, presence of **Dependencies**, number of **Steps** involved, and available optional installation methods in the readme. ``Factor(s)`` describes the variables as something akin to `software understanding features`, the features with the goal of facilitating the adoption of a software[ref.Inspect4py](Inspect4py). It includes **DISCLAIMER: bear in mind that determining the exact level of difficulty can still be subjective depending on individual experiences and expertise**.  Based on the given factors, here the scoring scheme could be: -->

Additionally, for each Plan, the following features as **technology** property belongs to a specific Plan. For example:
- Plan 0 --> Operating System --> a system program that manages the research software installation process --> {linux, windows, mac}
- Plan 1 --> Container --> a tool that orchestrates the software installation process --> {docker, docker-compose, Podman}
- Plan 2--> Package Manager --> a method to install and manage software the installation process --> {pip, conda, bioconda}

3. **`Step(s)`**: a list of planned activities as part of a `Plan` to be executed in a specific order. A Step could comprise more than one **action**. Then, a Step within a Plan could be linked to one specific executable operation e.g. *Step 1: First clone this repository via Git*, or refer to a group of activities e.g. *Step 2: Create a new Conda environment and activate it.* We define a Step as the sentence of a readme. Each sentence in a readme is an instance of the Step concept. For instance, the following example shows that `Step 1` involves two activities, and `Step 2` involves one activity:

`## Step 1: activity1[Clone the repository] and actvity2[create a virtual environment]`

`## Step 2: activity3[Cofigure] the installation with required dependencies`

---
#### 1. Installation methods:
**Method 0: Source-based installation**

- **Goal**: provide a standardized command-line interface for managing software packages installation process and its dependencies.
- **Definition**: Installing a software "from source" means installing a software without using automatic tools e.g. container or package manager.
- **Properties**:
1. Running in command line mode;
2. Deal with source code dependencies;
3. Compile the source code and copy the binaries to your computer instead;
4. Build the source code yourself, dealing with the dependencies. 
`Comments`: Also it is called `compile from source`or `native installation`

**Method 1: Package manager-based installation**

- **Goal**: provide the source code that contains the original code written by a developer/researcher to enable the ability to review the source code and understand its workings
- **Definition**: Installing a software "from source" means installing the software along with its dependencies indexed in official package managers.
- **Properties**:

| Name | Channel | Steps | Commands |
| ----- | ----------------- | ---------------------- | --- |
| Conda| bioconda | 1 |  ```conda install bioconda::sambamba``` or ```conda install bioconda/label/cf201901::sambamba``` |
| GNU Guix| - | 1 | ```guix install sambamba``` or ```guix install sambamba``` |
| Homebrew| homebrew-bio | 1  | ```brew install brewsci/bio/sambamba``` |
| Fedora| dnf | 1  | ```dnf install package``` |
| Debian| apt | 1 | ```apt install package``` |
|Pypi| pip | 1 | ```pypi install package``` |

**Method 2: Container-based installation**
+ **Goal**: provide a way of packaging research software and their dependencies inside lightweight, standalone containers.
+ **Definition**:  a method to create isolated environments where the application runs consistently regardless of the host environment. Popular container platforms include Docker, Podman, and Singularity.
+ **Properties**:


**Method 3: Binary-based installation**

- **Goal**: provide the downloading and running precompiled executable files or libraries specifically designed for a particular operating system and architecture. It is typically located in Github sources and binary releases.
- **Definition**: a binary files contains the entire codebase and associated resources needed to run the software, eliminating the need for compilation or building the software from source.
- **Properties**:
+ precompiled binaries are ready-to-run executable files
+ Deal with binary dependencies
+ Running usually in in user interface mode
<!-- - **General Steps**:
1. Step 1: Download the tarball.
2. Step 2: Unpack it
3. Step 3: Run it according to the accompanying release notes
4. To download and build binaries ` commands`:

```bash
wget https://download.example.org/example.tar.xz
tar xcJf example.tar.xz
cd example
./configure
make
```

`Notes`" Sometimes readme contains example on `cmd`:[https://www.qemu.org/download/](https://www.qemu.org/download/) -->

--
### Installation instructions as Step
Capture a collection of **`Step(s)`** within a **`Plan`** for acomplishing research software installation **`Task(s)`**.

### JSON Structure
---
**Translating abstract to executable instructions**

Create a method to connect human-readable language instructions to Step(s) (or activity) and collection of Steps as installation Plans in a research software installation task. We limit ourselves to tasks that can be characterized as "software installation and involve manually downloading, extracting, compiling, or configuring individual components. Examples of such tasks are also run a single command to install the desired software and its dependencies. To the best of our knowledge this work is the first to mine complex task descriptions from the readmes and translate them into executable agent plans.

We will present the different steps from the instruction in natural language to an executable plan with the example sentence. Dictionary structure of `ground_true_plan_steps.json`:

```json
{
    "research_softwares": { # (total number of research softwares)
        "research_software": [ # (research software dictionary)
            {
                "id": "1", # (unique research software ID)
                "name": "AAAI-DISIM-UnivAQ/DALI", # (repository name of research software)
                "url": "https://raw.githubusercontent.com/AAAI-DISIM-UnivAQ/DALI/master/README.md", # (readme URL)
                "n_plans": 2, # (count of plans in a research software)
                "plan_nodes": # (Plans info)
                    {
                        "type": "Source", # (one of the listed 4 plan types)
                        "plan_step": [
                            "Step 1: To download and install SICStus Prolog (it is needed), follow the instructions at https://sicstus.sics.se/download4.html.", # (step-by-step1 initial instruction)
                            "Step 2: Then, you can download DALI and test it by running an example DALI MAS" # (step-by-step2 end instruction)
                        ],
                        "technology": ["Linux"] # (plan for technology property)
                    },
                    {
                        "type": "Source", # (one of the listed 4 plan types)
                        "plan_step": [
                            "Step 1: To download and install SICStus Prolog (it is needed), follow the instructions at https://sicstus.sics.se/download4.html.", # (step-by-step1 initial instruction)
                            "Step 2: Then, you can download DALI and test it by running an example DALI MAS", # (step-by-step2 instruction)
                            "Step 3: Unzip the repository go to the folder DALI/Examples/basic, and test if DALI works by duble clicking startmas.bat file (this will launch an example DALI MAS)" # (step-by-step3 end instruction)
                        ],
                        "technology": ["Windows"] # (plan for technology type)
                    }
                ],
                "readme_instructions": "", # (raw content of the readme)
                "skip_content": "" # (annotation comments)
            }
        ]
    }
}
```

<!-- To download and build binaries from **git**

```git clone https://github.com/example.git```

```cd example```

```git submodule init```

```git submodule update --recursive```

```./configure```

```make``` -->



<!-- **Main Software type**
Levels of granuality on which software can be described. From top to the bottom:

| Type | Description | *Examples* |
| ----- | ----------------- |--|
| Bundle| A container with metadata about the software and its functionality | *N3.js library* |
| Library| A collection of components (codes) which are used to construct other software| *N3.js library* |
| Package| A tool that is aimed to be executed through the command-line| *somef* |
| Module| A concrete software package | *N3.js 0.10.0* |
| Component| A specific part of a module that runs in a specific environment and set of parameters | *N3.js 0.10.0 Parser* |
| Script| A code written for some run-time environment| *script.py* |
| Service| A collection of codes where the main functionality is to start a web service via scripts | *reactjs* | -->

<!-- Other taxonomy of types are considered [biotoolsSchema](https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/controlled_vocabularies.rst) -->


<!-- #### Level of difficulty
We manually categorise the level of difficulty the README installation_instruction has in our sample as:

* `Simple`: Label a research software repository with straightforward installation process. -->

<!-- `## Installation prerequisites`
- Python >= 3.8

`## Installation method pip:`
Install the library using pip:

`bash
pip install myprojectML
` -->

<!-- 
* `Moderate`: label a research software repository that requires several `dependencies,` and offers multiple installation methods (or options). Especially for DL frameworks. -->


<!-- `## Prerequisites`
- CUDA Toolkit (for GPU acceleration)
- TensorFlow >=2.0
- scikit-learn

`## Installation via pip`
If you don't have CUDA installed, use pip to install the CPU-only version:

`bash
pip install mynlpframework_cpu
`

or

`# If you have CUDA installed, use pip to install the GPU version:`

`bash
pip install mynlpframework
` -->


<!-- * `Complex`: it has numerous dependencies, more than one installation method available in readme, and complex configuration requirements  -->


---
<!-- 
#### Matrix Installation methods and level of Difficulty:
| Method | Description | Text | Code | Steps | Difficulty | README section |
| ----- | ----------------- | ---------------------- | -------------------- | ------- | -------- | -- |
| Source-based| Raw material (source) with a compiler to download the executable that machines then runs| ## Install from GitHub. To run, please follow the next steps: 1. Clone this GitHub repository. 2. Install software (you should be in the folder that you just cloned). 3. Test installation | ```git clone https://github.com.git``` ```cd folder pip install -e .``` ```software --help```| 3 | Complex | `## from source`, `##from Github`|
| Package Manager-based| A tool written for some run-time environment| ## Install from Pip: | `pip install software` |1 | Simple | `## from package manager`|
| Container-based| A tool that is aimed to be executed through the command-line| ## Installing Through Docker. To run through Docker, use the Docker image already built. Then, to run your image just type: | `docker pull image` ```bash docker run -it image /bin/bash```| 2 | Moderate | `## Installing through Docker` |
| Binary-based| Github source and binary releases (binary dependencies) | ## download the tarball, unpack it, and run it (ready-to-run)  | none | 3 | Moderate | |


**Scoring system/scheme based on all factors**
| Factors | Definition | Points |
|----------|------------| ---- |
| **Number requirements**| Provide a list of required packages and their versions | 1-5 |
| **Number of dependencies** | list the internal and external modules used by the target (to be installed) software.  A larger number of dependencies may indicate more complexity | 1-5 |
| **Number installation methods** | available the different alternatives to install the software | 1-5 |
| **Main software type** | Estimates whether the target software is a package, library, service or scripts | 1 - 4 |
| **Clarity on instructions** | writes concise and clear instructions | 0-3 |
| **Method 1 only** | from source (calculate length steps) | 3 |
| **Method 2 only** | from PiP | 1 |
| **Method 3 only** | from Container | 2 | -->


<!-- ```py
def count_dependencies(requirements_file):
    """Count the number of dependencies in a requirements file."""
    try:
        with open(requirements_file) as f:
            content = f.readlines()
            num_deps = sum([len(line.strip().split()) > 0 for line in content])
            return num_deps
    except FileNotFoundError:
        print(f"Could not find '{requirements_file}'.")
        return 0

def check_platform_compatibility(os_info):
    """Check platform compatibility based on operating system info."""
    supported_os = ["Linux", "Windows", "MacOS"]
    if os.name in supported_os:
        return 3
    elif "RHEL" in os_info or "CentOS" in os_info:
        return 2
    else:
        return 0

def check_clarity_of_instructions(readme):
    """Determine clarity of instructions based on README content."""
    clear_keywords = ["simple", "quick", "intuitive", "clear"]
    num_clear_keywords = sum([1 for word in readme.lower().split() if word in clear_keywords])
    return min(num_clear_keywords, 3)

def check_availability_automation_tools(setup_script):
    """Check for availability of automation tools in setup script."""
    available_tools = ["make", "cmake", "pip", "conda"]
    return int(any([tool in setup_script for tool in available_tools])) * 2

def check_presence_precompiled_binaries(downloads_folder):
    """Check for presence of precompiled binaries in downloads folder."""
    num_binary_files = sum([os.path.isfile(os.path.join(downloads_folder, f)) for f in os.listdir(downloads_folder)])
    return int(num_binary_files > 0) * 2

def check_known_issues(issue_count):
    """Determine impact of known issues based on issue count."""
    critical_issues = ["build failure", "runtime error"]
    severe_issues = ["major functionality loss"]
    moderate_issues = ["minor bugs"]
    weighted_score = sum([1 if issue in critical_issues else (issue_count // 10 if issue in severe_issues else (issue_count // 100 if issue in moderate_issues else 0)) for issue in issues])
    return min(weighted_score, 3)

def analyze_installation(req_file, setup_script, readme, downloads_folder, os_info):
    """Analyze installation complexity based on input parameters."""
    issues = []
    deps = count_dependencies(req_file)
    plat_comp = check_platform_compatibility(os_info)
    clar_inst = check_clarity_of_instructions(readme)
    auto_tools = check_availability_automation_tools(setup_script)
    binary_files = check_presence_precompiled_binaries(downloads_folder)
    known_issues = check_known_issues(len(issues))

    score = deps + plat_comp + clar_inst + auto_tools + binary_files + known_issues
    complexity = ""

    if score <= 3:
        complexity = "Easy"
    elif score <= 9:
        complexity = "Moderate"
    else:
        complexity = "Hard"

    return complexity
``` -->

---



<!-- #### 1. structure of instructions is identified -->
<!-- 
unified model that reuses several semantic models to show how a installation process can be semantically modeled -->

<!-- Let `concepts(w)` be the set of ontological concepts to which the word `w` could be mapped. For a `single instruction (ai, oi, pi)` consisting of an `action verb ai`, an `object oi` and a set of `prepositions` -->



<!-- **Ontological `concepts`**

**1.Properties**:

**2. Classes**: -->
 

 <!-- *e.g. Method 1: Install package from source:* -->



<!-- **`p-plan:Variable`**: a list of indivisible sequence of *Operations* that must executed without interruption. A concept similar to `bpmn:ScriptTask` *e.g.`git clone software`, `python3 -m venv .venv`* **[DISCLAIMER = it can be associated with a p-plan:Variable to represent input of the step such code blocks(to denote word or phrase as code) enclose it in backticks (`)** -->

<!-- Steps within a Plan could be linked to a specific executable step (or `Action`) or refer to a class of `Steps`. A plan `Step` could be performed in different executions of the same plan. -->


<!-- Optional:
**`Task(s)`**: a list of computationally actions steps in software installation domain. *e.g Method 1: From source* *(TBC)*
Possibility to define **`SubPlans`** *e.g. alternative methods for installing software* within the Plan (similar to procedure) as **`p-plan:MultiStep`** -->



#### 2. Resolve the meaning of the words using Cyc Ontology and or P-plan

<!-- **Formal Instruction Representation**

Each step Step1P1, Step2P1, etc is an instance of an step concept like *Clone this repo*. The Step *Clone this repo* needs to have information about the repository (object) to be cloned and the location where this object is to be placed. For execution, the formal instruction representation has to be transformed into a valid machine-readable plan. The plans for a machine are implemented in P-PLAN, which provides an expressive and extensible vocabulary representation for semantically writing and describing plans *e.g. scientific workflows* to machines.

Example of the Plan: Install software [https://raw.githubusercontent.com/lm-sys/FastChat/main/README.md](https://raw.githubusercontent.com/lm-sys/FastChat/main/README.md)

```ttl
@prefix p-plan: <http://purl.org/net/p-plan#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix bpmn: <http://www.w3.org/ns/bpmn#> .

# Define the Plan _:P1
_:P1 a p-plan:Plan ;
    rdfs:label "Method 1: With pip" ;
    p-plan:isStepOfPlan _:Step1P1 .

# Define the Step _:Step1P1
_:Step1P1 a p-plan:Step, bpmn:ScriptTask ;
    rdfs:label "pip3 install 'fschat[model_worker,webui]'" ;
    p-plan:isStepOfPlan _:P1 .

# Define the Plan _:P2
_:P2 a p-plan:Plan ;
    rdfs:label "Method 2: From source" ;
    p-plan:isStepOfPlan _:Step1P2, _:Step2P2, _:Step2P3, _:Step2P4 .

# Define the Step _:Step1P2
_:Step1P2 a p-plan:Step, bpmn:ManualTask ;
    rdfs:label "git clone https://github.com/lm-sys/FastChat.git" ;
    rdfs:comment "1. Clone this repository and" ;
    p-plan:isStepOfPlan _:P2 .

_:Step2P2 a p-plan:Step, bpmn:ScriptTask ;
    rdfs:label "cd FastChat" ;
    rdfs:comment "navigate to the FastChat folder" ;
    p-plan:isStepOfPlan _:P2 .

_:Step2P3 a p-plan:Step, bpmn:ScriptTask ;
    rdfs:label "brew install rust cmake" ;
    rdfs:comment "If you are running on Mac" ;
    p-plan:isStepOfPlan _:P2 .

_:Step2P4 a p-plan:Step, bpmn:ScriptTask ;
    rdfs:label "pip3 install --upgrade pip # enable PEP 660 support pip3 install -e .[model_worker,webui]" ;
    rdfs:comment "2. Install Package" ;
    p-plan:isStepOfPlan _:P2 .

``` -->