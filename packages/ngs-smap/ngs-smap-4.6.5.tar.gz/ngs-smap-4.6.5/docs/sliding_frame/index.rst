.. SMAP documentation master file, created by
   sphinx-quickstart on Wed Aug  5 13:28:17 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _SMAP_slidingframe_index:

SMAP sliding frame
==================

| This is the manual for the complementary **SMAP utility** tool **SMAP sliding-frames** of the SMAP package.
| The first step prior to running **SMAP haplotype-sites** is the definition of the locus start and end points.
| The python script **SMAP_sliding-frame.py** should be used to define sliding frames covering SNPs and/or structural variants in Shotgun data (currently provided as Python3 script in the **SMAP utility** tools).

.. image:: ../images/sliding_frames/SMAP_utilities_Sliding_frame_scope_Shotgun.png

| The module **SMAP** :ref:`delineate <SMAPdelindex>` should be run for GBS data to define relevant loci and read mapping polymorphisms in a data-driven manner.
| A module called **SMAP design** will be launched in the near future for integrated design of HiPlex PCR primers and downstream analysis with **SMAP** :ref:`haplotype-sites <SMAPhaploHiPlexHIW>` and/or **SMAP** :ref:`haplotype-window <SMAPwindowcommands>`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   slidingframe_scope_usage
   slidingframe_feature_description
   slidingframe_HIW
   slidingframe_examples
   slidingframe_faq