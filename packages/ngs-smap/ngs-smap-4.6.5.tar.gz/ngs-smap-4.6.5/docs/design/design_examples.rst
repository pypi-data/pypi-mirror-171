.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

########
Examples
########

.. _SMAPdesignex:

Illustration of primer and gRNA design
--------------------------------------

Below, we present the command to run **SMAP design** and summary plots of twelve designs for different species and gene family sizes created with **SMAP design** to illustrate typically expected output.

The user is advised to run **SMAP design** first with the mandatory and default settings, and then decide on the most optimal parameter settings for your own design.
The example data shown below are merely meant to illustrate the expected outcome of data sets processed with parameters adjusted to the specific species and reference (gene) sets.
**SMAP design** parameter settings are described in the section :ref:`Commands & options <SMAPdesignSummaryCommand>`.



.. tabs::

   .. tab:: Arabidopsis

       .. tabs::

           .. tab:: Small gene family

                   Command used to run **SMAP design** on a small gene family from Arabidopsis:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04D000931_ath.fasta HOM04D000931_ath.gff -g HOM04D000931_ath_FlashFry.tsv -o HOM04D000931_ath_SMAPdesign -minl 120 -maxl 150 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000931_Ath_SMAPdesign_summary_plot.png
                    

           .. tab:: Medium gene family

                   Command used to run **SMAP design** on a medium-sized gene family from Arabidopsis:
                   
                     ::

                       python3 SMAPdesign.py HOM04D000029_ath.fasta HOM04D000029_ath.gff -g HOM04D000029_ath_FlashFry.tsv -o HOM04D000029_ath_SMAPdesign -minl 120 -maxl 150 -smy -v -sf

                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000029_Ath_SMAPdesign_summary_plot.png
                    

           .. tab:: Large gene family

                   Command used to run **SMAP design** on a large gene family from Arabidopsis:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04D000001_ath.fasta HOM04D000001_ath.gff -g HOM04D000001_ath_FlashFry.tsv -o HOM04D000001_ath_SMAPdesign -minl 120 -maxl 150 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000001_Ath_SMAPdesign_summary_plot.png
                    

   .. tab:: Chlamydomonas

       .. tabs::

           .. tab:: Small gene family

                   Command used to run **SMAP design** on a small gene family from Chlamydomonas:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04x5M006964_cre.fasta HOM04x5M006964_cre.gff -g HOM04x5M006964_cre_FlashFry.tsv -o HOM04x5M006964_cre_SMAPdesign -minl 220 -maxl 250 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04x5M006964_Cre_SMAPdesign_summary_plot.png
                    

           .. tab:: Medium gene family

                   Command used to run **SMAP design** on a medium-sized gene family from Chlamydomonas:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04x5M000141_cre.fasta HOM04x5M000141_cre.gff -g HOM04x5M000141_cre_FlashFry.tsv -o HOM04x5M000141_cre_SMAPdesign -minl 220 -maxl 250 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04x5M000141_Cre_SMAPdesign_summary_plot.png
                    

           .. tab:: Large gene family

                   Command used to run **SMAP design** on a large gene family from Chlamydomonas:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04x5M000042_cre.fasta HOM04x5M000042_cre.gff -g HOM04x5M000042_cre_FlashFry.tsv -o HOM04x5M000042_cre_SMAPdesign -minl 220 -maxl 250 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04x5M000042_Cre_SMAPdesign_summary_plot.png
                    

   .. tab:: Soybean

       .. tabs::

           .. tab:: Small gene family

                   Command used to run **SMAP design** on a small gene family from Soybean:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04D000162_gma.fasta HOM04D000162_gma.gff -g HOM04D000162_gma_FlashFry.tsv -o HOM04D000162_gma_SMAPdesign -minl 400 -maxl 800 -d 150 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000162_Gma_SMAPdesign_summary_plot.png
                    

           .. tab:: Medium gene family

                   Command used to run **SMAP design** on a medium-sized gene family from Soybean:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04D000015_gma.fasta HOM04D000015_gma.gff -g HOM04D000015_gma_FlashFry.tsv -o HOM04D000015_gma_SMAPdesign -minl 400 -maxl 800 -d 150 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000015_Gma_SMAPdesign_summary_plot.png
                    

           .. tab:: Large gene family

                   Command used to run **SMAP design** on a large gene family from Soybean:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM04D000001_gma.fasta HOM04D000001_gma.gff -g HOM04D000001_gma_FlashFry.tsv -o HOM04D000001_gma_SMAPdesign -minl 400 -maxl 800 -d 150 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM04D000001_Gma_SMAPdesign_summary_plot.png
                    

   .. tab:: Human

       .. tabs::

           .. tab:: Small gene family

                   Command used to run **SMAP design** on a small gene family from the human genome:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM03P000828_hom.fasta HOM03P000828_hom.gff -g HOM03P000828_hom_FlashFry.tsv -o HOM03P000828_hom_SMAPdesign -minl 220 -maxl 250 -rpd -d 15 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM03P000828_Hom_rpd_SMAPdesign_summary_plot.png
                    

           .. tab:: Medium gene family

                   Command used to run **SMAP design** on a medium-sized gene family from the human genome:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM03P000059_hom.fasta HOM03P000059_hom.gff -g HOM03P000059_hom_FlashFry.tsv -o HOM03P000059_hom_SMAPdesign -minl 220 -maxl 250 -rpd -d 15 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM03P000059_Hom_rpd_SMAPdesign_summary_plot.png
                    

           .. tab:: Large gene family

                   Command used to run **SMAP design** on a large gene family from the human genome:
                   
                     ::
                    
                       python3 SMAPdesign.py HOM03P000013_hom.fasta HOM03P000013_hom.gff -g HOM03P000013_hom_FlashFry.tsv -o HOM03P000013_hom_SMAPdesign -minl 220 -maxl 250 -rpd -d 15 -smy -v -sf
                    
                   Summary plot
                    
                    .. image:: ../images/design/HOM03P000013_Hom_rpd_SMAPdesign_summary_plot.png


