.. Copyright (c) <2010,2011>, Intel Corporation
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


=========================================
Support of IEEE1588 Precise Time Protocol
=========================================

The functional test of the IEEE1588 Precise Time Protocol offload support
in Poll Mode Drivers is done with a specific `ieee1588`` forwarding mode
of the ``testpmd`` application.

In this mode, packets are received one by one and are expected to be
PTP V2 L2 Ethernet frames with the specific Ethernet type ``0x88F7``,
containing PTP ``SYNC`` messages (version 2 at offset 1, and message ID
0 at offset 0).

When started, the test enables the IEEE1588 PTP offload support of each
controller. It makes them automatically filter and timestamp the receipt
of incoming PTP ``SYNC`` messages contained in PTP V2 Ethernet frames.
Conversely, when stopped, the test disables the IEEE1588 PTP offload support
of each controller,

While running, the test checks that each received packet is a valid IEEE1588
PTP V2 Ethernet frame with a message of type ``PTP_SYNC_MESSAGE``, and that
the packet has been identified and timestamped by the hardware.
For this purpose, it checks that the corresponding ``PKT_RX_IEEE1588_PTP``
and ``PKT_RX_IEEE1588_TMST`` flags have been set in the mbufs returned
by the PMD receive function.

Then, the test checks that the two NIC registers holding the timestamp of a
received PTP packet are effectively valid, and that they contain a value
greater than their previous value.

If everything is OK, the test sends the received packet as-is on the same port,
requesting for its transmission to be timestamped by the hardware.
For this purpose, it set the ``PKT_TX_IEEE1588_TMST`` flag of the mbuf before
sending it.
The test finally checks that the two NIC registers holding the timestamp of
a transmitted PTP packet are effectively valid, and that they contain a value
greater than their previous value.



Test Case: test_ieee1588_disable
----------------------------------

Result: PASS

Test Case: test_ieee1588_enable
---------------------------------

Result: FAIL
