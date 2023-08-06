.. raw:: html

    <style> .purple {color:purple} </style>
	
.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

#############
Scope & Usage
#############

Scope
-----

In Shotgun sequencing, haplotypes are defined by a set of SNPs in a dynamic sliding frame. Start and end positions of sliding frames (called Anchor points) are typically defined as the first and last SNP of a string of neighboring SNPs across a given distance.  
A special case is the detection of the junctions of large-scale inversions or deletions, in which the read mapping breakpoint is taken as variable position flanked by two Anchor points: the nucleotides immediately upstream and downstream. See schemes below for graphical illustration of the two concepts and :ref:`Feature Description <SMAP_sliding_frame_def>` for further details.

.. image:: ../images/sliding_frames/utilities_HIW_SNP_step2.png

----

Integration in the SMAP workflow
--------------------------------

.. image:: ../images/sliding_frames/SMAP_global_scheme_home_sliding_frames.png

**SMAP sliding-frames** is run on a VCF file with variant positions and a reference genome FASTA file to delineate loci, before **SMAP haplotype-sites** or **SMAP haplotype-window**.  
**SMAP sliding-frames** works on Shotgun sequencing data.

Commands & options
------------------

.. _SMAP_utilities_quickstartcommands:

:purple:`Haplotyping sliding frames with adjacent SNPs`

The Python script in the SMAP utility tools directory transforms a simple VCF-formatted list of SNPs into a BED file with sliding frames for **SMAP haplotype-sites**.

::

	python3 SMAP_sliding-frames.py --bed reference_genome_Lp.bed --vcf 503TargetGenes_391Genotypes_SNPs.vcf --frame_length 10 --frame_distance 0 --offset 0 -s Set_FL10_FD0_OS0

The same VCF file is then used as input for the variant sites in **SMAP haplotype-sites**
Command examples and options of **SMAP haplotype-sites** for a range of specific sample types are given under :ref:`haplotype frequency profiles <SMAPhaplofreq>`.  

::

	smap haplotype-sites /path/to/BAM/ /path/to/BED/ /path/to/VCF/ -mapping_orientation ignore --no_indels -c 30 -f 5 -p 8 --plot_type png -partial exclude --min_distinct_haplotypes 1 -o haplotypes_FL10_FD0_OS0 --plot all --discrete_calls dosage -i diploid -z 2 --locus_correctness 80


:purple:`Haplotyping the junction sites of large structural variants such as deletions and inversions`

The Python script in the SMAP utility tools directory transforms a simple VCF-formatted list of breakpoints into a BED file for SMAP haplotype-sites with the following settings:

::

	python3 SMAP_sliding-frames.py --bed reference_genome_Os.bed --vcf StructuralVar_272Genotypes_Dels.vcf --frame_length 3 --frame_distance 0 --offset 1 -s Set_FL3_FD0_OS1

The same VCF file is then used as input for the variant sites in **SMAP haplotype-sites**
Command examples and options of **SMAP haplotype-sites** for a range of specific sample types are given under :ref:`haplotype frequency profiles <SMAPhaplofreq>`.

::

	smap haplotype-sites /path/to/BAM/ /path/to/BED/ /path/to/VCF/ -mapping_orientation ignore -partial include -c 30 -f 5 -p 8 --plot_type png --min_distinct_haplotypes 1 -o haplotypes_3bp_regions --plot all --discrete_calls dosage -i diploid -z 2 --locus_correctness 80

Options may be given in any order.

Example commands
----------------

Output
------
