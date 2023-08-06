.. raw:: html

    <style> .purple {color:purple} </style>
	
.. role:: purple

.. raw:: html

    <style> .white {color:white} </style>

.. role:: white

.. raw:: html

    <style> .green {color:green} </style>
    <style> .blue {color:blue} </style>
    <style> .red {color:red} </style>

.. role:: green
.. role:: blue
.. role:: red

############
How It Works
############


| **SMAP compare** uses `BEDtools intersect <https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html>`_ to identify shared loci by positional overlap between loci of two **SMAP delineate** BED files.
| **SMAP compare** then calculates summary statistics of features of overlapping loci, such as completeness scores and mean read depth per respective sample set.

For instance:

	1.	locus :green:`scaffold_1:41456-41541_+` is shared between the two sample sets.
	#.	in Set1, locus :green:`scaffold_1:41456-41541_+` is observed in 8 (out of 48) individual samples, and with mean read depth of 604.
	#.	in Set2, locus :green:`scaffold_1:41456-41541_+` is observed in 1 (out of 16) pool-Seq samples, and with mean read depth of 42.
	#.	locus :red:`scaffold_1:77858-77943_+` is only found in 3 out of 48 individuals and in none of the 16 pools.
	#.	locus :blue:`scaffold_72:23081-23166\_\-` is found in 48 out of 48 individuals, and also in 16 out of 16 pools.

| Since for each locus in either BED file, **SMAP compare** extracts the completeness scores in Set1 and Set2, respectively, it can create a pivot table with the number of **shared** loci for a given **combination of completeness scores in the two respective sets**.
| For instance, locus :green:`scaffold_1:41456-41541_+` is one example out of 8 shared loci that are found in 8 out of 48 individuals and also in 1 out of 16 pools, while locus :blue:`scaffold_72:23081-23166\_\-` is one example out of 8 shared loci that are found in 48 out of 48 individuals, and also in 16 out of 16 pools.
| For each set of shared loci for a given combination of completeness scores, **SMAP compare** also calculates the mean read depth across all those loci per sample set. This usually shows that loci with low completeness scores in one of both sample sets may be due to low read depth (and thus missed by undersampling during sequencing) in that sample set.  
