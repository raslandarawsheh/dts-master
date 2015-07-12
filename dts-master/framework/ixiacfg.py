"""
ixiaPorts Structure

IxiaGroup: {
Version : IXIA TCL server version
IP      : IXIA server IP address
Ports   : [IXIA port list]
},

IxiaGroup: {
Version : IXIA TCL server version
IP      : IXIA server IP address
Ports   : [IXIA ports list]
}
"""
# IXIA configure file
ixiaPorts = {
    'Group1': {"Version": "6.62",
               "IP": "10.239.128.121",
               "Ports": [
                   {"card": 4, "port": 5},
                   {"card": 4, "port": 6},
                   {"card": 4, "port": 7},
                   {"card": 4, "port": 8}
               ]
               }

}
