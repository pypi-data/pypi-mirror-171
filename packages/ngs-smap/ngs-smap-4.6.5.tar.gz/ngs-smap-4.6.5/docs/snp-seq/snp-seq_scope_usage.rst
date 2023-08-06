.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

.. _SMAPsnpseqscopeusage:

#############
Scope & Usage
#############

Scope
-----

SMAP snp-seq designs HiPlex primers encompassing dedicated polymorphic SNP sites, while taking neighboring SNPs into consideration.
It is a simple application to design primer panels for targetted amplicon resequencing taking known polymorphisms into account.

:purple:`Input`

SMAP snp-seq only requires a reference sequence FASTA file and one VCF file with the polymorphisms that need to be screened, optionally, one may provide a BED file with regions or a VCF file with SNPs that specifically need to be targeted.

:purple:`Output`

| **SMAP snp-seq** provides custom filters and a list of primers to order.
| **SMAP snp-seq** creates a BED file with SMAPs to delineate HiPlex loci for downstream analyses (e.g. SMAP haplotype-sites).
| **SMAP snp-seq** creates a GFF file with borders to delineate HiPlex windows for downstream analyses (e.g. SMAP haplotype-windows).
| **SMAP snp-seq** plots :ref:`feature distributions <SMAPsnpseqex>` such as length, :ref:`of amplicons <SMAPsnpseqdef>`.

----

Integration in the SMAP workflow
--------------------------------

.. image:: ../images/snp-seq/SMAP_global_scheme_home_snp-seq.png

**SMAP snp-seq** is run on a reference sequence FASTA file and one or two VCF files, after variant calling and before **SMAP haplotype-sites** or **SMAP haplotype-windows**.  
**SMAP snp-seq** designs primer panels for HiPlex amplicon sequencing.

----

Guidelines for variant calling
------------------------------

See `Veeckman et al. (2019) <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6379033/>`_ for a comparison of different SNP calling methods.

----

.. _SMAPsnpseqSummaryCommand:
   
Commands & options
------------------

:purple:`Mandatory options for SMAP snp-seq`

SMAP snp-seq only needs a reference sequence and known SNP positions.

| ``--vcf`` :white:`######` The VCF file with SNPs [no default].  
| ``--reference`` :white:`##` The FASTA file with the reference genome sequence or candidate gene sequences [no default].

.. _SMAPdelfilter:

:purple:`Command line options` 

See tabs below for command line options and specific filter options.

.. tabs:: 

	.. tab:: input data options

		**Input data options:**

		  | ``-i``, ``--input_directory`` :white:`##` *(str)* :white:`##` Input directory [current directory]. 
		  | ``-r``, ``--regions`` :white:`########` *(str)* :white:`##`  Name of the BED file in the input directory containing the genomic coordinates of regions wherein primers must be designed [no BED file provided].  
		  | ``--target_vcf`` :white:`###############` Name of the VCF file in the input directory containing target SNPs [no VCF file with target SNPs provided].  
		  | ``--reference_vcf`` :white:`#############` Name of the VCF file in the input directory containing non-polymorphic differences between the reference genome sequence and the samples for primer design [no VCF file with reference genome differences provided].  

	.. tab:: amplicon design options

		**Amplicon design options:**

		  | ``-d``, ``--variant_distance`` :white:`############` *(int)* :white:`###` Maximum distance (in bp) between two variants to be included in the same template [500].
		  | ``-t``, ``--target_size`` :white:`###############` *(int)* :white:`###` Maximum size (in bp) of a target region [10].
		  | ``-u``, ``--target_distance`` :white:`############` *(int)* :white:`###` Minimum distance (in bp) between two target regions in a template [0].
		  | ``-min``, ``--minimum_amplicon_size`` :white:`#######` *(int)* :white:`###` Minimum size of an amplicon (incl. primers) in bp [100].
		  | ``-max``, ``--maximum_amplicon_size`` :white:`#######` *(int)* :white:`###` Maximum size of an amplicon (incl. primers) in bp [110].
		  | ``--offset`` :white:`#######################` *(int)* :white:`###` Size of the offset at the 5' and 3' end of each region. Variants in the offsets are not tagged as targets for primer design [0, all variants are potential targets].
		  | ``-minp``, ``--minimum_primer_size`` :white:`########` *(int)* :white:`###` Minimum size (in bp) of a primer [18].
		  | ``-maxp``, ``--maximum_primer_size`` :white:`########` *(int)* :white:`###` Maximum size (in bp) of a primer [27].
		  | ``-optp``, ``--optimal_primer_size`` :white:`########` *(int)* :white:`###` Optimal size (in bp) of a primer [20].
		  | ``-max_misp``, ``--maximum_mispriming`` :white:`######` *(int)* :white:`###` Maximum allowed weighted similarity of a primer with the same template and other templates [12].
		  | ``-maxn``, ``--maximum_unknown_nucleotides`` :white:`##` *(int)* :white:`###` Maximum number of unknown nucleotides (N) in a primer sequence [0].
		  | ``-ex``, ``--region_extension`` :white:`###########` *(int)* :white:`###` Extend regions in the BED file provided via the ``--regions`` option at their 5' end 3' end with the provided value [0, no region extension].
		  | ``--retain_overlap`` :white:`#######################` Retain overlap in template sequences among regions [overlap in template sequences is removed].
		  | ``--split_template`` :white:`#######################` Split the regions in the BED file provided via the ``--regions`` option in multiple templates based on the variant_distance [regions are not split].

		Options may be given in any order.
		
		Command to run **SMAP snp-seq**::
	
			python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta 

	.. tab:: output data options

		  | ``-o``, ``--output_directory`` :white:`###` *(str)* :white:`###` Path to the output directory [current directory].
		  | ``-b``, ``--border_length`` :white:`#####` *(int)* :white:`###` Border size used in the GFF file that defines the windows for SMAP haplotype-window [10].
		  | ``-s``, ``--suffix`` :white:`##########` *(str)* :white:`###` Suffix added to output files [set_1].

		Options may be given in any order.

		Command to run **SMAP snp-seq** with adjusted border length and suffix to denote the design settings::

			python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta -b 10 -s Lp_120_180bp 

----

.. _SMAPsnpseqexcommands:

Example commands
----------------

.. tabs::

   .. tab:: simple design

	  Basic command to run SMAP snp-seq::
				
		python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta
		
   .. tab:: design with target regions

	  Command to run SMAP snp-seq for a subset of regions::
				
		python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta --target.vcf targets.vcf
		
   .. tab:: design with background SNP file

	  Command to run SMAP snp-seq with secondary file with background variation::
		
		python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta --reference_vcf reference_variants.vcf
		

.. _SMAPsnpseqoutput:
   
Output
------

.. tabs::

   .. tab:: Graphical output

	  | By default, SMAP snp-seq does not provide graphical output.

   .. tab:: Tabular output
	
	  | SMAP snp-seq creates a FASTA file with primer sequences, a GFF file with primer positions on the reference sequence, a BED file with SMAPs for SMAP haplotype-sites, and a GFF file with borders for SMAP haplotype-window.
