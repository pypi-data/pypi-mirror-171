.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

.. _SMAPsnpseqHIW:

############
How It Works
############

| Several applications of molecular markers iterate between marker discovery (*e.g.* GBS) and targeted screening by HiPlex amplicon sequencing (*i.e.* SNP-seq).
| This module of SMAP fill the gap inbetween those strategies: it takes SNP variants identified in a large screen, and allows to automatically design primers flanking selected SNPs or within selected regions, in both cases avoiding all known SNPs at primer binding sites.
| To do so, several input files are optionally provided to define the SNPs and/or regions to be targeted, and the SNPs to avoid during primer design.
| SMAP snp-seq also generates the coordinate files: a BED file with SMAPs for downstream analysis with SMAP haplotype-sites, or a GFF file with border positions for SMAP haplotype-window. 
| In addition, several parameters can be set to define distances between SNPs and/or loci.
| In principle, it is possible to *a priori* define regions to be targeted (such as 1 kb regions at 1 Mb intervals) to design a HiPlex set that covers the entire genome at a fixed marker distance.

----

Defining regions according to different scenario's
--------------------------------------------------

:purple:`Schematic overview of design steps`

.. image:: ../images/snp-seq/utilities_HIW_SNP_step1.png
.. image:: ../images/snp-seq/utilities_HIW_SNP_step2.png
.. image:: ../images/snp-seq/utilities_HIW_SNP_step3.png
.. image:: ../images/snp-seq/utilities_HIW_SNP_step4.png
