# 🕵️‍♀️ When the Model Imagines It All: Crime Resolution with LLMs 📚
---
This repository contains the code and resources supporting the research presented in "Cuando el Modelo se lo Imagina Todo: Resolución de Crímenes con LLMs" 🔍. This study investigates the impact of automated context enrichment on the performance of Large Language Models (LLMs) in question-answering tasks involving crime narratives .[Spanish](./README.md)

## Project Summary 📝

This research addresses the limitations of LLMs in accurately answering questions about narratives with insufficient context. We propose an automated system to enrich narrative texts and provide evidence that this enrichment improves LLM performance in question-answering tasks.

## Methodology ⚙️

To evaluate the impact of context enrichment:

1.  We utilized the **Murder Mysteries dataset** 📖, a structured collection of crime narratives designed for question-answering.
2.  We developed an automated system to generate enriched versions of these narratives. This system employs a three-stage process:
    * **Question Generation** ❓: Generating inferential questions relevant to the narrative.
    * **Answer Generation** ✍️: Producing narrative answers to the generated questions.
    * **Content Fusion** 🧩: Integrating the generated answers into the original narratives.
3.  We evaluated the performance of the LLAMA 3.3 70B model 🧠 on both the original and enriched narratives.

## Repository Contents 📁

This repository provides the following:

* Code implementation of the automated context enrichment system 💻.
* Scripts for dataset processing and evaluation 📊.
* Documentation detailing the experimental setup 🔬.

## Results 📈

The study's findings indicate that the automated context enrichment process improves LLM accuracy in question-answering tasks. The LLAMA 3.3 70B model demonstrated a notable increase in accuracy when evaluated on the enriched narratives compared to the original narratives.

## Implications 💡

This research highlights the potential of automated context enrichment to enhance LLM performance in narrative understanding. The proposed methodology offers a valuable approach for improving LLM capabilities without requiring additional training or human intervention.

## Contact 📧

For inquiries, please contact:

Javier Fontes Basabe

JAVIERFONTBAS@GMAIL.COM