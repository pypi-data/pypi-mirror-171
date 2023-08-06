.. raw:: html

    <style> .purple {color:purple} </style>
    <style> .white {color:white} </style>
    
.. role:: purple
.. role:: white

########
Examples
########

.. _SMAPeffectex:

Illustration of SMAP effect-prediction
--------------------------------------

Below, we present a fictive example data set. The command to run **SMAP effect-prediction** is displayed with varying parameter settings to compare their respective output.

**SMAP effect-prediction** collects the following information from files prepared by the other modules of SMAP:

.. tabs::

   .. tab:: example input

	1)	the gene sequence from the reference genome; **SMAP target-selection** extracts the gene sequence and places it with the CDS on the + strand orientation in the reference FASTA file used for SMAP.  
	#)	the position of the CDS regions in the reference sequence; **SMAP target-selection** calculates the correct positions of the CDS with respect to the extracted gene reference sequence of 1).  
	#)	the position of the amplicon(s) in the gene reference sequence; **SMAP design** creates pairs of primers for HiPlex sequencing of genomic DNA, and stores the relative position of the corresponding border regions in a GFF file.  
	#)	the position of gRNA(s) for CRISPR/Cas genome editing within an amplicon; **SMAP design** optionally creates one or more gRNAs per amplicon to induce mutations in a particular position of the reference genome.  
	#)	the collection of haplotypes per locus and their relative frequencies per sample; **SMAP haplotype-window** extracts haplotypes (exact DNA sequences) using the exact same reference gene coordinates as outlined in 1)-4).  

   .. tab:: reference sequence FASTA
	 
	  .. csv-table:: 
	     :delim: ;
	     :file: ../tables/effect/HowItWorks/genome_TR.fasta
	     :header-rows: 0
	  
   .. tab:: gene and CDS positions GFF
	  
	  .. csv-table:: 
	     :delim: , 
	     :file: ../tables/effect/HowItWorks/local_gff_file_TR.gff
	     :header-rows: 0
	  
   .. tab:: border positions GFF
	  
	  .. csv-table:: 
	     :delim: ;
	     :file: ../tables/effect/HowItWorks/borders_TR.gff
	     :header-rows: 0
	  
   .. tab:: gRNA positions GFF
	  
	  .. csv-table:: 
	     :delim: ;
	     :file: ../tables/effect/HowItWorks/guides_TR.gff
	     :header-rows: 0
	  
   .. tab:: SMAP haplotype-window haplotype frequency table
	  
	  .. csv-table:: 
	     :delim: ;
	     :file: ../tables/effect/HowItWorks/haplotype_frequency_TR.tsv
	     :header-rows: 1
	     :widths: 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
	  

The user is advised to run **SMAP effect-prediction** first with the mandatory and default settings, and then decide on the most optimal parameter settings for your own design.
The example data shown below are merely meant to illustrate the expected outcome of data sets processed with parameters adjusted to the specific species and reference (gene) sets.
**SMAP effect-prediction** parameter settings are described in the section :ref:`Commands & options <SMAPeffectSummaryCommand>`.

.. tabs::

   .. tab:: wide range ROI ``-s 15 -r 20``

       .. tabs::

           .. tab:: threshold 50%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 15 -r 20 -t 50 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t50/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t50/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t50/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t50/discretized.tsv
                         :header-rows: 1

           .. tab:: threshold 70%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 15 -r 20 -t 70 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t70/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t70/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t70/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t70/discretized.tsv
                         :header-rows: 1

           .. tab:: threshold 99%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 15 -r 20 -t 99 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t99/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t99/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t99/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/wide_range_ROI/t99/discretized.tsv
                         :header-rows: 1

   .. tab:: narrow range ROI ``-s 5 -r 5``

       .. tabs::

           .. tab:: threshold 50%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 5 -r 5 -t 50 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t50/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t50/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t50/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t50/discretized.tsv
                         :header-rows: 1

           .. tab:: threshold 70%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 5 -r 5 -t 70 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t70/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t70/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t70/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t70/discretized.tsv
                         :header-rows: 1

           .. tab:: threshold 99%

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a ::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 5 -r 5 -t 99 -e dosage -i diploid
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t99/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t99/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t99/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/narrow_range_ROI/t99/discretized.tsv
                         :header-rows: 1

   .. tab:: ``--no_gRNA_relative_naming`` 

       .. tabs::

           .. tab:: threshold 99% -s 15 -r 20

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a wide range ROI::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 15 -r 20 -t 99 -e dosage -i diploid -g 
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/wide_range_ROI/t99/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/wide_range_ROI/t99/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/wide_range_ROI/t99/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/wide_range_ROI/t99/discretized.tsv
                         :header-rows: 1

           .. tab:: threshold 99% -s 5 -r 5

               .. tabs::

                   .. tab:: Command
                     
                         Command used to run **SMAP effect-prediction** on a narrow range ROI::
                    
                             smap effect-prediction haplotype_frequency.tsv genome.fasta borders.gff -a gene_features.gff -u guides.gff -p CAS9 -s 15 -r 20 -t 99 -e dosage -i diploid -g 
                    
                   .. tab:: annotate
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/narrow_range_ROI/t99/annotate.tsv
                         :header-rows: 1
                     
                   .. tab:: collapsed
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/narrow_range_ROI/t99/collapsed.tsv
                         :header-rows: 1
                     
                   .. tab:: aggregated
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/narrow_range_ROI/t99/aggregated.tsv
                         :header-rows: 1
                      
                   .. tab:: discretized
                   
                      .. csv-table::
                         :delim: tab
                         :file: ../tables/effect/examples/relative_naming/narrow_range_ROI/t99/discretized.tsv
                         :header-rows: 1