| Using the GFF file generated by **SMAP design**, a graphical view of the amplicons and gRNAs can be obtained with a genome browser software such as CLCbio Genomics Workbench, or Geneious.
| In Geneious it would look like this.

.. image:: ../images/design/HOM04D000931_ath_graphicalOutput.png

The yellow arrows show the CDS (multiple transcripts are shown per gene), the blue arrows show the amplicons, the dark and light green arrows show the forward and reverse primer, respectively, the grey arrows show the gRNAs and the white arrows show the borders used for **SMAP haplotype-window**.

.. _SMAPdesignexrpd:

Option restrictedPrimerDesign
-----------------------------

The ``--restrictedPrimerDesign`` or ``-rpd`` option restricts amplicon design to exonic regions and will ignore large intronic regions. This speeds up the primer design and can increase retention rates, because the 150 amplicons that Primer3 designs by default will no longer be located in intronic regions, and subsequently discared because there is no overlap with a CDS.
Below are some examples comparing the design of three human gene families (with typically very large introns) with and without the ``-rpd`` option. The time needed to run these on a single core is given.


.. tabs::

            .. tab:: Small gene family (6 genes)

                  | **Without -rpd**
                  | Runtime: 00:00:26.69

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                               python3 SMAPdesign.py HOM03P000828_hom.fasta HOM03P000828_hom.gff -g HOM03P000828_hom_FlashFry.tsv -o HOM03P000828_hom_SMAPdesign -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000828_Hom_SMAPdesign_summary_plot.png

                  | **With -rpd**
                  | Runtime: 00:00:26.56

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                               python3 SMAPdesign.py HOM03P000828_hom.fasta HOM03P000828_hom.gff -g HOM03P000828_hom_FlashFry.tsv -o HOM03P000828_hom_SMAPdesign -rpd -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000828_Hom_rpd_SMAPdesign_summary_plot.png


            .. tab:: Medium gene family (34 genes)

                  | **Without -rpd**
                  | Runtime: 94:22:08.77

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                                 python3 SMAPdesign.py HOM03P000059_hom.fasta HOM03P000059_hom.gff -g HOM03P000059_hom_FlashFry.tsv -o HOM03P000059_hom_SMAPdesign -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000059_Hom_SMAPdesign_summary_plot.png

                  | **With -rpd**
                  | Runtime: 14:35:23.75

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                                 python3 SMAPdesign.py HOM03P000059_hom.fasta HOM03P000059_hom.gff -g HOM03P000059_hom_FlashFry.tsv -o HOM03P000059_hom_SMAPdesign -rpd -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000059_Hom_rpd_SMAPdesign_summary_plot.png

            .. tab:: Large gene family (98 genes)

                  | **Without -rpd**
                  | Runtime: 56:06:46.92

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                                python3 SMAPdesign.py HOM03P000013_hom.fasta HOM03P000013_hom.gff -g HOM03P000013_hom_FlashFry.tsv -o HOM03P000013_hom_SMAPdesign -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000013_Hom_SMAPdesign_summary_plot.png

                  | **With -rpd**
                  | Runtime: 08:57:11.93

                   .. tabs::

                         .. tab:: command
                                | command
                            ::

                                python3 SMAPdesign.py HOM03P000013_hom.fasta HOM03P000013_hom.gff -g HOM03P000013_hom_FlashFry.tsv -o HOM03P000013_hom_SMAPdesign -rpd -minl 220 -maxl 250 -d 15 -smy -v -sf

                         .. tab:: summary plot
                                | summary plot
                                .. image:: ../images/design/HOM03P000013_Hom_rpd_SMAPdesign_summary_plot.png

