.. raw:: html

    <style> .purple {color:purple} </style>
	
.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

############
How It Works
############

Workflow of SMAP haplotype-window
---------------------------------

.. tabs::

   .. tab:: procedure

	  | **Step 1**
	  | 
	  | **SMAP haplotype-window** extracts haplotypes from reads aligned to a predefined set of loci, here called Windows, in a reference sequence. Each Window is enclosed by a pair of Border regions.
	  | Border regions can be defined at primer binding sites, either *with* (Window 1) or *without* (Window 2) an off-set. Borders can be of variable length, defined by the user (typically 5-10 bp). Pairs of Borders can also be defined so that they enclose Sliding frames, for instance to process Shotgun data.
	  | 
	  | **Step 2**
	  | 
	  | Read mapping is used to assign reads to their corresponding locus on the reference genome. 
	  | Consider a sequenced fragment derived from a given genomic locus with a large deletion, or highly polymorphic region with multiple flanking SNPs, in the middle of the fragment. 
	  | Two flanking primers can bind the genome sequence of the sample and can amplify the fragment. Also, the two regions flanking the central polymorphism in the same read contain (near-)exact sequence similarity to the reference sequence of the genomic locus.
	  | Mapping reads with `BWA-MEM <http://bio-bwa.sourceforge.net/bwa.shtml>`_, defines which genomic locus is the origin of the sequenced fragment (the maximal exact match that seeds the alignment), and extends the alignment outwards untill a maximum number of read-reference mismatches is reached.
	  | If read-reference alignments are truncated before the end of the read, BWA-MEM removes the unmapped region of the sequence read in the resulting BAM file (called soft-clipping).
	  | Consequently, the sequence of a given read in the FASTQ file (before read mapping) may have a different length compared to the corresponding read in the BAM file (after mapping). 
	  | Also, the polymorphisms that caused the truncation of the read alignment are no longer present in the BAM file (not as alignment, not as FASTQ sequence data), and can not be used to detect polymorphisms by direct read-reference alignment comparison.
	  | 
	  | **Step 3**
	  | 
	  | For each Window, **SMAP haplotype-window** will define the Window region in the reference genome by pairing Border regions defined in a GFF file. 
	  | For each BAM file and for each Window, **SMAP haplotype-window** will identify the IDs of reads that overlap with at least one nucleotide for a given Window, retrieve their original complete read sequence from the corresponding sample's FASTQ file and create a separate FASTQ file for each sample-Window combination. 
	  | These steps make sure that reads that are soft-clipped during read alignment by BWA-MEM but that initially do contain the Border sequences at their respective ends, can still be evaluated in their entirety. Soft-clipping results in partial read alignment and removal of the unmapped part of the sequence read from the BAM file.
	  | **SMAP haplotype-window** then retrieves the respective sequences for the upstream Border and downstream Border regions using the GFF coordinates and the reference genome FASTA sequence for each Window. 
	  |
	  | **Step 4**
	  | 
	  | All separate FASTQ files (one for each sample-Window combination) are then passed to `Cutadapt <https://cutadapt.readthedocs.io/en/stable/>`_ using the Window-specific pair of Border sequences for pattern trimming. 
	  | Because the Window is defined as the region *inbetween* the Borders (*i.e.* read regions retained after removal of the Borders), the entire read sequence spanning the Window is considered as a unique haplotype. 
	  | 
	  | **Step 5**
	  | 
	  | These haplotypes are then counted per Window per sample, optionally filtered for (min/max) total read count per Window per sample.
	  | All individual sample specific haplotype count tables are integrated into a large haplotype count matrix.
	  | This procedure detects unique haplotypes in Windows enclosed by two known Border sequences consisting of any (*a priori* unknown) combination of InDels and/or SNPs, *without* using the BAM alignment itself for the detection of InDels and/or SNPs. The `BWA-MEM <http://bio-bwa.sourceforge.net/bwa.shtml>`_ alignment is merely used for efficiently sorting reads across the reference genome and grouping by locus. 
	  | Haplotype counts are converted into relative frequencies, which can then be filtered to remove low-frequency noise.
	  | The final step of **SMAP haplotype-window** is only applicable on individuals and converts haplotype frequencies into discrete calls. 
	  | Using customizable frequency intervals, haplotype frequencies can either be transformed into dominant calls (0/1) or dosage calls (0/1/2/..).

   .. tab:: overview
	  
	  | The scheme below shows an overview of the entire **SMAP haplotype-window** workflow.
	  
	  .. image:: ../images/window/haplotype_window_scheme_short_TR_all.png
	  
   .. tab:: required input

	  .. tabs::

		 .. tab:: reference sequence
		 
			The FASTA file containing the reference sequence.

		 .. tab:: GFF
         
			| The `GFF <https://en.wikipedia.org/wiki/General_feature_format#:~:text=In%20bioinformatics%2C%20the%20general%20feature,DNA%2C%20RNA%20and%20protein%20sequences.>`_ file describes the position of the Border regions on the reference sequence in 9 columns. **SMAP haplotype-window** expects two Borders that together enclose a Window, which are paired based on the \'NAME=\' field in the 9th column. The file does not need to contain a header. These fields need to be specified:

				| 1. Name of the sequence in the reference that contains the Window.
				| 2. Source of the feature. [SMAP haplotype-window]. 
				| 3. Feature type. Because in SMAP haplotype-window pairs of Borders define Windows, two feature types are used: Border_upstream and Border_downstream. Each line in the GFF is one of those borders. Borders always come in pairs.
				| 4. The start coordinate of the Border region [in the 1-based GFF coordinate system].
				| 5. The end coordinate of the Border region [in the 1-based GFF coordinate system, value must always be higher than column 4].
				| 8. Score. Irrelevant for SMAP haplotype-window [.].
				| 7. Orientation of the Border [always +].
				| 8. Phase. Irrelevant for SMAP haplotype-window [.].
				| 9. Attributes of the Border, the field \'NAME=\' is required. This field is used to pair Borders (by exact \'NAME=\' matching), and define the corresponding Window regions. The field Name must be unique for each Window and will be used to name loci in the haplotype frequency tables.

			| Depending on the type of data (HiPlex or Shotgun Seq), a specific GFF file must be created to define pairs of Borders enclosing Windows.

				.. tabs::

					.. tab:: HiPlex / primer binding sites
					
						| For HiPlex data it is advised to use the 5-10 nucleotides on the 3' of the primer binding site, where they flank the Window (to extract the sequence read region *inbetween* the primers). 

						 .. csv-table::
						    :file: ../tables/window/example_HiPlex_gff.csv
						    :header-rows: 0

					.. tab:: Shotgun Sequencing / Sliding Windows
					
						| Shotgun Sequencing data may be analysed with a set of sliding Windows, with a customisable Window size (here 50), step size (here 20), and Border length (here 10).

						 .. csv-table:: 	  
						    :file: ../tables/window/example_Shotgun_gff.csv
						    :header-rows: 0

		 .. tab:: FASTQ
		 
			A set of FASTQ files with reads that need to be haplotyped.

		 .. tab:: BAM
			
			 A set of BAM files made with `BWA-MEM <http://bio-bwa.sourceforge.net/bwa.shtml>`_ using the respective reference sequence and FASTQ files.

