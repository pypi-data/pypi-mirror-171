.. raw:: html

    <style> .purple {color:purple} </style>
    <style> .white {color:white} </style>

.. role:: purple
.. role:: white

.. _SMAP_target-selection_usage:

#############
Scope & Usage
#############

Scope
-----


**SMAP target-selection** is run prior to **SMAP design**.
HiPlex amplicon design optimization starts with choosing the set of target sequences (*e.g.* candidate genes) for which primers need to be designed.
To ensure primer and/or gRNA specificity by **SMAP design**, genome sequences with high sequence similarity should be included in the set of reference sequences. One straightforward approach is to use precomputed gene families such as provided by the comparative genomics platform `PLAZA <https://bioinformatics.psb.ugent.be/plaza/>`_. Alternatives are to group target genes by homology group, pathway, interpro domain, or other shared sequence features (*e.g.* `domain repository <https://www.ebi.ac.uk/interpro/about/consortium/>`_).

----

Integration in the SMAP workflow
--------------------------------

.. image:: ../images/target-selection/SMAP_global_scheme_home_target_selection.png

**SMAP target-selection** is run on a reference genome FASTA file, a genome annotation GFF file and a geneID list (optionally grouped) to extract and reorient candidate (gene) sequences before further downstream analysis such as read mapping, **SMAP design**, **SMAP haplotype-sites**, **SMAP haplotype-window** and **SMAP effect-prediction**.  
**SMAP target-selection** is run to create HiPlex designs.  

Guidelines for the selection of reference sequences
---------------------------------------------------

* A reference sequence FASTA file should include all target regions (*e.g.* sets of candidate genes, grouped by gene family or genetic pathway).
* In case sets of candidate genes are used as targets, the reference should include as many as possible paralogous sequences (or any other region with high sequence homology, BLAST hit, pseudogenes, etc.) to ensure primer specificity and minimal off-target primer binding. Precomputed gene families such as those retrieved from comparative genomics platforms as `PLAZA <https://bioinformatics.psb.ugent.be/plaza/>`_ are ideal for this. 
* All sequences in the reference sequence FASTA file should encode candidate genes on the positive strand (CDS orientation) to facilitate compatibility with downstream analysis (see Commands & options: ``--selectGenes``).
* The GFF file should contain at least the **genome_region** and the **CDS** features of all target regions. The coordinates of the features should correspond to their respective sequence in the reference sequence FASTA file. The GFF file can contain surplus target regions not present in the reference sequence FASTA file.
* The reference sequence FASTA and corresponding GFF file can be extracted from a reference genome sequence using **SMAP target-selection**.

Commands & options
------------------

Reference gene sets in GFF and FASTA format can be extracted with the python script **SMAP_target-selection.py**, provided in the **SMAP utility** tools.

| It is mandatory to specify the genome GFF and FASTA file of the species, the gene families data file and the species as positional arguments:

| ``gff3 file`` :white:`######` *(str)* :white:`###` Path to the gff3 file (tab-delimited) of the species containing gene, CDS, and exon features with positions relative to the fasta file [no default].
| Example from PLAZA: `annotation.selected_transcript.all_features.ath.gff3.gz <https://ftp.psb.ugent.be/pub/plaza/plaza_public_monocots_05/GFF/ath/annotation.selected_transcript.all_features.ath.gff3.gz>`_
| ``fasta file`` :white:`#####` *(str)* :white:`###` Path to the FASTA file containing the genomic sequence of the species [no default].
| Example from PLAZA: `ath.fasta.gz <https://ftp.psb.ugent.be/pub/plaza/plaza_public_dicots_05/Genomes/ath.fasta.gz>`_
| ``gene families data file`` :white:`#####` *(str)* :white:`###` Path to the gene family information file (tab-delimited) for the (coding) genes, separated per gene family type [no default].
| Example from PLAZA: `genefamily_data.HOMFAM.csv.gz <https://ftp.psb.ugent.be/pub/plaza/plaza_public_dicots_05/GeneFamilies/genefamily_data.HOMFAM.csv.gz>`_
| ``species`` :white:`#####` *(str)* :white:`###` Species, corresponding with species indicated in the gene family info file. [no default].
| Example: ath.

The gene families data file can be used to group genes by homology group, pathway, interpro domain, etc., by listing the group_id in the first column of the file, species and gene_id in the second and third column, respectively, and together with the list of 'group_id's' given with the option ``-f``, ``--hom_groups``

.. tabs::

   .. tab:: Example: gene families data file

	  .. csv-table::
	     :file: ../tables/target-selection/gene_families_data_file.csv
	     :header-rows: 1

   .. tab:: Example: group_id's file given with option ``-f, --hom_groups``

	  .. csv-table::
	     :file: ../tables/target-selection/hom_groups.csv
	     :header-rows: 0


| It is mandatory to specify a list with homology groups of interest or a list with genes of interest:

| ``-f``, ``--hom_groups`` :white:`######` *(str)* :white:`###` Path to the list with homology groups of interest [no default and given list with genes is used].
| ``-g``, ``--genes`` :white:`#########` *(str)* :white:`###` Path to the list with genes of interest [no default and given list with homology groups is used].

| Optionally, a flanking region can be extracted upstream and downstream of the target gene:

| ``-r``, ``--region`` :white:`#########` *(int)* :white:`###` Region to extend the FASTA sequence of the genes of interest on both sides with the given number of nucleotides or with the maximum possible [default: 0 or enter a positive value].

Options may be given in any order.


Example commands
----------------

Command to run the script with specified GFF and FASTA file, gene families data file, species, region and list with genes of interest::

		python3 SMAP_target-selection.py /path/to/gff /path/to/fasta /path/to/gene_family_info ath --region 500 --genes /path/to/gene_list

Command to run the script with specified GFF and FASTA file, gene families data file, species, region and list with homology groups of interest::

		python3 SMAP_target-selection.py /path/to/gff /path/to/fasta /path/to/gene_family_info ath --region 500 --hom_groups /path/to/hom_list

| Once the FASTA and GFF files are obtained, **SMAP design** is run with these files and optionally with a gRNA file. **SMAP design** first filters the gRNAs from the list and generates amplicons on the reference sequences. See further description under :ref:`SMAP design <SMAPdesignHIW>`.
| If the script is run in the directory where the input files are, then it is still required to denote the path/to/ as "./<file>", otherwise the script likely attempts to place the output at the root directory, possibly generating the error: permission denied for "/<output_file>".

Output
------

