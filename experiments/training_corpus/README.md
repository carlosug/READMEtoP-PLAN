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

**Altenrate methods of installation**: mostly devided in ```fromClient```, ```fromSource```, and ```fromContainer```


### Software type

| Type | Description |
| ----- | ----------------- |
| Library| A collection of components that are used to construct other tools|
| Script| A tool written for some run-time environment| 
| Package| A tool that is aimed to be executed through the command-line|
| Service| A collection of codes that do not fit any of the previous categories |

### Taxonomy of research software installation types
The type of software installation: a discrete software entity can have more than one level of complexity e.g. command-line, services

| Mode | Description | Complexity | Method(s) | Steps | number of steps | README section |
| ----- | ----------------- | ---------------------- | -------------------- | ------- | -------- | -- |
| Source| Raw material (source) with a compiler to download the executable that machines then runs| High | Git and official release websites | Download the compiler and install all the required libraries manually  | | `## Manual install` , `## from source`, `## Install from Github`|
| Package Manager| A tool written for some run-time environment| Low | Pip |1 |`## Install from Pypi` | |
| Container| A tool that is aimed to be executed through the command-line| High | Docker | |`## Installing through Docker` | |
| Binary| Github source and binary releases (binary dependencies) | Low | - | download the tarball, unpack it, and run it (ready-to-run)  | 3 | |

**Method 1: from Source**
Goal: provide the source code to enable the ability to review the source code and understand its workings
Development setup sometimes it is called
compile from source
Running in command line mode
Deal with source code dependencies
You need to build the source code yourself. That means you need to take care of the dependencies yourself. 
A source file contains the original code as written by the developer in whatever language he/she chooses (C, C++, Python etc),and is generic
Installing a program "from source" means installing a program without using a package manager. You compile the source code and copy the binaries to your computer instead

**Method 2: from Package managers**
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

**Method 3: from Container**

**Method 4: Binary**
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