.. _SMAPwindowcrispr:


CRISPR extension of SMAP haplotype-window
-----------------------------------------

A specific extension of the **SMAP haplotype-window** workflow for CRISPR data can be invoked using the optional command ``--guides``.

If CRISPR-mediated genome editing was performed by stable transformation with a CRISPR/gRNA delivery vector, then the presence of the gRNA cassette in the delivery vector may be detected in the transformed genome.
Primers can be designed on the vector sequence to amplify the gRNA sequence in the gRNA expression cassette, and Border regions can be positioned directly flanking the 20 bp gRNA sequence. The haplotype of that 'locus' that is then detected is effectively a copy of the gRNA sequence incorporated into the transformed genome. 
These primers can be included in the HiPlex primer set used to screen for the genomic target loci.
SMAP **haplotype-window** can assign gRNA vector-derived reads to the respective target loci, if the user provides a FASTA file with the target loci names as identifiers and the 20 bp gRNA as sequence.
In this way, genome-edited haplotypes at genomic target loci can be detected in parallel to the gRNAs that cause them, for any number of loci and any number of samples.

  .. image:: ../images/window/smap_window_sgrna_extraction_crispr.png

Example of gRNA sequences FASTA:

========================= =
>AT1G07650_1_gRNA_001
TGAAGTCGCAGAACTTAACG
>AT1G07650_1_gRNA_002
CTGAAGTCGCAGAACTTAAC
========================= =

Example of output file with diverse genome-edited haplotypes at genomic target loci and corresponding gRNA.
By sorting on the fourth column (**Target**) in any output .tsv file, it is possible to arrange all the target loci with their corresponding gRNAs.
Note that the standard output of **SMAP haplotype-window** can be further annotated by :ref:`SMAP effect-prediction  <smapeffectoutput>`, for instance as the length difference with the reference, or even with the effect of the mutation on the predicted protein, in case candidate genes are used as reference sequence. 

.. tabs::

   .. tab:: Unsorted output file
   
     .. csv-table::
	     :file: ../tables/window/crispr_example_unsorted.csv
	     :header-rows: 1
	  
   .. tab:: Sorted output file
   
	  .. csv-table::
	     :file: ../tables/window/crispr_example_sorted.csv
	     :header-rows: 1
		

