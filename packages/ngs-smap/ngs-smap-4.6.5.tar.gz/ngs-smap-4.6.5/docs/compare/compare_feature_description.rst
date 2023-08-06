.. raw:: html

    <style> .purple {color:purple} </style>
    <style> .white {color:white} </style>

.. role:: purple
.. role:: white


###################
Feature Description
###################

**SMAP compare** only needs two final BED files containing loci, created with :ref:`SMAP delineate <SMAPdelHIW3>`.

Examples of input BED files are shown below:

| Set1 contains GBS samples of 48 diploid individuals.  
| Set2 contains 16 replicate Pool-Seq GBS samples of those constituent 48 individuals.

.. tabs::

   .. tab:: Set1 BED (individuals)
   
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= ==============
	  Reference     Start  End    MergedCluster_name                  Mean_read_depth   Strand  SMAPs              Completeness   nr_SMAPs  Name
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= ==============
	  scaffold_1    41455  41541  :green:`scaffold_1:41456-41541_+`   :green:`604`      \+      41456,41541        :green:`8`     2         48_individuals
	  scaffold_1    41486  41569  scaffold_1:41487-41569\_\-          579               \-      41487,41569        3              2         48_individuals
	  scaffold_1    42704  42778  scaffold_1:42705-42778_+            61                \+      42705,42778        2              2         48_individuals
	  scaffold_1    42798  42884  scaffold_1:42799-42884\_\-          72                \-      42799,42884        2              2         48_individuals
	  scaffold_1    77857  77943  :red:`scaffold_1:77858-77943_+`     :red:`43`         \+      77858,77943        :red:`3`       2         48_individuals
	  scaffold_1    156606 156692 scaffold_1:156607-156692\_\-        1067              \-      156607,156692      37             2         48_individuals
	  scaffold_12   2530   2596   scaffold_12:2531-2596_+             39                \+      2531,2596          3              2         48_individuals
	  scaffold_12   33659  33725  scaffold_12:33660-33725_+           18                \+      33660,33725        1              2         48_individuals
	  scaffold_12   34732  34806  scaffold_12:34733-34806_+           890               \+      34733,34806        45             2         48_individuals
	  scaffold_12   34732  34806  scaffold_12:34733-34806\_\-         768               \-      34733,34806        47             2         48_individuals
	  scaffold_34   36267  36358  scaffold_34:36268-36358_+           1169              \+      36268,36296,36358  36             3         48_individuals
	  scaffold_34   46267  46334  scaffold_34:46268-46334\_\-         150               \-      46268,46334        48             2         48_individuals
	  scaffold_72   23080  23166  :blue:`scaffold_72:23081-23166\_\-` :blue:`1423`      \-      23081,23156,23166  :blue:`48`     3         48_individuals
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= ==============
	  

   .. tab:: Set2 BED (pools)
   
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= =========
	  Reference     Start  End    MergedCluster_name                  Mean_read_depth   Strand  SMAPs              Completeness   nr_SMAPs  Name
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= =========
	  scaffold_1    41455  41541  :green:`scaffold_1:41456-41541_+`   :green:`42`       \+      41456,41541        :green:`1`     2         16_pools 
	  scaffold_1    41486  41569  scaffold_1:41487-41569\_\-          111               \-      41487,41569        3              2         16_pools 
	  scaffold_1    156606 156692 scaffold_1:156607-156692\_\-        915               \-      156607,156692      16             2         16_pools 
	  scaffold_12   34732  34806  scaffold_12:34733-34806_+           2403              \+      34733,34806        16             2         16_pools 
	  scaffold_12   34732  34806  scaffold_12:34733-34806\_\-         2284              \-      34733,34806        16             2         16_pools 
	  scaffold_34   36267  36358  scaffold_34:36268-36358_+           1242              \+      36268,36296,36358  16             3         16_pools 
	  scaffold_34   46267  46334  scaffold_34:46268-46334\_\-         809               \-      46268,46334        16             2         16_pools 
	  scaffold_72   23080  23166  :blue:`scaffold_72:23081-23166\_\-` :blue:`1882`      \-      23081,23156,23166  :blue:`16`     3         16_pools 
	  ============= ====== ====== =================================== ================= ======= ================== ============== ========= =========
	  