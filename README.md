<h1 align="center">
  AutoTarget: A Disease-Associated Drug Target Recommendation System Using Graph Theory and Machine Learning
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
* [Contact](#Contact)

## General Info
Target discovery, the first stage of early drug discovery, is a time-consuming and crucial process. This is because it is difficult to achieve appropriate efficacy when a drug candidate acts on an inapposite target. For that reason, pharmaceutical companies invest a lot of time and money to find the right target from the beginning. We present AutoTarget, a disease-associated drug target recommendation system using graph theory and machine learning. AutoTarget predicts the structurally equivalent nodes of drug targets on the market, based on the assumption that potential drug targets have similar local structural patterns in protein networks. As a result, researchers can use AutoTarget to check a list of novel drug targets associated with a specific disease.

![image](https://user-images.githubusercontent.com/65825773/216899986-8096cca8-0bd9-40ab-955d-4898c2864767.png)

The above figure shows two pathways with similar network structures in the protein-protein network (PPI). B and D are structurally equivalent nodes in the two pathways that lead to different reactions. Both nodes are at the end of each pathway, which leads directly to each phenomenon. If the flow of the two pathways is similar and protein B is a drug target, protein D can also be considered as a potential drug target.


## Installation
```bash
$ pip install AutoTarget
```

## Web Interface
AutoTarget provides web-based access. Through the web interface, researchers can use all functions of the AutoTarget library in a GUI. The web interface was programmed through Streamlit. The web interface version can be accessed via https://gumgo91.github.io/apps/autotarget .

## Contact
If you have any questions or suggestions, please contact us at hskong@snu.ac.kr.
