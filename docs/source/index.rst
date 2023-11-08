Welcome to STEGO.R's documentation!
===================================

**STEGO.R** is an R shiny application

Check out the :doc:`1.installation` for how to install the project
- :ref:`Installation`


.. note::

   This project is under active development.

Contents
--------

.. toctree::

   Installation
   QualityControl
   Analysis
   FAQ
   History

   usage
   api

# Welcome to STEGO's documentation!

STEGO is an R Shiny application to aid in scRNA-seq with scTCR-seq.

!!! note

This project is under active development.
##### Overview - [installation](1.installation) - [QC](2.QualityControl)

STEP 1 Formatting the 10x Genomics, BD Rhapsody or Array for the Seruat, ClusTCR2, TCRex and TC
STEP 2 Clustering with ClusTCR2 and if needed, merging multiple TCRex files.
STEP 3 Quality control of one Seurat object and adding the TCR pairing information.
STEP 4 Merging multiple Seurat objects
STEP 5 Annotating the Seurat object
10X Genomics for human
10X Genomcis for Mouse
BD rhapsody for Human immune panel
BD Rhapsody for Mouse data
Performing the [analysis](3.Analysis)
Overview
GEx
TCR-seq
Differential expression
GEx + TCR-seq
Prioritization strategy (under active development)
Top clonotype
Expanded clones
Epitope
ClusTCR2
[Frequently asked question](4.FAQ)
[Version History](5.History)
citing STEGO.

STEGO pre-print
Seurat
scGate (if annotations were used)
If clustering with ClusTCR2, please cite the original paper.


Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.
