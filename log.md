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

![Home 1 ping router](https://user-images.githubusercontent.com/31746937/73717522-e9ec3480-46ce-11ea-98bf-331e709cad9d.png)

3. One of the DNS: `209.18.47.63`

![Home 1 ping DNS](https://user-images.githubusercontent.com/31746937/73717538-f96b7d80-46ce-11ea-8518-aea938085748.png)

4. `www.lmu.edu`

![Home 1 ping lmu](https://user-images.githubusercontent.com/31746937/73717557-07210300-46cf-11ea-8758-b7ddd3f82464.png)

5. `dondi.lmu.build`

![Home 1 ping dondi](https://user-images.githubusercontent.com/31746937/73717572-12742e80-46cf-11ea-8dcb-401d06746453.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `192.168.0.29`

![Home 1 traceroute host](https://user-images.githubusercontent.com/31746937/73717657-48b1ae00-46cf-11ea-88ae-cc08a45109f7.png)

2. Default router: `192.168.0.1`

![Home 1 traceroute router](https://user-images.githubusercontent.com/31746937/73717684-5a935100-46cf-11ea-8201-4131f5b8bf69.png)

3. One of the DNS: `209.18.47.63`

![Home 1 traceroute DNS](https://user-images.githubusercontent.com/31746937/73717706-6848d680-46cf-11ea-874e-c1c69266ef87.png)

4. `www.lmu.edu`

![Home 1 traceroute lmu](https://user-images.githubusercontent.com/31746937/73717731-7860b600-46cf-11ea-94ca-2cb07d877ff6.png)

5. `dondi.lmu.build`

![Home 1 traceroute dondi](https://user-images.githubusercontent.com/31746937/73717745-831b4b00-46cf-11ea-8a95-403ea1487477.png)

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
