---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Introduction

Each football data provider uses its own unique format to describe the sequence of a game.
Therefore, the software written to analyze this data must be suitable for a specific provider and cannot be used without modifications to analyze the data of other providers.

Kloppy is a Python package that addresses the challenges posed by the variety of data formats and aims to be the fundamental building block for processing soccer tracking and event data. 

How can kloppy deal with all these providers and generate the same result for each one? and which providers can support?

Before delving into the details we will identify the problematic .The Company is delivered with football data from different providers, In our case, we will point to the Instat provider. We simply want to adapt Instat to the Kloppy package to be able to use its many features.
