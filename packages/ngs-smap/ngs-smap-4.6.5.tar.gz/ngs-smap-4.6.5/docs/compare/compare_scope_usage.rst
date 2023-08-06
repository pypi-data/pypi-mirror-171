.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

.. raw:: html

    <style> .green {color:green} </style>
    <style> .blue {color:blue} </style>
    <style> .red {color:red} </style>

.. role:: green
.. role:: blue
.. role:: red

#############
Scope & Usage
#############

Scope
-----

:purple:`Comparisons across data sets, shared and unique loci`

**SMAP compare** analyzes the overlap (shared and unique loci) between two GBA data sets that have both been processed with :ref:`SMAP delineate <SMAPdelindex>`.
**SMAP compare** can be used to compare:

	1.	parameter settings during read `preprocessing <https://gbprocess.readthedocs.io/en/latest/gbs_data_processing.html>`_. 
	#.  parameter settings during read mapping (e.g. `BWA-MEM <http://bio-bwa.sourceforge.net/bwa.shtml>`_).
	#.  parameter settings during locus delineation (:ref:`SMAP delineate <SMAPdelindex>`).
	#.	sets of progeny derived from independent breeding lines to estimate transferability of marker sets across a breeding program.
	#.	a set of pools against their constituent individuals to estimate sensitivity of detection across the allele frequency spectrum (example shown below).
	#.	GBS experiments performed in different labs, to investigate if similar protocols lead to similar sets of loci, *i.e.* comparability of own data to external data.
	

----

Integration in the SMAP workflow
--------------------------------

.. image:: ../images/compare/SMAP_global_scheme_home_compare.png

**SMAP compare** is run on BED files with locus positions, directly after **SMAP delineate**, **SMAP sliding-frames** or **SMAP design**, and before the BED files are used for **SMAP haplotype-sites**.  
**SMAP compare** works on GBS, HiPlex and Shotgun sequencing data.

Commands & options
------------------

::

	smap compare <Set1.bed> <Set2.bed> 
