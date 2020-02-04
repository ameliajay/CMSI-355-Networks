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

![Home 1 table](https://user-images.githubusercontent.com/31746937/73716756-c9bb7600-46cc-11ea-9537-14130e026211.png)

_____________________________________

Other hosts on the same network: `arp -a`

![Home 1 arp](https://user-images.githubusercontent.com/31746937/73717100-af35cc80-46cd-11ea-8438-139f603d2abc.png)

______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.29`

![Home 1 ping host](https://user-images.githubusercontent.com/31746937/73717341-62062a80-46ce-11ea-8a39-6b9c117457fb.png)


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

____________________________________

#### Exploration 2
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
