.. SMAP documentation master file, created by
   sphinx-quickstart on Wed Aug  5 13:28:17 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. _SMAPsnpseqindex:

SMAP snp-seq
============

| This is the manual for the component **SMAP snp-seq** of the SMAP package.  
| **SMAP snp-seq** was designed specifically to design HiPlex amplicon primers for targeted resequencing of polymorphic loci, while accounting for neighboring SNPs during primer design.  
| **SMAP snp-seq** requires a reference genome sequence, a VCF file with all known SNPs, a list of SNPs that should be targetted by amplicon sequencing.
| **SMAP snp-seq** creates a list of primer sequences, a GFF file with primer sequence coordinates, a BED file with SMAPs for downstream analysis with **SMAP haplotype-sites** or a GFF file with border coordinates for downstream analysis with **SMAP haplotype-window**.  


| Detailed information on these features can be found in the section :ref:`Feature Description <SMAPdeldef>`.



.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   snp-seq_scope_usage
   snp-seq_feature_description
   snp-seq_HIW
   snp-seq_examples
   snp-seq_faq

