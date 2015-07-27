.. Copyright (c) <2010>, Intel Corporation
   All rights reserved.
   
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions
   are met:
   
   - Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   
   - Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the
     distribution.
   
   - Neither the name of Intel Corporation nor the names of its
     contributors may be used to endorse or promote products derived
     from this software without specific prior written permission.
   
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
   FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
   COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
   HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
   STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
   OF THE POSSIBILITY OF SUCH DAMAGE.

=====================================================
Support of VLAN Offload Features by Poll Mode Drivers
=====================================================

The support of VLAN offload features by Poll Mode Drivers consists in:

- the filtering of received VLAN packets,
- VLAN header stripping by hardware in received [VLAN] packets,
- VLAN header insertion by hardware in transmitted packets.

The filtering of VLAN packets is automatically enabled by the ``testpmd``
application for each port.
By default, the VLAN filter of each port is empty and all received VLAN packets
are dropped by the hardware.
To enable the receipt of VLAN packets tagged with the VLAN tag identifier
``vlan_id`` on the port ``port_id``, the following command of the ``testpmd``
application must be used::
  
  rx_vlan add vlan_id port_id

In the same way, the insertion of a VLAN header with the VLAN tag identifier
``vlan_id`` in packets sent on the port ``port_id`` can be enabled with the
following command of the ``testpmd`` application::
  
  tx_vlan set vlan_id port_id


The transmission of VLAN packets is done with the ``start tx_first`` command
of the ``testpmd`` application that arranges to first send a burst of packets
on all configured ports before starting the ``rxonly`` packet forwarding mode
that has been previously selected.


Test Case: test_vlan_disable_receipt
--------------------------------------

Result: FAIL

Test Case: test_vlan_enable_receipt
-------------------------------------

Result: PASS

Test Case: test_vlan_strip_config_off
---------------------------------------

Result: FAIL

Test Case: test_vlan_strip_config_on
--------------------------------------

Result: FAIL
