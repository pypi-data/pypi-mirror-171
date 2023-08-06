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

| **SMAP haplotype-window** extracts haplotypes from reads aligned to a predefined set of Windows in a reference sequence, wherein each Window is enclosed by a pair of Border regions.
| **SMAP haplotype-window** can be used for highly multiplex amplicon sequencing (HiPlex) or Shotgun sequencing data.
| **SMAP haplotype-window** extracts an entire DNA sequence between two Borders as a haplotype allele, without prior knowledge of polymorphisms within that sequence, and considers any unique DNA sequence as a haplotype. This is different from :ref:`SMAP haplotype-sites  <smaphaploquickstart>`, which performs read-backed haplotyping using prior positional information of read alignments and creates multi-allelic haplotypes from a concatenated short string of polymorphic sites (ShortHaps).

  .. image:: ../images/window/SMAP_haplotype_window_SQS_short_v2.png


| In the **SMAP haplotype-window** workflow, the user first selects Windows (loci to be haplotyped) enclosed by pairs of Border regions. Then, for each BAM file and each Window, **SMAP haplotype-window** extracts the ID's of reads that overlap with the respective Windows with at least one nucleotide. Using the list of read-IDs, a new temporary FASTQ file is created for each sample-Window combination. Then, for each sample-Window FASTQ file, the corresponding Border sequences are used for pattern-match read trimming with `Cutadapt <https://cutadapt.readthedocs.io/en/stable/>`_. The remaining read sequences per Window are considered haplotypes, which are counted and listed in an integrated haplotype table per sample and per Window.  
|
| **SMAP haplotype-window** considers the entire read sequence spanning the region between the Borders as haplotype.
| **SMAP haplotype-window** filters out genotype calls of Windows with low read depth and low frequency haplotypes to control for noise in the data.
| **SMAP haplotype-window** creates a multi-allelic haplotype matrix listing haplotype counts and frequencies per Window, per sample, across the sample set.
| **SMAP haplotype-window** plots the haplotype frequency distribution across all Windows per sample, and the distribution of haplotype diversity (number of distinct haplotypes per locus) across the sample set.
| **SMAP haplotype-window** can transform the haplotype frequency table into multi-allelic discrete genotype calls.

Integration in the SMAP workflow
--------------------------------

.. image:: ../images/window/SMAP_global_scheme_home_window.png

:purple:`SMAP haplotype-window requires this input:`
	
	1. a FASTA file with the reference sequence. Typically, whole genome reference sequences are used for Shotgun sequencing data, while a reference consisting of selected candidate genes may be created by **SMAP target-selection** for HiPlex data.  
	2. a GFF file with the coordinates of pairs of borders that enclose a window to define the locus positions, created with **SMAP sliding-frames** for Shotgun data or **SMAP design** for HiPlex data.  
	3. a set of FASTQ files with preprocessed reads that need to be haplotyped. Any number of samples may be given and will be processed in parallel.  
	4. a set of BAM files made with `BWA-MEM <http://bio-bwa.sourceforge.net/bwa.shtml>`_ using the respective reference sequence and FASTQ files.  
	5. optional: a FASTA file containing the gRNA sequences, created by **SMAP design**, in case CRISPR was performed by stable transformation with a CRISPR/gRNA delivery vector, see also :ref:`CRISPR <SMAPwindowcrispr>`.  

Genotype call tables created by **SMAP haplotype-window** may further be analysed with **SMAP grm** (for HiPlex and Shotgun data), or with **SMAP effect-prediction** (for HiPlex data).

.. _SMAPwindowcommands:
 
Commands & options
------------------

