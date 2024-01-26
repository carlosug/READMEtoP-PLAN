# Benchmark for installation instructions of software repositories
---
This folder aims to keep track of the experiements related to the research question:

* can machines interpret and execute installation plans for biomedical software?

### Selection criteria [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) :
The repositories will be selected on community-curated list of software packages:
+ bioinformatics software documentation ([e.g](https://blog.bioconductor.org/posts/2022-10-22-awesome-lists/)) and/or [bio.tools](https://bio.tools/t?page=1&q=%27Python%27&topic=%27Neurobiology%27&sort=score);
+ part of [awesome-healthcare list](https://github.com/kakoni/awesome-healthcare) or;
+ part of [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools);
+ part of [awesome-neuroscience](https://github.com/analyticalmonk/awesome-neuroscience);
+ part of [biological image analysis](https://github.com/hallvaaw/awesome-biological-image-analysis)

Also thinking about LLMs for bioinformatics

### Available software repositories
A list of research software registries (also known as catalog, index, warehouse, repository, hub, platform, and other terms) can be found here: [Awesome Research Software Registries](https://github.com/NLeSC/awesome-research-software-registries) 

* [Research software directory]()
* [4TUResearchData repository]()
* [TUD]()
* [Research Software Heritage]()
* [Marven Central Repository]()
* [Apache projects](https://projects.apache.org/)
* [ORKG](https://orkg.org)
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

**Altenrate methods of installation**: mostly devided in ```fromClient```, ```fromSource```, and ```fromContainer```


### Software type

| Type | Description |
| ----- | ----------------- |
| Library| A collection of components that are used to construct other tools|
| Script| A tool written for some run-time environment| 
| Package| A tool that is aimed to be executed through the command-line|
| Service| A collection of codes that do not fit any of the previous categories |

### Taxonomy of research software installation types
The type of software installation: a discrete software entity can have more than one e.g. command-line, services

| Mode | Description | Complexity | Method | Steps | number of steps |
| ----- | ----------------- | ---------------------- | -------------------- |
| Source| A collection of components that are used to construct other tools| High | Git | | |
| Package Manager| A tool written for some run-time environment| Low | Pip | | |
| Container| A tool that is aimed to be executed through the command-line| High | Docker | | |
| Binary| Github source and binary releases | Low | Downdload | download the tarball, unpack it, and run it | 3 |

#### Package managers



