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

=======================
Ip_pipeline application
=======================

The ``ip_pipeline application`` is the main DPDK Packet Framework (PFW)
application.

The application allows setting of a pipeline through the PFW. Currently the
application set a pipeline using 2 main features, routing and flow control
and, in addition, ARP is used.

The application has an interactive session when started to allow in-app
configuration.

This application uses 5 CPU cores, reception, flow control, routing and
transmission.

The traffic will pass through the pipeline if meets the following conditions:

  - If ``flow add all`` is used in the setup then:

    - TCP/IPv4
    - IP destination = A.B.C.D with A = 0 and B,C,D random
    - IP source = 0.0.0.0
    - TCP destination port = 0
    - TCP source port = 0

  - If ``flow add all`` is not used then there is no restrictions.

