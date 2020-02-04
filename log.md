# Network Log

### Private Network: My House
#### Exploration 1
_______________________________________

IP Address: `192.168.0.26`

Subnet Mask: `255.255.255.0`

Router: `192.168.0.1`

DNS: `209.18.47.63` & `209.18.47.62`

______________________________________

Full Routing Table: `netstat -r`


_____________________________________

Other hosts on the same network: `arp -a`


______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.29`

2. Default router: `192.168.0.1`

3. One of the DNS: `209.18.47.63`

4. `www.lmu.edu`

5. `dondi.lmu.build`

___________________________________

traceroute:

1. Host discovered by *arp*: `192.168.0.29`

2. Default router: `192.168.0.1`

3. One of the DNS: `209.18.47.63`

4. `www.lmu.edu`

5. `dondi.lmu.build`

_____________________________

dig:

1. `www.lmu.edu`

2. `dondi.lmu.build`

______________________________

nmap:

1. `www.lmu.edu`

2. `dondi.lmu.build`

3. A stop discovered by traceroute: `72.129.17.152`
