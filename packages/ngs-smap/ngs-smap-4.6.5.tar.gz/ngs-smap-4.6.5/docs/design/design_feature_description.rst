.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

###################
Feature Description
###################

.. _SMAPdesigndef:

Definition of reference gene, CDS, amplicons, gRNA, and overlaps
------------------------------------------------------------------

| **SMAP design** designs amplicons to resequence specific parts of the genome, possibly in combination with gRNA design for CRISPR/Cas genome editing.

| **SMAP design** first creates **amplicons** by designing pairs of primers within a given length range. Specificity of primer binding is embedded in the Primer3 algorithm and tested against all other sequences in the same run of primer design. The primer binding site locations of such **amplicons** are also used during the downstream analysis pipelines of **SMAP haplotype-sites** or **SMAP haplotype-window**, so that the entire workflow from design to analysis is integrated.  
| **SMAP haplotype-sites** creates haplotypes based on neighboring SNPs at loci delineated by (:ref:`SMAPs <SMAPdeldef>`), in which the SMAPs are located at the nucleotides immediately internal to the primers.  
| **SMAP haplotype-window** creates haplotypes based on the entire DNA sequence at loci delineated by borders, in which borders are defined as the 8 to 10 nucleotides on the 3' end of the primers.
| See schemes below for graphical illustration of the concepts.  
| Amplicons are then positionally overlapped with predefined gRNAs (designed by third-party software such as `CRISPOR <http://crispor.tefor.net/>`_ or `FlashFry <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6033233/>`_), to allow targetted resequencing of potential genome editing sites.

| **Schematic overview of reference gene, CDS, amplicons, guides, and overlaps.**

.. image:: ../images/design/Design_overview_scope_sites_window.png

----

.. _SMAPdesignrules:

Design rules
------------

* Robust, reliable primers should be designed that are mutually compatible in HiPlex assays.
* Primers should be specific to the target loci, and off-target primer binding should be avoided to ensure specific assignments of detected alleles to target loci.
* Multiple, non-overlapping amplicons may be designed to increase coverage of the targeted genome regions.
* Overlapping amplicons should be split in independent HiPlex assays, that together increase coverage of the target genome regions (see panel Natural variation above).
* Multiple gRNAs may be designed per target gene, to increase the chance of obtaining a mutation that effectively disrupts the gene function.
* Per gRNA, two flanking primers are designed to amplify the regions containing the anticipated CRISPR/Cas-induced mutation. 
* One amplicon may cover multiple gRNAs. 
* Multiple amplicons may be required to cover all potential gRNAs, but amplicons should be non-overlapping per HiPlex primer assay.
* Amplicon design parameters such as amplicon length depend on the downstream sequencing method (*e.g.* Sanger sequencing 400-800 bp; short-read Illumina 80-150 bp; long-read NGS 500-2000 bp).
* Amplicon design parameters such as distance between gRNA and primer binding site depend on the downstream sequencing method (*e.g.* Sanger sequencing minimal 150 bp; short-read Illumina minimal 15 bp; long-read NGS minimal 50 bp).

----

Avoiding polymorphic sites (*e.g.* SNPs) during amplicon design
---------------------------------------------------------------

| It is possible to avoid primer design in locations with known polymorphisms by coding SNP sites as "N" in the reference sequence before running **SMAP design**.
| Scripts to substitute nucleotides in the reference sequence using a list of SNP positions are under development.
