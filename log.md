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

![Home 1 dig lmu](https://user-images.githubusercontent.com/31746937/73717827-b5c54380-46cf-11ea-97cf-29f73b66824a.png)

2. `dondi.lmu.build`

![Home 1 dig dondi](https://user-images.githubusercontent.com/31746937/73717837-beb61500-46cf-11ea-81a0-854aa2f4b12b.png)

______________________________

nmap:

1. `www.lmu.edu`

![Home 1 nmap lmu ](https://user-images.githubusercontent.com/31746937/73717885-db524d00-46cf-11ea-9139-aba32d452ed1.png)

2. `dondi.lmu.build`

![Home 1 nmap dondi](https://user-images.githubusercontent.com/31746937/73717902-e7d6a580-46cf-11ea-8b6f-e64505883c10.png)

3. A stop discovered by traceroute: `72.129.17.152`

![Home 1 nmap stop](https://user-images.githubusercontent.com/31746937/73717922-f45afe00-46cf-11ea-856f-a4da5efc46a6.png)

____________________________________

#### Exploration 2
_______________________________________

IP Address: `192.168.0.6`

Subnet Mask: `255.255.255.0`

Router: `192.168.0.1`

DNS: `209.18.47.63` & `209.18.47.62`

______________________________________

Full Routing Table: `netstat -r`

![Home 2 table](https://user-images.githubusercontent.com/31746937/73718547-afd06200-46d1-11ea-82f6-4855f2340bbd.png)

_____________________________________

Other hosts on the same network: `arp -a`

![Home 2 arp](https://user-images.githubusercontent.com/31746937/73718566-b9f26080-46d1-11ea-8468-61060959e504.png)

______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.9`

![Home 2 ping host](https://user-images.githubusercontent.com/31746937/73718583-c7a7e600-46d1-11ea-88c4-ec3e70885a07.png)

2. Default router: `192.168.0.1`

![Home 2 ping router](https://user-images.githubusercontent.com/31746937/73718598-d393a800-46d1-11ea-9373-a477bb7e9787.png)

3. One of the DNS: `209.18.47.63`

![Home 2 ping DNS](https://user-images.githubusercontent.com/31746937/73718606-dee6d380-46d1-11ea-8b63-0485f48b83aa.png)

4. `www.lmu.edu`

![Home 2 ping lmu](https://user-images.githubusercontent.com/31746937/73718615-e6a67800-46d1-11ea-9acf-82e090d70b12.png)

5. `dondi.lmu.build`

![Home 2 ping dondi](https://user-images.githubusercontent.com/31746937/73718651-00e05600-46d2-11ea-8c7c-60e2a7e8d82d.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `192.168.0.9`

![Home 2 traceroute host](https://user-images.githubusercontent.com/31746937/73718696-1eadbb00-46d2-11ea-96a3-934f0ac7db1b.png)

2. Default router: `192.168.0.1`

![Home 2 traceroute router](https://user-images.githubusercontent.com/31746937/73718711-2705f600-46d2-11ea-87b6-8c848ea83830.png)

3. One of the DNS: `209.18.47.63`

![Home 2 traceroute DNS](https://user-images.githubusercontent.com/31746937/73718730-32f1b800-46d2-11ea-9564-b28a1cce1af4.png)

4. `www.lmu.edu`

![Home 2 traceroute lmu](https://user-images.githubusercontent.com/31746937/73718748-3c7b2000-46d2-11ea-8d6b-8f35951c1dd8.png)

5. `dondi.lmu.build`

![Home 2 traceroute dondi](https://user-images.githubusercontent.com/31746937/73718758-47ce4b80-46d2-11ea-8423-54f76d4ea59b.png)

_____________________________

dig:

1. `www.lmu.edu`

![Home 2 dig lmu](https://user-images.githubusercontent.com/31746937/73718799-53ba0d80-46d2-11ea-8a17-6efcf02da7d3.png)

2. `dondi.lmu.build`

![Home 2 dig dondi](https://user-images.githubusercontent.com/31746937/73718808-5f0d3900-46d2-11ea-938e-c9be0a7e3abb.png)

______________________________

nmap:

1. `www.lmu.edu`

![Home 2 nmap lmu](https://user-images.githubusercontent.com/31746937/73718824-69c7ce00-46d2-11ea-8204-007966e41346.png)

2. `dondi.lmu.build`

![Home 2 nmap dondi](https://user-images.githubusercontent.com/31746937/73718832-74826300-46d2-11ea-9e21-6baf72761df3.png)

3. A stop discovered by traceroute: `99.82.176.54`

![Home 2 nmap stop](https://user-images.githubusercontent.com/31746937/73718852-8237e880-46d2-11ea-9b4f-f3be7cbdcecf.png)
![Home 2 nmap stop pt2](https://user-images.githubusercontent.com/31746937/73718861-89f78d00-46d2-11ea-85fc-5b74b5115b5c.png)

_____________________________

### Public Network: Playa Provisions (Cafe in Playa del Rey)
#### Exploration 1
_______________________________________

IP Address: `192.168.0.34`

Subnet Mask: `255.255.255.0`

Router: `192.168.0.1`

DNS: `209.18.47.63` & `209.18.47.61`

______________________________________

Full Routing Table: `netstat -r`

![Playa Guest 1 table](https://user-images.githubusercontent.com/31746937/73720663-566b3180-46d7-11ea-8e13-6149e30f4f0f.png)

_____________________________________

Other hosts on the same network: `arp -a`

![Playa Guest 1 arp](https://user-images.githubusercontent.com/31746937/73720702-6551e400-46d7-11ea-86d6-56a49931663e.png)

______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.37`

![Playa Guest 1 ping host](https://user-images.githubusercontent.com/31746937/73720731-7864b400-46d7-11ea-8245-4c3bba7b560d.png)

2. Default router: `192.168.0.1`

![Playa Guest 1 ping router](https://user-images.githubusercontent.com/31746937/73720743-84507600-46d7-11ea-9bc8-52cafa3f0d78.png)

3. One of the DNS: `209.18.47.63`

![Playa Guest 1 ping DNS](https://user-images.githubusercontent.com/31746937/73720761-8dd9de00-46d7-11ea-8a81-11a8796112ef.png)

4. `www.lmu.edu`

![Playa Guest 1 ping lmu](https://user-images.githubusercontent.com/31746937/73720773-9a5e3680-46d7-11ea-8250-83c22c189e25.png)

5. `dondi.lmu.build`

![Playa Guest 1 ping dondi](https://user-images.githubusercontent.com/31746937/73720782-a3e79e80-46d7-11ea-822d-88c98ba77f82.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `192.168.0.37`

![Playa Guest 1 traceroute host](https://user-images.githubusercontent.com/31746937/73720868-d4c7d380-46d7-11ea-98e2-e714069340f1.png)

2. Default router: `192.168.0.1`

![Playa Guest 1 traceroute router](https://user-images.githubusercontent.com/31746937/73720884-de513b80-46d7-11ea-8be6-313a13789a3a.png)

3. One of the DNS: `209.18.47.63`

![Playa Guest 1 traceroute DNS](https://user-images.githubusercontent.com/31746937/73720896-e610e000-46d7-11ea-9fe1-3a7958520bef.png)

4. `www.lmu.edu`

![Playa Guest 1 traceroute lmu](https://user-images.githubusercontent.com/31746937/73720915-f032de80-46d7-11ea-9efe-9a5f733d21b8.png)

5. `dondi.lmu.build`

![Playa Guest 1 traceroute dondi](https://user-images.githubusercontent.com/31746937/73720936-f923b000-46d7-11ea-811c-df6250bf2ce7.png)

_____________________________

dig:

1. `www.lmu.edu`

![Playa Guest 1 dig lmu](https://user-images.githubusercontent.com/31746937/73720982-0f317080-46d8-11ea-8338-06e5dfbc6b9a.png)

2. `dondi.lmu.build`

![Playa Guest 1 dig dondi](https://user-images.githubusercontent.com/31746937/73721003-18224200-46d8-11ea-918c-b4e8962b1748.png)

______________________________

nmap:

*Unfortuately the first time I went to this cafe I didn't have `nmap` installed so I didn't get to run this command!*

___________________________

### LMU
#### Exploration 2
_______________________________________

IP Address: `10.27.185.191`

Subnet Mask: `255.255.0.0`

Router: `10.27.0.4`

DNS: `10.0.100.16` & `10.0.100.17`

______________________________________

Full Routing Table: `netstat -r`

![LMU 2 table](https://user-images.githubusercontent.com/31746937/73799732-9e3b9880-476b-11ea-84dd-6969e2be22c7.png)

_____________________________________

Other hosts on the same network: `arp -a`

![LMU 2 arp](https://user-images.githubusercontent.com/31746937/73799739-a8f62d80-476b-11ea-938a-b07a6d422958.png)

______________________________________

ping:

1. Host discovered by *arp*: `10.27.200.253`

![LMU 2 ping host](https://user-images.githubusercontent.com/31746937/73799754-b1e6ff00-476b-11ea-85ab-e98404b6fda6.png)

2. Default router: `192.168.0.1`

![LMU 2 ping router](https://user-images.githubusercontent.com/31746937/73799782-c2977500-476b-11ea-8887-42da3a6e3ea7.png)

3. One of the DNS: `209.18.47.63`

![LMU 2 ping DNS](https://user-images.githubusercontent.com/31746937/73799796-ce833700-476b-11ea-9a22-a23e7e0375b9.png)

4. `www.lmu.edu`

![LMU 2 ping lmu](https://user-images.githubusercontent.com/31746937/73799809-d93dcc00-476b-11ea-8761-a0170db651a8.png)

5. `dondi.lmu.build`

![LMU 2 ping dondi blocked](https://user-images.githubusercontent.com/31746937/73799824-e35fca80-476b-11ea-8b14-6991a8fbae78.png)
![LMU 2 ping dondi](https://user-images.githubusercontent.com/31746937/73799838-ea86d880-476b-11ea-86c5-f014b86548b7.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `10.27.200.253`

![LMU 1 traceroute host](https://user-images.githubusercontent.com/31746937/73722137-ad263a80-46da-11ea-927c-82993c652415.png)

2. Default router: `192.168.0.1`

![LMU 1 traceroute router](https://user-images.githubusercontent.com/31746937/73722145-b57e7580-46da-11ea-8ac3-d18e45dcd45b.png)

3. One of the DNS: `209.18.47.63`

![LMU 1 traceroute DNS](https://user-images.githubusercontent.com/31746937/73722163-bfa07400-46da-11ea-8689-983fb559fdd8.png)

4. `www.lmu.edu`

![LMU 1 traceroute lmu](https://user-images.githubusercontent.com/31746937/73722181-c8914580-46da-11ea-9049-bae1f88782da.png)

5. `dondi.lmu.build`

![LMU 1 traceroute dondi](https://user-images.githubusercontent.com/31746937/73722209-d34bda80-46da-11ea-8a5d-f0d14821e077.png)

_____________________________

dig:

1. `www.lmu.edu`

![LMU 1 dig lmu](https://user-images.githubusercontent.com/31746937/73722226-de066f80-46da-11ea-9a71-4cebe69bd530.png)

2. `dondi.lmu.build`

![LMU 1 dig dondi](https://user-images.githubusercontent.com/31746937/73722248-e8c10480-46da-11ea-8e6f-63f521ab2bc4.png)
![LMU 1 dig dondi pt2](https://user-images.githubusercontent.com/31746937/73722260-efe81280-46da-11ea-86ff-a1a1deb260d9.png)

______________________________

nmap:

1. `www.lmu.edu`

![LMU 1 nmap lmu](https://user-images.githubusercontent.com/31746937/73722276-ff675b80-46da-11ea-91f9-6af51c74b236.png)

2. `dondi.lmu.build`

![LMU 1 nmap dondi](https://user-images.githubusercontent.com/31746937/73722314-0db57780-46db-11ea-85bc-c91451760c9d.png)
![LMU 1 nmap dondi pt2](https://user-images.githubusercontent.com/31746937/73722327-15751c00-46db-11ea-9e14-cd2b4a715cdb.png)

3. A stop discovered by traceroute: `10.8.255.1`

![LMU 1 nmap stop](https://user-images.githubusercontent.com/31746937/73722336-1d34c080-46db-11ea-9085-c7df2d73cf8a.png)

____________________________________

### LMU
#### Exploration 1
_______________________________________

IP Address: `10.27.185.191`

Subnet Mask: `255.255.0.0`

Router: `10.27.0.4`

DNS: `10.0.100.16` & `10.0.100.17`

______________________________________

Full Routing Table: `netstat -r`

![LMU 1 table](https://user-images.githubusercontent.com/31746937/73721767-ca0e3e00-46d9-11ea-9fc9-5272c8e79aa2.png)

_____________________________________

Other hosts on the same network: `arp -a`

![LMU 1 arp](https://user-images.githubusercontent.com/31746937/73721906-2e310200-46da-11ea-9fca-b609508af33b.png)

______________________________________

ping:

1. Host discovered by *arp*: `10.27.200.253`

![LMU 1 ping host](https://user-images.githubusercontent.com/31746937/73721926-38530080-46da-11ea-94c5-088bac55ba76.png)

2. Default router: `192.168.0.1`

![LMU 1 ping router](https://user-images.githubusercontent.com/31746937/73721947-430d9580-46da-11ea-8bd3-d402d59e840c.png)

3. One of the DNS: `209.18.47.63`

![LMU 1 ping DNS](https://user-images.githubusercontent.com/31746937/73721973-4d2f9400-46da-11ea-8162-c9ef05c47031.png)

4. `www.lmu.edu`

![LMU 1 ping lmu](https://user-images.githubusercontent.com/31746937/73721992-5882bf80-46da-11ea-8ee8-5df2f7698732.png)

5. `dondi.lmu.build`

![LMU 1 ping dondi](https://user-images.githubusercontent.com/31746937/73722010-620c2780-46da-11ea-9739-a0763b440f42.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `10.27.200.253`

![LMU 1 traceroute host](https://user-images.githubusercontent.com/31746937/73722137-ad263a80-46da-11ea-927c-82993c652415.png)

2. Default router: `192.168.0.1`

![LMU 1 traceroute router](https://user-images.githubusercontent.com/31746937/73722145-b57e7580-46da-11ea-8ac3-d18e45dcd45b.png)

3. One of the DNS: `209.18.47.63`

![LMU 1 traceroute DNS](https://user-images.githubusercontent.com/31746937/73722163-bfa07400-46da-11ea-8689-983fb559fdd8.png)

4. `www.lmu.edu`

![LMU 1 traceroute lmu](https://user-images.githubusercontent.com/31746937/73722181-c8914580-46da-11ea-9049-bae1f88782da.png)

5. `dondi.lmu.build`

![LMU 1 traceroute dondi](https://user-images.githubusercontent.com/31746937/73722209-d34bda80-46da-11ea-8a5d-f0d14821e077.png)

_____________________________

dig:

1. `www.lmu.edu`

![LMU 1 dig lmu](https://user-images.githubusercontent.com/31746937/73722226-de066f80-46da-11ea-9a71-4cebe69bd530.png)

2. `dondi.lmu.build`

![LMU 1 dig dondi](https://user-images.githubusercontent.com/31746937/73722248-e8c10480-46da-11ea-8e6f-63f521ab2bc4.png)
![LMU 1 dig dondi pt2](https://user-images.githubusercontent.com/31746937/73722260-efe81280-46da-11ea-86ff-a1a1deb260d9.png)

______________________________

nmap:

1. `www.lmu.edu`

![LMU 1 nmap lmu](https://user-images.githubusercontent.com/31746937/73722276-ff675b80-46da-11ea-91f9-6af51c74b236.png)

2. `dondi.lmu.build`

![LMU 1 nmap dondi](https://user-images.githubusercontent.com/31746937/73722314-0db57780-46db-11ea-85bc-c91451760c9d.png)
![LMU 1 nmap dondi pt2](https://user-images.githubusercontent.com/31746937/73722327-15751c00-46db-11ea-9e14-cd2b4a715cdb.png)

3. A stop discovered by traceroute: `10.8.255.1`

![LMU 1 nmap stop](https://user-images.githubusercontent.com/31746937/73722336-1d34c080-46db-11ea-9085-c7df2d73cf8a.png)

____________________________________