----

.. _SMAPdesignexpsp:

Option preSelectedPrimers
-------------------------

If a set of (validated) amplicons is already available and you want to find gRNAs within these amplicons, this can be done using the ``--preSelectedPrimers`` or ``-psp`` option. If this option is used, primer3 will not design any amplicons, but will merge the existing amplicons with the gRNAs to generate the designs. The user should provide a GFF file containing the alternating features: Primer_forward and Primer_reverse, whereby the Primer_reverse forms a pair with the Primer_forward just above it. Any other options concerning the amplicons are ignored, except the –ampliconLabel option.

.. tabs::

   .. tab:: input

        Examples of files required as input using option ``--preSelectedPrimers``.

         .. tabs::


               .. tab:: reference sequence FASTA

                      | Reference sequence FASTA

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/WNK_psp_HOM04D000265_ath_selected_genes_extended_500_bp_fasta.csv
                         :header-rows: 0

               .. tab:: gene annotation GFF

                      | Gene annotations

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/WNK_psp_HOM04D000265_ath_selected_genes_extended_500_bp_gff.csv
                         :header-rows: 0

               .. tab:: FlashFry gRNA file

                      | gRNA positions and scores

                      .. csv-table::
                         :file: ../tables/design/WNK_FlashFry_gRNA.csv
                         :header-rows: 1

               .. tab:: primer position GFF

                      | Primer positions

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/WNK_psp_HOM04D000265_ath_preSelectedPrimers_gff.csv
                         :header-rows: 0


   .. tab:: command

        Example command to run SMAP design with option ``--preSelectedPrimers``. ::

           python3 SMAPdesign.py HOM04D000265_ath_selected_genes_extended_500_bp.fasta HOM04D000265_ath_selected_genes_extended_500_bp.gff -g Ath_FlashFry.tsv -v -smy -o SMAPdesign_with_psp -gl -al -psp HOM04D000265_ath_preSelectedPrimers.gff

   .. tab:: output

        Examples of files generated as output with option ``--preSelectedPrimers``.

         .. tabs::

               .. tab:: summary plot

                      | Summary plot

                      .. image:: ../images/design/SMAPdesign_with_psp_summary_plot.png

               .. tab:: summary file

                      | Summary of amplicons and gRNAs

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/SMAPdesign_with_psp_summary.tsv
                         :header-rows: 1

               .. tab:: gRNA file

                      | Selected gRNAs

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/SMAPdesign_with_psp_gRNAs.tsv
                         :header-rows: 0

               .. tab:: primer file

                      | Selected primers

                      .. csv-table::
                         :delim: tab
                         :file: ../tables/design/SMAPdesign_with_psp_primers.tsv
                         :header-rows: 0
