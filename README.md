# CLAP: Learning Transferable Binary Code Representations with Natural Language Supervision

This repository contains materials for the paper "CLAP: Learning Transferable Binary Code Representations with Natural Language Supervision", submitted for review. In this document, we provide an overview of the contents of this repository and instructions for accessing the materials.

## Contents

1. **CaseStudy.ipynb**: A Jupyter Notebook showcasing the zero-shot performance of our proposed model using a case study. Please open this file to get an in-depth view of how our model works and the results it produces. This file also contains 
the SHA-256 hash of the model we used to produce the results in the paper. This hash can be used to verify the integrity and reproducibility of our model. The hash is also provided in the Model_SHA256.txt file.

2. **CaseStudy**: A folder containing IDB files and rebased assembly code for the case study used in the Jupyter Notebook. These files are used to generate the results in the Jupyter Notebook. We provide three different senarios for the case study,
including a bubble sort program, SHA-3 crypto algorithms and a real-world malware sample (which can be found at [virustotal](https://www.virustotal.com/gui/file/cd677242197cdc89d7b8e2e3056030fe2bb9b384c95a7a027a7eee8182b8426f/)). We conduct three zero-shot (without any further training) case studies, the results are shown in the Jupyter Notebook.

3. **Prompts**: A folder containing prompts for explaining source code and zero-shot evaluation in crypto identification task and protocol categorization.

3. **HumanEvaluationExamples**: A folder containing screenshots of human evaluations procedure performed while evaluating our data engine. These examples serve as supplementary evidence to support the claims made in the paper.

4. **Model_SHA256.txt**: A text file containing the SHA256 hash of our model to ensure reproducibility.

## Instructions

To access the materials, please follow these steps:

1. You can view these materials with your brower. Just open the CaseStudy.ipynb file to view the case study and the performance of our model. And you can browse the **HumanEvaluationExamples** folder to view the screenshots of human evaluations performed during the assessment of our shadow models. 

2. Download or clone this repository to your local machine.

   1. Ensure you have a recent version of Jupyter Notebook installed on your system. Or you can use VSCode to open the Jupyter Notebook file.

   2. Open the CaseStudy.ipynb file with Jupyter Notebook to view the case study and the performance of our model.
   
   3. We provide IDB files and rebased assembly code for the case study in the **CaseStudy** folder. You can use IDA Pro to open the IDB files and view the assembly code. Or you can view the rebased assembly code in any text editor.

Thank you for your interest in our work, and we hope these materials help you better understand our research and findings.
