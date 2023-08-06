.. SMAP documentation master file, created by
   sphinx-quickstart on Wed Aug  5 13:28:17 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _SMAP_target_selection_index:

SMAP target-selection
=====================

| This is the manual for the SMAP utility tool **SMAP target-selection** of the SMAP package.  
| **SMAP target-selection** was designed to easily select groups of genes and create subsets of reference sequences as input for **SMAP design** and further downstream analysis with *e.g.* **SMAP haplotype-sites**, **SMAP haplotype-window** or **SMAP effect-prediction**.
| **SMAP target-selection** extracts FASTA sequences from a reference genome sequence, using a short list of gene identifiers and/or grouping information, places candidate genes with the CDS encoded on the positive strand in the extracted reference sequence FASTA, and re-positions GFF features according to the novel coordinates, and may extract flanking regions of a user-defined length.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   target_selection_scope_usage
   target_selection_feature_description
   target_selection_HIW
   target_selection_examples
   target_selection_faq