.. tabs::

   .. tab:: general options

	  | ``-genome`` :white:`###################` *(str)* :white:`###` FASTA file with the reference genome sequence.
	  | ``–borders`` :white:`##################` *(str)* :white:`###` GFF file with the coordinates of pairs of Borders that enclose a Window. Must contain NAME=<> in column 9 to denote the Window name.
	  | ``-alignments_dir`` :white:`#############` *(str)* :white:`###` Path to the directory containing BAM and BAM index (BAI) files. All BAM files should be in the same directory [default current directory].
	  | ``–sample_dir`` :white:`################` *(str)* :white:`###` Path to the directory containing FASTQ files with the reads mapped to the reference genome to create the BAM files. The FASTQ file names must have the same prefix as the BAM files specified in ``-alignments_dir`` [no default].
	  | ``-–guides`` :white:`##################` *(str)* :white:`###` Optional FASTA file containing the sequences from gRNAs used in CRISPR genome editing. Useful when amplicons on the CRISPR/gRNA delivery vector are included in the HiPlex amplicon mixture.
	  | ``--write_sorted_sequences`` :white:`#############` Write FASTQ files containing the reads for each Window in a separate file per input sample [default off].
	  | ``-p``, ``--processes`` :white:`############` *(int)* :white:`###` Number of parallel processes [1].
	  | ``--memory_efficient`` :white:`#################` Reduces the memory load significantly, but increases time to calculate results.
	  | ``-o``, ``--out`` :white:`################` *(str)* :white:`###` Basename of the output file without extension [""].
	  | ``-h``, ``--help`` :white:`######################` Show the full list of options. Disregards all other parameters.
	  | ``-v``, ``--version`` :white:`####################` Show the version. Disregards all other parameters.
	  | ``--debug`` :white:`#########################` Enable verbose logging. Provides additional intermediate output files used for sample-specific QC.
	  |
	  | Options may be given in any order.
	  
   .. tab:: filtering options
   
	  | ``-q``, ``--min_mapping_quality`` :white:`####` *(int)* :white:`###` Minimum BAM mapping quality to retain reads for analysis [30].
	  | ``-c``, ``--min_read_count`` :white:`#######` *(int)* :white:`###` Minimum total number of reads per locus per sample [0].
	  | ``-d``, ``--max_read_count`` :white:`#######` *(int)* :white:`###` Maximum number of reads per locus per sample, read depth is calculated after filtering out the low frequency haplotypes (``-f``) [inf].
	  | ``-f``, ``--min_haplotype_frequency`` :white:`#` *(int)* :white:`###` Set minimum haplotype frequency (in %) to retain the haplotype in the genotyping matrix. Haplotypes above this threshold in at least one of the samples are retained. Haplotypes that never reach this threshold in any of the samples are removed [0].
	  | ``-j``, ``--min_distinct_haplotypes`` :white:`#` *(int)* :white:`###` Set minimum number of distinct haplotypes per locus across all samples. Loci that do not fit this criterium are removed from the final output [0].
	  | ``-k``, ``--max_distinct_haplotypes`` :white:`#` *(int)* :white:`###` Set maximum number of distinct haplotypes per locus across all samples. Loci that do not fit this criterium are removed from the final output [inf].
	  | ``--max_error`` :white:`#############` *(float)* :white:`###` The maximum error rate (between 0 and 1; but not exactly 1) for finding the border sequences in the reads [0].
	  | 
	  | Options may be given in any order.
	  

   .. tab:: file formatting options
   
	  | ``-m``, ``--mask_frequency`` :white:`#######` *(float)* :white:`##` Mask haplotype frequency values below this threshold for individual samples. Can be used to mask noise.  Haplotype frequency values below ``-m`` are set to ``-u``. Haplotypes are not removed removed from the genotype table based on this value, use ``--min_haplotype_frequency`` for this purpose instead.
	  | ``-u``, ``--undefined_representation`` :white:`#` *(str)* :white:`###` Value to use for non-existing or masked data [NaN].
	  | ``--cervus`` :white:`###########` Create genotype table in the format that can be used as input for Cervus parental analysis [default off].

   .. tab:: graphical output options

	  | ``--plot`` :white:`###` *(all, summary, nothing)* :white:`##` Select which plots are generated. Choosing "nothing" disables plot generation. Passing "summary" only generates graphs with information for all samples, while "all" will also generate per-sample plots [default "summary"].
	  | ``-t``, ``--plot_type`` :white:`#####` *(png, pdf)* :white:`##` Choose the file type for the plots [png].


   .. tab:: options for discrete calling in individual samples
	  
	   This option is primarily supported for diploids and tetraploids. Users can define their own custom frequency bounds for species with a higher ploidy, but this requires optimization based on the observed haplotype frequency distributions.
	  
	  ``-e``, ``–-discrete_calls`` :white:`###` *(str)* :white:`###` Set to "dominant" to transform haplotype frequency values into presence(1)/absence(0) calls per allele, or "dosage" to indicate the allele copy number.
	  
	  ``-i``, ``--frequency_interval_bounds`` :white:`##` Frequency interval bounds for classifying the read frequencies into discrete calls. Custom thresholds can be defined by passing one or more space-separated values (integer or float) which represent relative frequencies in percentage. For dominant calling, one value should be specified. For dosage calling, an even total number of four or more thresholds should be specified. The usage of defaults can be enabled by passing either "diploid" or "tetraploid". The default value for dominant calling (see discrete_calls argument) is 10, regardless whether or not "diploid" or "tetraploid" is used. For dosage calling, the default for diploids is "10 10 90 90" and for tetraploids "12.5 12.5 37.5 37.5 62.5 62.5 87.5 87.5"
	  
	  ``-z``, ``--dosage_mask`` :white:`###` *(int)* :white:`###` Mask dosage calls in the loci for which the total dosage call for a given locus at a given sample differs from the defined value. For example, in diploid organisms the total dosage call must be 2, and in tetraploids the total dosage call must be 4. (default no masking).
	 
	  ``--locus_correctness`` :white:`########` *(int)* :white:`###` Threshold value: % of samples with locus correctness. Create a new GFF file defining only the loci that were correctly dosage called (-z) in at least the defined percentage of samples (default no filtering).
	  
	  ``--frequency_interval_bounds`` **in practical examples and additional information on the dosage mask:**
	  
	  .. tabs::

		 .. tab:: diploid dosage
			
			**discrete dosage calls for diploids (0/1/2)**
			
			Use this option if you want to customize discrete calling thresholds. Haplotype calls with frequency below the lowerbound percentage are considered "not detected" and receive dosage \`0´\. Haplotype calls with a frequency between the lowerbound and the next percentage are considered heterozygous and receive haplotype dosage \`1´\.  Haplotype calls with frequency above the upperbound percentage are considered homozygous and scored as haplotype dosage \`2´\. default \<10, [10:90], >90 \. Should be written with spaces between percentages, percentages may be written as floats or as integers [10 10 90 90].
			
			*e.g.* ``--discrete_calls dosage --frequency_interval_bounds 10 10 90 90`` translates to: haplotype frequency < 10% = 0, haplotype frequency > 10% & < 90% = 1, haplotype frequency > 90% = 2.
			
			Graphical examples of these thresholds can be found in :ref:`these tabs <SMAPhaplofreq>`.
			
		 .. tab:: diploid dominant
			
			**discrete dominant calls for diploids (0/1)**
			
			LowerBound frequency for dominant call haplotypes. Haplotypes with frequency above this percentage are scored as dominant present haplotype [10]. 	
			
			*e.g.* ``--discrete_calls dominant --frequency_interval_bounds 10`` translates to: haplotype frequency < 10% = 0, haplotype frequency > 10% = 1
			
			Graphical examples of these thresholds can be found in :ref:`these tabs <SMAPhaplofreq>`.

		 .. tab:: tetraploid dosage
			
			**discrete dosage calls for tetraploids (0/1/2/3/4)**
			
			Use this option if you want to customize discrete calling thresholds, haplotype calls with frequency below the lowerbound percentage are considered not detected and receive dosage \`0´ \. Haplotype calls with frequency between the lowerbound and next percentage are considered present in 1 out of 4 alleles and scored as haplotype dosage \`1´ \, haplotype frequencies in the next frequency interval are scored as haplotype dosage \`2´ \, and so on. Haplotype calls with frequency above the upperbound percentage are considered homozygous and scored as haplotype dosage \`4´ \ default \<12.5, [12.5:37.5], [37.5:62.5], [62.5:87.5], >87.5 \. Should be written with spaces between percentages, percentages may be written as floats or as integers [12.5 12.5 37.5 37.5 62.5 62.5 87.5 87.5].
			
			*e.g.* ``--discrete_calls dosage --frequency_interval_bounds 12.5 12.5 37.5 37.5 62.5 62.5 87.5 87.5`` translates to: haplotype frequency < 12.5% = 0, haplotype frequency > 12.5% & < 37.5% = 1, haplotype frequency > 37.5% & < 62.5% = 2, haplotype frequency > 62.5% & < 87.5% = 3, haplotype frequency > 87.5% = 4.
			
			Graphical examples of these thresholds can be found in :ref:`these tabs <SMAPhaplofreq>`.
			
		 .. tab:: tetraploid dominant
			
			**discrete dominant calls for tetraploids (0/1)**
			
			LowerBound frequency for dominant call haplotypes. Haplotypes with frequency above this percentage are scored as dominant present haplotype [10].
			
			*e.g.* ``--discrete_calls dominant --frequency_interval_bounds 10`` translates to: haplotype frequency < 10% = 0, haplotype frequency > 10% = 1.
			
			Graphical examples of these thresholds can be found in :ref:`these tabs <SMAPhaplofreq>`.

		 .. tab:: Why dosage mask (-z)?

			| The dosage mask ``-z`` is an additional mask specifically for dosage calls in individuals. It masks loci within samples from the dataset (replaced by ``-u`` or ``--undefined_representation``) based on total dosage calls (= total allele count calculated from haplotype frequencies using frequency interval bounds). 
			| It is important to make a distinction between total dosage call and total number of unique alleles per locus per sample.
			| A tetraploid individual for example is expected to contain a total dosage call of 4 alleles, but can contain from 1 up to 4 unique (different) alleles:
			 
			===== = = = = ================= ================
			locus dosage  total dosage call number of unique
			                                alleles
			----- ------- -----------------	----------------
			.     a b c d .                 .               
			===== = = = = ================= ================
			aaaa  4 0 0 0 4                 1       
			aaab  3 1 0 0 4                 2       
			aabb  2 2 0 0 4                 2       
			abcc  1 1 2 0 4                 3       
			abcd  1 1 1 1 4                 4       
			===== = = = = ================= ================
			
			| The dosage mask ``-z`` evaluates the total dosage call against the expected number of alleles (2 in diploids, 4 in tetraploids), but does not consider the number of unique alleles.
			| In general the expected total dosage call for any locus is equal to the ploidy of the individual (except in exceptional cases such as aneuploidy).
			| Consider the examples of a single locus in the tabs below for illustration of the combined functions of ``-f`` (minimum haplotype frequency), ``--frequency_interval_bounds`` and ``-z`` (dosage_mask).
			
			.. tabs::

			   .. tab:: diploid dosage
				  
				  .. image:: ../images/window/dosage_mask_2n.png
			   
			   .. tab:: tetraploid dosage
			
				  .. image:: ../images/window/dosage_mask_4n.png
			
			
			| The dosage mask is applied last (after all other filters).
			| An adequate value for the filter ``-f`` (minimum haplotype frequency) is especially useful to reduce the number of masked calls across the sample set. 
			| For example, in Sample2 in the diploid example above a haplotype (c) persisted at 4.7%. If this had been filtered out using the option ``-f``, the other haplotype values would have been recalculated and the total dosage would have become 2 (haplotype aa).
			| Additionally the ``--frequency_interval_bounds`` can be tuned to the users liking at the hand of the :ref:`haplotype frequency graphs <SMAPhaplofreq>` in order to reduce the number of within sample loci filtered out by ``--dosage_mask``.

Example commands
----------------

:purple:`Pools`

.. tabs::

   .. tab:: diploid pool
	  
	  ::
			
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 30 -f 2 -m 1 -p 8 --min_distinct_haplotypes 2 

   .. tab:: tetraploid pool

	  ::
			
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 30 -f 2 -m 1 -p 8 --min_distinct_haplotypes 2 

	
:purple:`Individuals`

.. tabs::

   .. tab:: diploid individual, dominant
  
	  ::
		
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 10 --discrete_calls dominant --frequency_interval_bounds 10 -f 5 -p 8 --min_distinct_haplotypes 2

   .. tab:: diploid individual, dosage
  
	  ::
		
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 10 --discrete_calls dosage --dosage_mask 2 --frequency_interval_bounds 10 10 90 90 -f 5 -p 8 --min_distinct_haplotypes 2

  
   .. tab:: tetraploid individual, dominant
	  
	  ::
	  
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 20 --discrete_calls dominant --frequency_interval_bounds 10 -f 5 -p 8 --min_distinct_haplotypes 2

   .. tab:: tetraploid individual, dosage
	  
	  ::
	  
			smap haplotype-window -borders /path/to/GFF/ -alignments_dir /path/to/BAM/ -reads_dir /path/to/FASTQ/ -genome /path/to/RefGenome/ --min_read_count 20 --discrete_calls dosage --dosage_mask 4 --frequency_interval_bounds 12.5 12.5 37.5 37.5 62.5 62.5 87.5 87.5 -f 5 -p 8 --min_distinct_haplotypes 2
	  
	  

Output
------ 

**Tabular output**

.. tabs::

   .. tab:: General output

      By default, **SMAP haplotype-window** will return two .tsv files.  
 
      :purple:`haplotype counts`
      
      **counts_cx_fx_mx.tsv** (with x the value per option used in the analysis) contains the read counts (``-c``) and haplotype frequency (``-f``) filtered and/or masked (``-m``) read counts per haplotype per locus as defined in the BED file from **SMAP delineate**.  
      This is the file structure:
	  
		  ========= ========= ========== ======= ======= ========
		  Reference Locus     Haplotypes Sample1 Sample2 Sample..
		  ========= ========= ========== ======= ======= ========
		  Chr1      Window_1  ACGTCGTCGC 60      13      34
		  Chr1      Window_1  ACGTCGTCAC 19      90      51
		  Chr1      Window_2  GCTCATCG   70      63      87
		  Chr1      Window_2  GCTCTCG    108     22      134
		  ========= ========= ========== ======= ======= ======== 

      :purple:`relative haplotype frequency`
      
      **haplotypes_cx_fx_mx.tsv** contains the relative frequency per haplotype per locus in sample (based on the corresponding count table: counts_cx_fx_mx.tsv). The transformation to relative frequency per locus-sample combination inherently normalizes for differences in total number of mapped reads across samples, and differences in amplification efficiency across loci.  
      This is the file structure:

		  ========= ========= ========== ======= ======= ========
		  Reference Locus     Haplotypes Sample1 Sample2 Sample..
		  ========= ========= ========== ======= ======= ========
		  Chr1      Window_1  ACGTCGTCGC 0.76    0.13    0.40
		  Chr1      Window_1  ACGTCGTCAC 0.24    0.87    0.60
		  Chr1      Window_2  GCTCATCG   0.39    0.74    0.39
		  Chr1      Window_2  GCTCTCG    0.61    0.26    0.61
		  ========= ========= ========== ======= ======= ========

	  | Additionally **freqs_unfiltered.tsv** can be further filtered using the options ``-j`` (minimum distinct haplotypes) and ``-k`` (maximum distinct haplotypes), resulting in the file **freqs_distinct_haplotypes_filter.tsv**

   .. tab:: Additional output for individuals
   
	  | For individuals, if the option ``--discrete_calls`` is used, the program will return three additional .tsv files. Their order of creation and content is shown in the scheme :ref:`above <SMAPhaplostep4>`.
	  | The first file is called **haplotypes_cx_fx_mx_total_discrete_calls.tsv** and this file contains the total sum of discrete calls, obtained after transforming haplotype frequencies into discrete calls, using the defined ``--frequency_interval_bounds``. The total sum of discrete dosage calls is expected to be 2 in diploids and 4 in tetraploids.
	  | The second file is **haplotypes_cx_fx_mx_call.tsv**, which incorporates the filter ``--dosage_filter`` to remove loci per sample with an unexpected number of haplotype calls in **haplotypes_cx_fx_mx_total_discrete_calls.tsv**. The expected number of calls is set with option ``-z`` [use 2 for diploids, 4 for tetraploids].
	  | The third file, **haplotypes_cx_fx_mx_AF.tsv**, lists the population haplotype frequencies (over all individual samples) based on the total number of discrete haplotype calls relative to the total number of calls per Window.

