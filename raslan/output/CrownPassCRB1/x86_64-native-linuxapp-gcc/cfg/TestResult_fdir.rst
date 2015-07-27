.. <COPYRIGHT_TAG>


==============================================
Testing of 82599 Flow Director Support in DPDK
==============================================


Description
===========

This document provides the plan for testing the Flow Director (FDir) feature of
the Intel 82599 10GbE Ethernet Controller. FDir allows an application to add
filters that identify specific flows (or sets of flows), by examining the VLAN
header, IP addresses, port numbers, protocol type (IPv4/IPv6, UDP/TCP, SCTP), or
a two-byte tuple within the first 64 bytes of the packet.

There are two types of filters:

1. Perfect match filters, where there must be a match between the fields of
   received packets and the programmed filters.
2. Signature filters, where there must be a match between a hash-based signature
   if the fields in the received packet.

There is also support for global masks that affect all filters by masking out
some fields, or parts of fields from the matching process.

Within DPDK, the FDir feature can be configured through the API in the
lib_ethdev library, and this API is used by the ``testpmd`` application.

Note that RSS features can not be enabled at the same time as FDir.



Test Case: test_fdir_filter_masks
-----------------------------------

Result: FAIL

Test Case: test_fdir_flexbytes_filtering
------------------------------------------

Result: FAIL

Test Case: test_fdir_matching
-------------------------------

Result: FAIL

Test Case: test_fdir_perfect_matching
---------------------------------------

Result: FAIL

Test Case: test_fdir_signatures
---------------------------------

Result: FAIL

Test Case: test_fdir_space
----------------------------

Result: FAIL

Test Case: test_fdir_vlanfiltering
------------------------------------

Result: FAIL
