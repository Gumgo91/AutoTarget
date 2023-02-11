<h1 align="center">
  AutoTarget: A Disease-Associated Drug Target Recommendation System using Node Classification with Neighborhood Context in PPI Networks
  <br/>
    <a href="https://pypi.org/project/autotarget/">
        <img src="https://img.shields.io/badge/pypi-1.0.0.0-green" alt="AutoTarget on PyPI">
    </a>
    <a href="">
        <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT">
    </a>
</h1>

## Table of Contents

* [General Info](#general-info)
* [Installation](#installation)
* [Web Interface](#Web-Interface)
* [Contact](#Contact)

## General Info
Target discovery, the initial stage of early drug development, is a critical and resource-intensive process. This is because an improper target selection can result in ineffective drug efficacy. As a result, pharmaceutical companies invest considerable time and resources to find the appropriate target at the outset. To address this challenge, we introduce AutoTarget, a disease-associated drug target recommendation system that uses node classification and neighborhood context in protein-protein interaction networks. AutoTarget predicts drug targets that are structurally equivalent to existing drugs on the market by leveraging the premise that potential drug targets exhibit similar local structural and neighborhood context within PPI networks. With AutoTarget, researchers can quickly and easily obtain a list of novel drug targets related to a specific disease, streamlining their drug discovery process.

![image](https://user-images.githubusercontent.com/65825773/218240443-4cca0afe-7e75-4e49-b3a9-01075fc55b5a.png)


The above figure illustrates the process of embedding through the utilization of neighborhood context and structural equivalence between nodes. The node marked as α, depicted in black, serves as the central node, while the remaining nodes depicted in white, represent the neighborhood nodes. The vector representation of α can be derived based on the contextual information of its neighboring nodes at various depths. In this study, each node is represented as a 128-dimensional vector. β and γ are both connected to a single node at depth 1 and to two nodes at depth 2, with the directions of their edges being consistent. β and γ display similar connectivity patterns, and as a result, possess structural equivalence. If the protein β is associated with disease 1 and serves as a drug target, and the protein γ is linked to disease 2, this indicates that γ could serve as a novel potential drug target for disease 2. Furthermore, if a neighborhood context δ, similar to β, is identified in a pathway where the target for drug discovery is currently unknown, then δ can also be considered as a potential target. 

## Installation
```bash
$ pip install AutoTarget
```

## Web Interface
In addition to the Python library, AutoTarget also offers web-based access, enabling researchers to utilize all functions of the AutoTarget library through a graphical user interface (GUI). The web interface has been developed using Streamlit, and can be accessed through the following URL: https://gumgo91.github.io/apps/autotarget. This provides researchers with a convenient and user-friendly way to access the capabilities of the AutoTarget pipeline, without the need for any prior programming knowledge.

## Contact
If you have any questions or suggestions, please contact us at hskong@snu.ac.kr.
