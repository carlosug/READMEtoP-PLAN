# Benchmark for installation instructions of research software repositories
---
This folder aims to keep track of the experiements related to the research question:

* can machines interpret and execute installation plans for biomedical software?

### 1. Selection criteria:
The repositories will be selected on community-curated list of software packages. Automated extraction of README files:
+ Github repositories with specific topics
+ Most recent ML papers with repositories in [paperwithcodes]
+ bioinformatics software documentation ([e.g](https://blog.bioconductor.org/posts/2022-10-22-awesome-lists/)) and/or [bio.tools](https://bio.tools/api/t/?documentationType=%22Installation+instructions%22&tool=%22Web%20service%22&programming%20language=%22python%22);
+ part of [awesome-healthcare list](https://github.com/kakoni/awesome-healthcare) or;
+ part of [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools);
+ part of [awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience);
+ part of [biological image analysis](https://github.com/hallvaaw/awesome-biological-image-analysis)
* part of [Awesome-genome-visualization](https://github.com/cmdcolin/awesome-genome-visualization)

---

### 2. Study Subjects inspected manually
The following versions of 26 research software projects using Python were selected as study subjects:

<!-- # Select a representative sample of research software repositories from various domains and languages. This can be done manually or through automated means such as web scraping or API access. -->

| # | GitHub Repository | Stars | Stable release as of 01.01.23 |
| - | ----------------- | ----------- | ----------------------------- |
| 1 | [jenkins](https://github.com/jenkinsci/jenkins) | [ce7e5d7](https://github.com/jenkinsci/jenkins/commit/ce7e5d70373a36c8d26d4117384a9c5cb57ff1c1) | [2.384](https://mvnrepository.com/artifact/org.jenkins-ci.main/jenkins-core/2.384) |  |  |
| 2 | [mybatis-3](https://github.com/mybatis/mybatis-3) | [c195f12](https://github.com/mybatis/mybatis-3/commit/c195f12808a88a1ee245dc86d9c1621042655970) | [3.5.11](https://mvnrepository.com/artifact/org.mybatis/mybatis/3.5.11) |  |  |
| 3 | [flink](https://github.com/apache/flink) | [c41c8e5](https://github.com/apache/flink/commit/c41c8e5cfab683da8135d6c822693ef851d6e2b7) | [1.15.3](https://mvnrepository.com/artifact/org.apache.flink/flink-core/1.15.3) |  |  |
| 4 | [checkstyle](https://github.com/checkstyle/checkstyle) | [233c91b](https://github.com/checkstyle/checkstyle/commit/233c91be45abc1ddf67c1df7bc8f9f8ab64caa1c) | [10.6.0](https://mvnrepository.com/artifact/com.puppycrawl.tools/checkstyle/10.6.0) |  |  |
| 5 | [CoreNLP](https://github.com/stanfordnlp/CoreNLP) | [f7782ff](https://github.com/stanfordnlp/CoreNLP/commit/f7782ff5f235584b0fc559f266961b5ab013556a) | [4.5.1](https://mvnrepository.com/artifact/edu.stanford.nlp/stanford-corenlp/4.5.1) |  |  |


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
### 3. Classify research software installation options (`Method`) and level of difficulty:

**Context**: Currently unknown standards for measuring level of difficulty in a research software installation process, and the ```Factor(s)``` that impact the different `Methods` installation process and its `Level of difficulty`.

#### Definitions: 
- **Installation Methods**: instructions to follow in a research software installation process. In context of the study, there are several different methods (see below).
- **Level of difficulty**: We define `level of difficulty` of the installation process as the state or degree of being intricate or complicated to complete the process successfully.

```Factor(s)```: type of software, clarity of instructions, presence of **Dependencies**, number of **Steps** involved, errors in the installation process. ``Factor(s)`` describes the variables as something akin to `software understanding features`, the features with the goal of facilitating the adoption of a software[ref.Inspect4py](Inspect4py). It includes **DISCLAIMER: bear in mind that determining the exact level of difficulty can still be subjective depending on individual experiences and expertise**:

| Features | Definition |
|----------|------------|
| Requirements | Provide a list of required packages and their versions |
| Dependencies | list the internal and external modules used by the target (to be installed) software.  A larger number of dependencies may indicate more complexity |
| **Software invocation** | ranks the different alternatives to run the software component based on relevance |
| **Main software type** | Estimates whether the target software is a package, library, srvice or scripts |
| **Detailed instructions** | writes concise and clear instructions |
| **Containerization** | helps researchers dealing with complex installation |
| **Package managers** | eases difficulty in installation proccess |


#### Installation methods:

**Method 1: Source-based installation**

- **Goal**: provide a standardized command-line interface for managing software packages installation process and its dependencies.
- **Definition**: Installing a software "from source" means installing a software without using automatic tools e.g. container or package manager.
- **Requiremements**:
- Running in command line mode;
- Deal with source code dependencies;
- Compile the source code and copy the binaries to your computer instead;
- Build the source code yourself, dealing with the dependencies. 
`Comments`: Development setup sometimes it is called compile from source

**Method 2: Package manager-based installation**

- **Goal**: provide the source code that contains the original code written by a developer/researcher to enable the ability to review the source code and understand its workings
- **Definition**: Installing a software "from source" means installing the software along with its dependencies indexed in official package managers.
- **Requirements**

| Name | Channel | Steps | Commands |
| ----- | ----------------- | ---------------------- | --- |
| Conda| bioconda | 1 |  ```conda install bioconda::sambamba``` or ```conda install bioconda/label/cf201901::sambamba``` |
| GNU Guix| | 1 | ```guix install sambamba``` or | ```guix install sambamba``` |
| Homebrew| homebrew-bio | 1  | ```brew install brewsci/bio/sambamba``` |
| Fedora| dnf | 1  | ```dnf install package``` |
| Debian| apt | 1 | ```apt install package``` |
|Pypi| | pip | ```pypi install package``` |

**Method 3: Container-based installation**

+ **Goal**: provide a way of packaging research software and their dependencies inside lightweight, standalone containers.
+ **Definition**:  a method to create isolated environments where the application runs consistently regardless of the host environment. Popular container platforms include Docker, Podman, and Singularity.
+ **Requirements**:

**Method 4: Binary-based installation**

- **Goal**: provide the downloading and running precompiled executable files or libraries specifically designed for a particular operating system and architecture
- **Definition**: a binary files contains the entire codebase and associated resources needed to run the software, eliminating the need for compilation or building the software from source.
- **Requirements**
+ precompiled binaries are ready-to-run executable files
+ Deal with binary dependencies
+ Running usually in in user interface mode

Sometimes readme contains example on `cmd`:[https://www.qemu.org/download/](https://www.qemu.org/download/)

To download and build binaries
```wget https://download.example.org/example.tar.xz```
```tar xcJf example.tar.xz```
```cd example```
```./configure```
```make```

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


#### Level of difficulty
We manually categorise the level of difficulty the README installation_instruction has in our sample as:

* `Simple`: Label a research software repository with straightforward installation process.

<!-- `## Installation prerequisites`
- Python >= 3.8

`## Installation method pip:`
Install the library using pip:

`bash
pip install myprojectML
` -->


* `Moderate`: label a research software repository that requires several `dependencies` and offers multiple installation methods (or options). Especially for DL frameworks.


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


* `Complex`: it has numerous dependencies and complex configuration requirements


---

#### Matrix Installation methods and level of Difficulty:
| Method | Description | Text | Code | Steps | Difficulty | README section |
| ----- | ----------------- | ---------------------- | -------------------- | ------- | -------- | -- |
| Source-based| Raw material (source) with a compiler to download the executable that machines then runs| ## Install from GitHub. To run, please follow the next steps: 1. Clone this GitHub repository. 2. Install software (you should be in the folder that you just cloned). 3. Test installation | ```git clone https://github.com.git``` ```cd folder pip install -e .``` ```software --help```| 3 | Complex | `## from source`, `##from Github`|
| Package Manager-based| A tool written for some run-time environment| ## Install from Pip: | `pip install software` |1 | Simple | `## from package manager`|
| Container-based| A tool that is aimed to be executed through the command-line| ## Installing Through Docker. To run through Docker, use the Docker image already built. Then, to run your image just type: | `docker pull image` ```bash docker run -it image /bin/bash```| 2 | Moderate | `## Installing through Docker` |
| Binary-based| Github source and binary releases (binary dependencies) | ## download the tarball, unpack it, and run it (ready-to-run)  | none | 3 | Moderate | |

---

### 4. Translating abstract to executable instructions

Create a method to connect human-readable language instructions to steps (or activity) and collection of steps in software installation domain (machine learning a planning domain). We limit ourselves to tasks that can be characterized as "software installation and involve manually downloading, extracting, compiling, or configuring individual components; instead, they just. Examples of such tasks are also run a single command to install the desired software and its dependencies. To the best of our knowledge this work is the first to mine complex task descriptions from the readmes and translate them into executable agent plans.


We will present the different steps from the instruction in natural language to an executable plan with the example sentence **"Place the cup on the table"** **Install package from source**.


#### 1. structure of instructions is identified
<!-- 
unified model that reuses several semantic models to show how a installation process can be semantically modeled -->

<!-- Let `concepts(w)` be the set of ontological concepts to which the word `w` could be mapped. For a `single instruction (ai, oi, pi)` consisting of an `action verb ai`, an `object oi` and a set of `prepositions` -->

**GOAL**= Capture a collection of **`Step(s)`** within a **`Plan`** for acomplishing software installation **`Task(s)`**

**Ontological `concepts`**

**`p-plan:Plan`**: a sequence/collection of instatiated **Step(s)** that a machine executes to fulfil its objective in installation. A installation Method (similar to procedure or option) is an instance of the `Plan` *e.g. Method 2: Install package from source:*

**`p-plan:Step(s)`**: a list of planned Action(s) or *Activity* or *Task* as part of a `Plan` to be executed by an Agent *e.g. First clone the repository from source , then create virtual environment*. 

**`p-plan:Variable`**: a list of indivisible sequence of *Operations* that must executed without interruption. A concept similar to `bpmn:ScriptTask` *e.g.`git clone software`, `python3 -m venv .venv`* **[DISCLAIMER = it can be associated with a p-plan:Variable to represent input of the step such code blocks(to denote word or phrase as code) enclose it in backticks (`)**

<!-- Steps within a Plan could be linked to a specific executable step (or `Action`) or refer to a class of `Steps`. A plan `Step` could be performed in different executions of the same plan. -->


Optional:
**`Task(s)`**: a list of computationally actions steps in software installation domain. *e.g Method 1: From source* *(TBC)*
Possibility to define **`SubPlans`** *e.g. alternative methods for installing software* within the Plan (similar to procedure) as **`p-plan:MultiStep`**



#### 2. Resolve the meaning of the words using Cyc Ontology and or P-plan

**Formal Instruction Representation**

Each step action1, action2, etc is an instance of an action concept like *CloneTheRepository*. The action *CloneTheRepository* needs to have information about the object to be manipulated and the location where this object is to be placed. For execution, the formal instruction representation has to be transformed into a valid machine-readable plan. The plans for a machine are implemented in P-PLAN, which provides an expressive and extensible vocabulary representation for semantically writing and describing plans *e.g. scientific workflows* to machines.

Example of the Plan: Install software [https://raw.githubusercontent.com/lm-sys/FastChat/main/README.md](https://raw.githubusercontent.com/lm-sys/FastChat/main/README.md)

```ttl
@prefix p-plan: <http://purl.org/net/p-plan#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix bpmn: <http://www.w3.org/ns/ ## no found w3 ttl

# Define the Plan
_:P1 a p-plan:Plan ;
    rdfs:label "### Method 1: With pip" ;
    p-plan:isStepOfPlan _:Step1P1 .

# Define the Step _:Step1P1
_:Step1P1 a p-plan:Step ;
    rdf:type bpmn:ScriptTasks ;
    rdfs:label "```bash pip3 install "fschat[model_worker,webui]"```" ;
    p-plan:isStepOfPlan _:P1 . # final step of Plan _:P1 .

# Define the Plan
_:P2 a p-plan:Plan ;
    rdfs:label "### Method 2: From source" ;
    rdf:type bpmn:ManualTasks ;
    p-plan:isStepOfPlan _:Step1P2, Step2P2, Step2P3 .

# Define the Step _:Step1P2
_:Step1P2 a p-plan:Step ;
    rdfs:label "```bash git clone https://github.com/lm-sys/FastChat.git```" ;
    rdfs:comment "1. Clone this repository and" ;
    rdf:type bpmn:ManualTasks ;
    p-plan:isStepOfPlan _:P2 .

_:Step2P2 a p-plan:Step ;
    rdfs:label "```cd FastChat```" ;
    rdfs:comment "navigate to the FastChat folder" ;
    rdf:type bpmn:ScriptTasks ;
    p-plan:isStepOfPlan _:P2 .

_:Step2P3 a p-plan:Step ;
    rdfs:label "```bash brew install rust cmake```" ;
    rdfs:comment "If you are running on Mac" ;
    p-plan:isStepOfPlan _:P2 . # optional step

_:Step2P4 a p-plan:Step ;
    rdfs:label "```bash pip3 install --upgrade pip  # enable PEP 660 support pip3 install -e".[model_worker,webui]```"" ;
    rdfs:comment "2. Install Package" ;
    p-plan:isStepOfPlan _:P2 . # final step
```