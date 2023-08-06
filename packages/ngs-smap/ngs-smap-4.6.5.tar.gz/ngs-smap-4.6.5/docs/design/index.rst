.. SMAP documentation master file, created by
   sphinx-quickstart on Wed Aug  5 13:28:17 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _SMAPdesignindex:

SMAP design
===========

| This is the manual for the component **SMAP design** of the SMAP package.
| **SMAP design** was created specifically to design primers for amplicon sequencing, in combination with gRNA design from third-party software such as `CRISPOR <http://crispor.tefor.net/>`_ or `FlashFry <https://github.com/mckennalab/FlashFry>`_.
| **SMAP design** takes one or more reference sequences (FASTA and GFF) as input and designs non-overlapping amplicons per reference taking target specificity into account.
| **SMAP design** can be combined with gRNA sequences for CRISPR/Cas targetted mutagenesis of the reference sequences. As such, **SMAP design** overlaps these amplicons and gRNAs, and selects *n* (user-defined) non-overlapping amplicons with gRNAs according to several criteria such as number of gRNAs covered by the amplicon, specificity and efficiency scores.
| **SMAP design** creates a primer file, gRNA file, GFF file with all structural features, and optionally a summary file and plot, and input files required for downstream analyses using :ref:`SMAP haplotype-sites <SMAPhaploindex>` or :ref:`SMAP haplotype-window <SMAPwindowindex>` and :ref:`SMAP effect-prediction <SMAPeffectindex>`.
| A clear illustration of the implementation and use of **SMAP design** is described in detail in `Develtere et al. (2022) <https://www.biorxiv.org/content/10.1101/2022.07.21.500617v1>`_.
| For more information on optimal coverage of the combinatorial design space of multiplex CRISPR/Cas experiments, please see `Van Huffel et al. (2022) <https://www.frontiersin.org/articles/10.3389/fpls.2022.907095/abstract>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   design_scope_usage
   design_feature_description
   design_HIW
   design_examples

