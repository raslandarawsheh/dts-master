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

==========================
PMD RX/TX Checksum Offload
==========================

The support of RX/TX L3/L4 Checksum offload features by Poll Mode Drivers consists in:

On the RX side:
- Verify IPv4 checksum by hardware for received packets.
- Verify UDP/TCP/SCTP checksum by hardware for received packets.

On the TX side:

- IPv4 checksum insertion by hardware in transmitted packets.
- IPv4/UDP checksum insertion by hardware in transmitted packets.
- IPv4/TCP checksum insertion by hardware in transmitted packets.
- IPv4/SCTP checksum insertion by hardware in transmitted packets (sctp 
        length in 4 bytes).
- IPv6/UDP checksum insertion by hardware in transmitted packets.
- IPv6/TCP checksum insertion by hardware in transmitted packets.
- IPv6/SCTP checksum insertion by hardware in transmitted packets (sctp 
        length in 4 bytes).

RX side, the L3/L4 checksum offload by hardware can be enabled with the
following command of the ``testpmd`` application::

   enable-rx-checksum

TX side, the insertion of a L3/L4 checksum by hardware can be enabled with the
following command of the ``testpmd`` application and running in a dedicated
tx checksum mode::

   set fwd csum
   tx_checksum set mask port_id

The transmission of packet is done with the ``start`` command of the ``testpmd`` 
application that will receive packets and then transmit the packet out on all 
configured ports. ``mask`` is used to indicated what hardware checksum
offload is required on the ``port_id``. Please check the NIC datasheet for the 
corrresponding Hardware limits::

      bit 0 - insert ip checksum offload if set 
      bit 1 - insert udp checksum offload if set 
      bit 2 - insert tcp checksum offload if set
      bit 3 - insert sctp checksum offload if set



Test Case: test_checksum_offload_disable
------------------------------------------

Result: FAIL

Test Case: test_checksum_offload_enable
-----------------------------------------

Result: FAIL

Test Case: test_checksum_offload_with_vlan
--------------------------------------------

Result: FAIL
