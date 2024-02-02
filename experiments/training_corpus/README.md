# Benchmark for installation instructions of software repositories
---
This folder aims to keep track of the experiements related to the research question:

* can machines interpret and execute installation plans for biomedical software?

### Selection criteria [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) :
The repositories will be selected on community-curated list of software packages:
+ bioinformatics software documentation ([e.g](https://blog.bioconductor.org/posts/2022-10-22-awesome-lists/)) and/or [bio.tools](https://bio.tools/api/t/?documentationType=%22Installation+instructions%22&tool=%22Web%20service%22&programming%20language=%22python%22);
+ part of [awesome-healthcare list](https://github.com/kakoni/awesome-healthcare) or;
+ part of [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools);
+ part of [awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience);
+ part of [biological image analysis](https://github.com/hallvaaw/awesome-biological-image-analysis)
* part of [Awesome-genome-visualization](https://github.com/cmdcolin/awesome-genome-visualization)


## Study Subjects
The following versions of 26 Java projects using Maven were selected as study subjects:

| # | GitHub Repository | Commit Hash | Stable release as of 01.01.23 |
| - | ----------------- | ----------- | ----------------------------- |
| 1 | [jenkins](https://github.com/jenkinsci/jenkins) | [ce7e5d7](https://github.com/jenkinsci/jenkins/commit/ce7e5d70373a36c8d26d4117384a9c5cb57ff1c1) | [2.384](https://mvnrepository.com/artifact/org.jenkins-ci.main/jenkins-core/2.384) |  |  |
| 2 | [mybatis-3](https://github.com/mybatis/mybatis-3) | [c195f12](https://github.com/mybatis/mybatis-3/commit/c195f12808a88a1ee245dc86d9c1621042655970) | [3.5.11](https://mvnrepository.com/artifact/org.mybatis/mybatis/3.5.11) |  |  |
| 3 | [flink](https://github.com/apache/flink) | [c41c8e5](https://github.com/apache/flink/commit/c41c8e5cfab683da8135d6c822693ef851d6e2b7) | [1.15.3](https://mvnrepository.com/artifact/org.apache.flink/flink-core/1.15.3) |  |  |
| 4 | [checkstyle](https://github.com/checkstyle/checkstyle) | [233c91b](https://github.com/checkstyle/checkstyle/commit/233c91be45abc1ddf67c1df7bc8f9f8ab64caa1c) | [10.6.0](https://mvnrepository.com/artifact/com.puppycrawl.tools/checkstyle/10.6.0) |  |  |
| 5 | [CoreNLP](https://github.com/stanfordnlp/CoreNLP) | [f7782ff](https://github.com/stanfordnlp/CoreNLP/commit/f7782ff5f235584b0fc559f266961b5ab013556a) | [4.5.1](https://mvnrepository.com/artifact/edu.stanford.nlp/stanford-corenlp/4.5.1) |  |  |

Also thinking about LLMs for bioinformatics

### Available software repositories
A list of research software registries (also known as catalog, index, warehouse, repository, hub, platform, and other terms) can be found here: [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries) 

* [Research software directory]()
* [4TUResearchData repository]()
* [Codewithpapers](https://paperswithcode.com/)




### Benchmark file
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
* **buildInstructions**


**Context**: Currently unknown the ```Factor(s)``` that impact the installation process and its level of difficulty.
**Definition**: The level of difficulty of the installation process is defined as the state or degree of being intricate or complicated to complete the process successfully.

```Factor(s)```: type of software, clarity of instructions, presence of **Dependencies**, number of **Steps** involved, errors in the installation process. ``Factor(s)`` describes the variables as something akin to `software understanding features`, the features with the goal of facilitating the adoption of a software[ref.Inspect4py](Inspect4py). It includes:

| Features | Definition |
|----------|------------|
| Class metadata | Extract information such as name, methods, function arguments |
| Requirements | Provide a list of required packages and their versions |
| Dependencies | list the internal and external modules used by the target (to be installed) software |
| **Software invocation** | ranks the different alternatives to run the software component based on relevance |
| **Main software type** | Estimates whether the target software is a package, library, srvice or scripts |

**Main Software type**
Levels of granuality on which software can be described. From top to the bottom:

| Type | Description | *Examples* |
| ----- | ----------------- |--|
| Bundle| A container with metadata about the software and its functionality | *N3.js library* |
| Library| A collection of components (codes) which are used to construct other software| *N3.js library* |
| Package| A tool that is aimed to be executed through the command-line| *somef* |
| Module| A concrete software package | *N3.js 0.10.0* |
| Component| A specific part of a module that runs in a specific environment and set of parameters | *N3.js 0.10.0 Parser* |
| Script| A code written for some run-time environment| *script.py* |
| Service| A collection of codes where the main functionality is to start a web service via scripts | *reactjs* |

Other taxonomy of types are considered [biotoolsSchema](https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/controlled_vocabularies.rst)

### Taxonomy of research software installation types (`Method`) and level of difficulty


| Method | Description | Difficulty | Method(s) | Steps | Dependec | README section |
| ----- | ----------------- | ---------------------- | -------------------- | ------- | -------- | -- |
| Source-based| Raw material (source) with a compiler to download the executable that machines then runs| High | Git and official release websites | Download the compiler and install all the required libraries manually  | | `## Manual install` , `## from source`, `## Install from Github`|
| Package Manager-based| A tool written for some run-time environment| Low | Pip |1 |`## Install from Pypi` | |
| Container-based| A tool that is aimed to be executed through the command-line| High | Docker | |`## Installing through Docker` | |
| Binary-based| Github source and binary releases (binary dependencies) | Low | - | download the tarball, unpack it, and run it (ready-to-run)  | 3 | |




**Method 1: Source-based installation**
Goal: provide the source code to enable the ability to review the source code and understand its workings
Development setup sometimes it is called
compile from source
Running in command line mode
Deal with source code dependencies
You need to build the source code yourself. That means you need to take care of the dependencies yourself. 
A source file contains the original code as written by the developer in whatever language he/she chooses (C, C++, Python etc),and is generic
Installing a program "from source" means installing a program without using a package manager. You compile the source code and copy the binaries to your computer instead

**Method 2: Package manager-based installation**
Pre-built package
A package (RPM or DEB for example) is the binary executable (or interpreted script etc) pre-prepared for your particular distro. The task of preparing the source for compiling (adding any necessary patches etc), the actual compile, creating distro specific config files, creating pre and post install scripts etc are all done for you by the package maintainer.

| Name | Channel | Steps | Commands |
| ----- | ----------------- | ---------------------- | --- |
| Conda| bioconda | 1 |  ```conda install bioconda::sambamba``` or ```conda install bioconda/label/cf201901::sambamba``` |
| GNU Guix| | 1 | ```guix install sambamba``` or | ```guix install sambamba``` |
| Homebrew| homebrew-bio | 1  | ```brew install brewsci/bio/sambamba``` |
| Fedora| dnf | 1  | ```dnf install package``` |
| Debian| apt | 1 | ```apt install package``` |
|Pypi| | pip | ```pypi install package``` |

**Method 3: Container-based installation**


**Method 4: Binary-based installation**
precompiled binaries are ready-to-run executable files
Deal with binary dependencies
Running AML in user interface mode


example:[https://www.qemu.org/download/](https://www.qemu.org/download/)

To download and build binaries

```wget https://download.example.org/example.tar.xz```

```tar xcJf example.tar.xz```

```cd example```

```./configure```

```make```

To download and build binaries from **git**

```git clone https://github.com/example.git```

```cd example```

```git submodule init```

```git submodule update --recursive```

```./configure```

```make```




### Translating abstract to executable instructions

Create a method to connect human-readable language instructions to actions and collection of actions in software installation domain (manchine learning a planning domain). We limit ourselves to tasks that can be characterized as "software manipulation” and involve picking up, putting down and handling objects at different places. Examples of such tasks are setting a table, cleaning up, making toast or cooking tea. To the best of our knowledge this work is the first to mine complex task descriptions from the readmes and translate them into executable agent plans.


We will present the different steps from the instruction in natural language to an executable plan with the example sentence **"Place the cup on the table"** **Install package from source**.


#### 1. structure of instructions is identified

Let `concepts(w)` be the set of ontological concepts to which the word `w` could be mapped. For a `single instruction (ai, oi, pi)` consisting of an `action verb ai`, an `object oi` and a set of `prepositions`


**GOAL**= Capture a collection of **`Step(s)`** within a **`Plan`** for acomplishing software installation **`Task(s)`**

**Ontological `concepts`**

**`Plan`**: a sequence/collection of instatiated **Step(s)** that a machine execute one **Action** among many alternatives to fulfil its objective in installation. A installation method (similar to procedure) is an instance of the `Plan` **Task(s)**. *e.g. Method 2: Install package from source*

**`Step(s)`**: a list of sequencial Action(s) part of a `Plan` to be executed by a machine *e.g. Clone the repository from source `git clone repository`, `second` create virtual environment*

**`Action(s)`**: a list of indivisible sequence of operations that must executed without interruption. Each `Action` is an instance of the `Step` concept *e.g.`git clone repository`*

**`Task(s)`**: a list of computationally actions steps in software installation domain. *e.g Method 1: From source* *(TBC)*

Possibility to define **`SubPlans`** *e.g. alternative methods for installing software* within the Plan (similar to procedure)



#### 2. Resolve the meaning of the words using Cyc Ontology and or P-plan

**Formal Instruction Representation**

Each step action1, action2, etc is an instance of an action concept like *CloneTheRepository*. The action *CloneTheRepository* needs to have information about the object to be manipulated and the location where this object is to be placed. For execution, the formal instruction representation has to be transformed into a valid machine-readable plan. The plans for a machine are implemented in P-PLAN, which provdes an expressive and extensible ontology representation for semantically writing plans to machines.

```ttl
@prefix p-plan: <http://purl.org/net/p-plan#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

_:b0 a p-plan:Plan ;
    rdfs:label "Installing a software open source tool using containerization" ;
    p-plan:isStepOfPlan _:b1, _:b2, _:b3, _:b4, _:b5, _:b6 .

_:b1 a p-plan:Step ;
    rdfs:label "Prerequisites" ;
    rdfs:comment "Ensure you have Docker installed on your system. If not, download and install Docker from its official website." .

_:b2 a p-plan:Step ;
    rdfs:label "Pull the Docker Image" ;
    rdfs:comment "Locate the section in the README that specifies the Docker image for the software tool. Use the `docker pull` command to download the image from the Docker Hub or another container registry." ;
    p-plan:correspondsToStep _:b7 .

_:b7 a p-plan:Step ;
    rdfs:label "docker pull <image_name>:<tag>" ;
    rdf:type "Bash" .

_:b3 a p-plan:Step ;
    rdfs:label "Run the Container" ;
    rdfs:comment "After pulling the image, use the `docker run` command to create and start a container from the image. This step often includes mounting volumes for data persistence and specifying ports if the software requires network access." ;
    p-plan:correspondsToStep _:b8 .

_:b8 a p-plan:Step ;
    rdfs:label "docker run -d -p <host_port>:<container_port> -v <host_directory>:<container_directory> <image_name>:<tag>" ;
    rdf:type "Bash" .

_:b4 a p-plan:Step ;
    rdfs:label "Access the Software" ;
    rdfs:comment "Depending on the software, you might access it through a web interface, command line, or API. The README should provide details on how to interact with the software once it's running in the Docker container." .

_:b5 a p-plan:Step ;
    rdfs:label "Custom Configuration" ;
    rdfs:comment "Some tools may require additional configuration steps, such as setting environment variables or editing configuration files. These steps should also be detailed in the README section for containerization." .

_:b6 a p-plan:Step ;
    rdfs:label "Stopping and Removing the Container" ;
    rdfs:comment "When you're done using the software, you can stop the container using `docker stop <container_id>` and remove it with `docker rm <container_id>`. Replace `<container_id>` with the ID of your container." ;
    p-plan:correspondsToStep _:b9, _:b10 .

_:b9 a p-plan:Step ;
    rdfs:label "docker stop <container_id>" ;
    rdf:type "Bash" .

_:b10 a p-plan:Step ;
    rdfs:label "docker rm <container_id>" ;
    rdf:type "Bash" .
```

Task Info:
```json
['task_id'] = "trial_00000_T000000000000000"        (unique instruction ID)
['task_type'] = "pick_heat_then_place_in_recep"     (one of 7 task types)
['plan_params'] = {'object_target': "AlarmClock",   (object)
                   'parent_target': "DeskLamp",     (receptacle)
                   'mrecep_target': "",             (movable receptacle)
                   "toggle_target": "",             (toggle object)
                   "object_sliced": false}          (should the object be sliced?)

```

Language Annotations:
```json
['turk_annotations']['anns'] =  
             [{'task_desc': "Examine a clock using the light of a lamp.",                 (goal instruction) 
               'high_descs': ["Turn to the left and move forward to the window ledge.",   (list of step-by-step instructions)
                              "Pick up the alarm clock on the table", ...],               (indexes aligned with high_idx)
               'votes': [1, 1, 1]                                                         (AMTurk languauge quality votes)
              },
              ...]
```

Expert Demonstration:

```json
['plan'] = {'high_pddl':
                ...,
                ["high_idx": 4,                          (high-level subgoal index)
                 "discrete_action":                    
                     {"action": "PutObject",             (discrete high-level action)
                      "args": ["bread", "microwave"],    (discrete params)
                 "planner_action": <PDDL_ACTION> ],      (PDDL action)
                ...],
                 
            'low_actions': 
                ...,
                ["high_idx": 1,                          (high-level subgoal index)
                 "discrete_action":
                     {"action": "PickupObject",          (discrete low-level action)
                      "args": 
                          {"bbox": [180, 346, 332, 421]} (bounding box for interact action)
                           "mask": [0, 0, ... 1, 1]},    (compressed pixel mask for interact action)
                 "api_action": <API_CMD> ],              (THOR API command for replay)
                ...], 
           }
```