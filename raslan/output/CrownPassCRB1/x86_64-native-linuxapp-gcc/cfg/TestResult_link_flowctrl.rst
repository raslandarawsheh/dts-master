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

=====================================================================
Support of Ethernet Link Flow Control Features by Poll Mode Drivers
=====================================================================

The support of Ethernet link flow control features by Poll Mode Drivers 
consists in:

- At the receive side, if packet buffer is not enough, NIC will send out the 
  pause frame to peer and ask the peer to slow down the Ethernet frame #
  transmission.

- At the transmit side, if pause frame is received, NIC will slow down the 
  Ethernet frame transmission according to the pause frame.

MAC Control Frame Forwarding consists in:

- Control frames (PAUSE Frames) are taken by the NIC and do not pass to the 
  host.
  
- When Flow Control and MAC Control Frame Forwarding are enabled the PAUSE
  frames will be passed to the host and can be handled by testpmd.

Note: Priority flow control is not included in this test plan.

Note: the high_water, low_water, pause_time, send_xon are configured into the
NIC register. It is not necessary to validate the accuracy of these parameters.
And what change it can cause. The port_id is used to indicate the NIC to be 
configured. In certain case, a system can contain multiple NIC. However the NIC 
need not be configured multiple times. 



Test Case: test_flowctrl_off_pause_fwd_off
--------------------------------------------

Test Case: test_flowctrl_off_pause_fwd_on
-------------------------------------------

Test Case: test_flowctrl_on_pause_fwd_off
-------------------------------------------

Test Case: test_flowctrl_on_pause_fwd_on
------------------------------------------
