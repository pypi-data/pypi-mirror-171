
.. raw:: html

    <style> .purple {color:purple} </style>

.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

############
How It Works
############

.. _SMAPdesignHIW:

Workflow of SMAP design
+++++++++++++++++++++++

.. image:: ../images/design/SMAPdesign_HIW.png

| The target genes must be provided as a FASTA and associated GFF file containing at least the *CDS* feature, which can be obtained using **SMAP target-selection**.
|
| The gRNAs are provided by the user as a list with the standard output of CRISPOR, FlashFry, or any other tab-delimited file with matching format. The list is filtered based on several criteria: gRNAs with a poly-T stretch (≥4T; a Pol III termination signal), and *Bsa*\I and *Bbs*\I restriction sites (for cloning) are removed and only gRNAs targeting the ‘central part’ of the CDS (as defined by the user as a length percentage) are retained. The gRNAs must also have a minimum user-defined MIT score, when available. For each gene, Primer3 designs a maximum of 150 amplicons (by default) of a user-defined size range. The specificity of each primer is tested against all reference sequences, ensuring no cross-amplification is possible. Amplicons are spaced by a minimum of 5 bp to spread the amplicons across the target genes. Amplicons containing a stretch of 10 or more identical nucleotides (homopolymers) are filtered out since they will likely result in low quality reads. If no gRNAs are provided by the user (e.g., in case of screening for natural variation), SMAP design selects sets of non-overlapping amplicons to maximize reference sequence coverage.
|
| Filtered gRNAs are grouped to amplicons by positional overlap. By default, a gRNA is only grouped to an amplicon if the distance between the end of the primer and gRNA binding site is at least 15 bp. Amplicons are ranked based on the gRNAs they cover according to the following criteria and order: 1) the number of gRNAs (an amplicon with multiple gRNAs will rank higher than an amplicon with a single gRNA); 2) the positional overlap between gRNAs (amplicons with non-overlapping gRNAs will rank highest); 3) the average gRNA specificity scores (e.g., MIT score); and 4) the average gRNA efficiency scores (such as the Doench and out-of-frame scores). If no specificity or efficiency scores are provided in the gRNA file, amplicons are only ranked by the first two criteria. Ultimately, **SMAP design** selects a (user-defined) maximum number of top-ranking, non-overlapping amplicons per gene, each covering a (user-defined) maximum number of gRNAs.
|
| **SMAP design** generates two files by default: a tab-separated values (TSV) file with the primer sequences sequentially numbered per gene and a GFF file with the primer locations on the target gene reference sequences (and other annotation features that were included in the GFF input file). If a gRNA list is provided, SMAP design also generates a TSV file with the selected gRNA sequences per gene. Sequences for which no design was retained are included at the end of the primer and gRNA file with extra information on the reason for design failure. Optionally, **SMAP design** creates a summary file and summary graphs, to facilitate quick evaluation of the set of gRNAs and amplicons. These graphs show the relationship between the number of gRNAs and the number of non-overlapping amplicons per gene that **SMAP design** generated and indicate the reasons for not retaining any gRNA-overlapping amplicons on given genes. This is either because no gRNAs were designed for that gene, none of the gRNAs passed the filters, Primer3 was not capable of designing specific amplicons for the gene, or there was no overlap between the gRNAs and the amplicons. Optionally, a GFF file is created with positions of border sequences required for downstream amplicon analysis by SMAP haplotype-window and a BED file required for SMAP haplotype-sites. In debug mode, an extra GFF output file containing all amplicons and gRNAs prior to filtering is given as a way to visualize the relative positions of all amplicons and gRNAs and also describes ways to select gRNAs and existing primers/amplicons during iterative cycles of parameter tuning. Finally, an optional GFF file can be generated with all amplicons and their respective gRNAs after filtering for each gene to manually select amplicons of interest.


SMAP target-selection
+++++++++++++++++++++

The **SMAP utility** tool :ref:`SMAP target-selection <SMAP_target-selection_usage>` is run prior to **SMAP design**.  

**SMAP design** minimally requires as input a FASTA file with target sequences and a GFF file with gene features such as gene, CDS, exon.
Once the FASTA and GFF files are obtained, **SMAP design** is run with these files and optionally with a gRNA file. **SMAP design** first filters the gRNAs from the list and generates amplicons on the reference sequences.

----

gRNA filtering
++++++++++++++

| gRNAs are designed by third-party software like :ref:`FlashFry or CRISPOR <SMAPDesigngRNA>`.
| **SMAP design** applies a couple of filters to gRNAs:

* First, **SMAP design** checks for each gRNA sequence whether it is indeed present in the reference sequence FASTA file and to which strand it corresponds.
* Next, gRNAs with poly-T stretches are discarded (by default) since they create a termination signal for Pol III.
* gRNAs with *Bsa*\I or *Bbs*\I recognition sites are also discarded (by default) since those restriction enzymes are very often used to clone the gRNAs into expression vectors. To find these sites, the gRNA sequence (without PAM) is extended by the last 6 bases of the promoter and first 6 bases of the scaffold as these extensions can create additional restriction sites.
* gRNAs with an MIT score (also known as Hsu score) below the threshold are discarded. The MIT score gives an indication on the specificity of the gRNA. The higher the MIT score the more specific the gRNA. More info on the MIT score can be found `here <https://pubmed.ncbi.nlm.nih.gov/23873081/>`_.
* gRNAs that target the upstream or downstream ends of the CDS are discarded by default. A gRNA targetting the start of the CDS has a chance of creating an alternative translational start site which can result in a slightly truncated, yet functional protein. A gRNA targeting the end of the CDS might not result in a full knock-out. **SMAP design** calculates the length of the CDS and the position of the gRNA in the CDS; if the gRNA targets the first or last 20% of the CDS length (by default), the gRNA is discarded. As such, the length of the introns do not influence the calculation. Users can adjust the length of 5' and 3' excluded CDS regions.
* The output of FlashFry or CRISPOR can be used directly as input of **SMAP design**. The first row of the gRNA file should be a header and is skipped.

