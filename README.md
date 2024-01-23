# READMEtoP-PLAN
We present a method called READMEtoPLAN, which takes as input a the *installation instructions* and outputs a corresponding P-PLAN ontology model.

## Expected contributions
Support researchers reusing software artefacts by adding discoverability, traceability and reproducibility functionalities in 4TUResearchData using semantic technology approaches:

* 1. Add descriptors on the existing RDF data model (annotate with [GUIX Package standards](https://guix.gnu.org/manual/en/html_node/Defining-Packages.html))
* 2. A framework to generate the dataset in RDF.
* 3. Raw data files from the dataset generation that can be reused for further researcher


## Ontology
Extending [P-PLAN](https://lov.linkeddata.es/dataset/lov/vocabs/p-plan) is the most suitable solution for representing installation plans (the steps, plans, input and output variables and their relationship with each other):

* P-PLAN URI: [http://purl.org/net/p-plan#](http://purl.org/net/p-plan#)
* P-PLAN homepage: [http://www.opmw.org/model/p-plan/](http://www.opmw.org/model/p-plan/)

Other available vocabularies and data models:
* [Codemeta terms](https://codemeta.github.io/terms/)
* [REPRODUCE-ME](https://github.com/Sheeba-Samuel/REPRODUCE-ME/tree/master)
* [Planning domain definition lamguage](https://github.com/AI-Planning/pddl)
* [https://schema.org/InstallAction](https://schema.org/InstallAction)
* [GUIX Package standards](https://guix.gnu.org/manual/en/html_node/Defining-Packages.html)


We define the following labels:
*Installation instructions*: A set of instructions that indicate how to install a target repository
*Invocation*: Execution command(s) needed to run a scientific software component

## Annotated dataset
A gold-standard dataset of software installation in research is needed. A manually annotated corpus will be generated with the following labels:

We will be using one of the following tools (possibly following [The Softcite approach](https://github.com/howisonlab/softcite-dataset#the-softcite-approach)):
- [Prodigy](https://prodi.gy/)
- [hypothes.is](https://web.hypothes.is/)


