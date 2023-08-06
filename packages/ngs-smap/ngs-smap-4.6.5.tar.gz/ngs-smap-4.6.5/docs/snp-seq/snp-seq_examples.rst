.. raw:: html

    <style> .purple {color:purple} </style>
	
.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

########
Examples
########

.. _SMAPsnpseqex:

Illustration of amplicon distribution
-------------------------------------

| Below, we present a set of amplicons that was designed on *L. perenne* reference genome based on SNPs that were previously discovered by GBS.
| 
| Please note that while we *suggest* 'optimal' parameter settings in the command to run SMAP snp-seq, the user is adviced to run SMAP snp-seq first with the mandatory and default settings (no data filtered out), and then decide on the most optimal parameter settings for your own data. Parameter settings should be iteratively adjusted for each novel data set, after manual inspection of the output. The example data shown below are merely meant to illustrate the expected outcome of data sets processed with parameters adjusted to the specific type of library, reads and samples. If your data does not look like these examples, please check out the section :ref:`Recommendations and Troubleshooting <SMAPsnpseqfaq>` for examples (and suggested solutions).

.. tabs::

   .. tab:: HiPlex after GBS

	  | Tab command shows a typical command to run **SMAP snp-seq** for SNPs identified by GBS.
	  | The other tabs show the output of SMAP snp-seq (primer files and coordinate files for downstream analysis)

		  .. tabs::

			 .. tab:: command
			 
				:: 
					
					python3 SMAP_snp-seq.py -i /path/to/dir/ --vcf variants.vcf --reference genome.fasta --reference_vcf reference_variants.vcf
			 
			 .. tab:: primers
			 
				
			 .. tab:: SMAP position files
			 
				