Amplicon generation
+++++++++++++++++++

Primer3 is used to generate amplicons on each target gene with the following parameters::

    'PRIMER_PRODUCT_SIZE_RANGE': [[-minl, -maxl]],
    'PRIMER_NUM_RETURN': --generateAmplicons,
    'PRIMER_MAX_LIBRARY_MISPRIMING': --primerMaxLibraryMispriming,
    'PRIMER_PAIR_MAX_LIBRARY_MISPRIMING': --primerPairMaxLibraryMispriming,
    'PRIMER_MAX_TEMPLATE_MISPRIMING': --primerMaxTemplateMispriming,
    'PRIMER_PAIR_MAX_TEMPALTE_MISPRIMING': --primerPairMaxTemplateMispriming,
    'PRIMER_MIN_LEFT_THREE_PRIME_DISTANCE': 5,
    'PRIMER_MIN_RIGHT_THREE_PRIME_DISTANCE': 5,

* The **PRIMER_PRODUCT_SIZE_RANGE** parameter determines the size range of the amplicons. The default is set to 120 - 150 bp
* The **PRIMER_NUM_RETURN** parameter  determines the maximum number of amplicons that Primer3 should generate per reference sequence. The default is set to 150 amplicons.
* The **PRIMER_MAX_LIBRARY_MISPRIMING** parameter is the maximum score of a primer to be retained. The score is based on the ability of the primer to bind to other reference sequences in the FASTA file. The default is set to 12.
* The **PRIMER_PAIR_MAX_LIBRARY_MISPRIMING** parameter is the maximum score of a primer pair to be retained. The score is based on the ability of the primer to bind to other reference sequences in the FASTA file. The default is set to 24.
* The **PRIMER_MAX_TEMPLATE_MISPRIMING** parameter is the maximum score of a primer to be retained. The score is based on the ability of the primer to bind elsewhere in the reference sequence.
* The **PRIMER_PAIR_MAX_TEMPLATE_MISPRIMING** parameter is the maximum score a primer pair can have to be used. The score is based on the ability of the primer to bind elsewhere in the reference sequence.
* The **PRIMER_MIN_LEFT_THREE_PRIME_DISTANCE** parameter determines the minimum number of bases between the ends of the left primers. This is set to 5 bp to prevent design of amplicons around hotspots and so spread the amplicons across the reference sequence.
* The **PRIMER_MIN_RIGHT_THREE_PRIME_DISTANCE** parameter determines the minimum number of bases between the ends of the right primers. This is set to 5 bp to prevent design of amplicons around hotspots and so spread the amplicons across the reference sequence.

A mispriming library is given to Primer3 consisting of all reference sequences in the FASTA file. This will ensure that no primers can bind to other reference sequences. These sets of reference sequences can conveniently be created with **SMAP target-selection**.

If no gRNAs were given to **SMAP design**, it will select as many non-overlapping amplicons as possible as output.

Assignment of gRNAs to amplicons
++++++++++++++++++++++++++++++++

If a gRNA is located between the coordinates of the forward and reverse primer and there is a minimum distance (by default 15 bp) between the gRNA binding site (including the PAM) and both primers, the gRNA is retained. gRNAs are assigned to the amplicons in order of highest specificity and efficiency scores, until the maximum allowed number of assigned gRNAs per amplicon is reached ``--numbergRNAs``.

Amplicon ranking
++++++++++++++++

| At this stage, the amplicons are ranked according to the gRNAs that were assigned to the amplicon.

* First the amplicons are ranked based on the number of gRNAs that were assigned. If the user set the ``--numbergRNAs`` parameter to 3, amplicons with 3 gRNAs will be ranked first, followed by amplicons with 2 gRNAs and then amplicons with 1 gRNA.
* Next, within the groups of amplicons with an equal number of gRNAs, the amplicons for which the gRNAs do not overlap are ranked above the amplicons for which the gRNAs do overlap. This is to spread the gRNA target sites as much as possible within each amplicon.
* Then, the average MIT score (specificity score) and average number of off-targets of the gRNAs per amplicon is calculated. The amplicons with the highest average MIT score and the lowest number of off-targets are ranked highest.
* Finally, the average Doench score (efficiency score) and average OOF score of the gRNAs per amplicon is calculated. The amplicons with the highest average Doench and OOF score are ranked highest.

Amplicon and gRNA selection
+++++++++++++++++++++++++++

| To pick the best scoring amplicons, the position in the gene of the highest ranking amplicon is compared to the position of the second highest ranking amplicon.
| If the amplicons do not overlap, the two amplicons are retained. If the amplicons overlap, the position of the highest ranking amplicon is compared to the position of the third highest ranking amplicon and checked for overlap and so on until the maximum number of allowed non-overlapping amplicons per gene is reached.
| If the maximum number of non-overlapping amplicons is not reached, the amplicon combination with the most amplicons is selected.
| The information (ID, position, sequences...) of the selected amplicons and gRNAs are output to primer, gRNA, and GFF files.
