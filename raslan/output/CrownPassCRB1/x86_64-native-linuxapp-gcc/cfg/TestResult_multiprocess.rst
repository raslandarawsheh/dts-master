..
  <COPYRIGHT_TAG>

===============================
Multi-process Test Instructions
===============================

Simple MP Application Test
--------------------------

Description
-----------

This test is a basic multi-process test which demonstrates the basics of sharing
information between Intel DPDK processes. The same application binary is run
twice - once as a primary instance, and once as a secondary instance. Messages
are sent from primary to secondary and vice versa, demonstrating the processes
are sharing memory and can communicate using rte_ring structures.


Test Case: test_multiprocess_simple_mpapplicationstartup
----------------------------------------------------------

Result: PASS

Test Case: test_multiprocess_simple_mpbasicoperation
------------------------------------------------------
