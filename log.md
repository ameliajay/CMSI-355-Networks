# Network Log
## Amelia Jay

*For this assignment I explored networks at my house, a cafe near my house, and LMU.*

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

I found it interesting that this time around my IP Address changed, but all the other values above stayed the same.
______________________________________

Full Routing Table: `netstat -r`

![Home 2 table](https://user-images.githubusercontent.com/31746937/73718547-afd06200-46d1-11ea-82f6-4855f2340bbd.png)

_____________________________________

Other hosts on the same network: `arp -a`

![Home 2 arp](https://user-images.githubusercontent.com/31746937/73718566-b9f26080-46d1-11ea-8468-61060959e504.png)

There were more hosts on during my first exploration. I wonder if this is because for this second exploration I did it in the morning so less of my roommates had been on our WiFi that day.
______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.9`

![Home 2 ping host](https://user-images.githubusercontent.com/31746937/73718583-c7a7e600-46d1-11ea-88c4-ec3e70885a07.png)

I found it interesting that for both explorations, it only took one hop to get to the host discovered by `arp` when I ran `traceroute`. When I performed this command at other locations (LMU and Playa Provisions), this wasn't always the case.

2. Default router: `192.168.0.1`

![Home 2 ping router](https://user-images.githubusercontent.com/31746937/73718598-d393a800-46d1-11ea-9373-a477bb7e9787.png)

3. One of the DNS: `209.18.47.63`

![Home 2 ping DNS](https://user-images.githubusercontent.com/31746937/73718606-dee6d380-46d1-11ea-8b63-0485f48b83aa.png)

4. `www.lmu.edu`

![Home 2 ping lmu](https://user-images.githubusercontent.com/31746937/73718615-e6a67800-46d1-11ea-9acf-82e090d70b12.png)

5. `dondi.lmu.build`

![Home 2 ping dondi](https://user-images.githubusercontent.com/31746937/73718651-00e05600-46d2-11ea-8c7c-60e2a7e8d82d.png)

The first time when I used `ping`, there was a 12.5% packet loss when I tried to communicate with `dondi.lmu.build`, but this time there was only a 8.5% packet loss. The rest of the pings all had a 0.0% packet loss though, which was interesting to see.
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

This `traceroute` worked, but I found that a majority of them timed out, or just took a very long time. I would see this, `***`, and after a few lines of it I would quit running the command because it had already been going for quite a while.
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

There were only two ports open for `www.lmu.edu` both times I did this exploration from home. These were `http` and `https`, as we can see in the screenshot.

2. `dondi.lmu.build`

![Home 2 nmap dondi](https://user-images.githubusercontent.com/31746937/73718832-74826300-46d2-11ea-9e21-6baf72761df3.png)

The first time I ran `nmap` it took a very long time so I quit out of it. The second time I tried this it gave me the message you can see above. This was interesting to see because it said it was blocking the ping probes.

3. A stop discovered by traceroute: `99.82.176.54`

![Home 2 nmap stop](https://user-images.githubusercontent.com/31746937/73718852-8237e880-46d2-11ea-9b4f-f3be7cbdcecf.png)
![Home 2 nmap stop pt2](https://user-images.githubusercontent.com/31746937/73718861-89f78d00-46d2-11ea-85fc-5b74b5115b5c.png)

This stop that I found using `traceroute www.lmu.edu` had an extremely large amount of ports open which I thought was noteworthy so I added a couple screenshots of it.

_____________________________

### Public Network: Playa Guest 2.0 (Playa Provisions Cafe in Playa del Rey)
#### Exploration 1
_______________________________________

IP Address: `192.168.0.34`

Subnet Mask: `255.255.255.0`

Router: `192.168.0.1`

DNS: `209.18.47.63` & `209.18.47.61`

It is interesting that the router address is the same as the one for my home network. I liked learning about network address translation in class though, which could be the reason behind these similarities.

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

*Unfortuately the first time I went to this cafe I didn't have `nmap` installed and the installation wasn't working on the WiFi so I didn't get to run this command!*

___________________________

#### Exploration 2
_______________________________________

IP Address: `192.168.0.2`

Subnet Mask: `255.255.255.0`

Router: `192.168.0.1`

DNS: `209.18.47.63` & `209.18.47.61`

______________________________________

Full Routing Table: `netstat -r`

![Playa Guest 2 table](https://user-images.githubusercontent.com/31746937/73801038-566a4080-476e-11ea-9565-08dc8c19311b.png)

_____________________________________

Other hosts on the same network: `arp -a`

![Playa Guest 2 arp](https://user-images.githubusercontent.com/31746937/73801066-5e29e500-476e-11ea-9951-7b1b05518a58.png)

______________________________________

ping:

1. Host discovered by *arp*: `192.168.0.6`

![Playa Guest 2 ping host](https://user-images.githubusercontent.com/31746937/73801185-7a2d8680-476e-11ea-91fd-678b9e804fa5.png)

2. Default router: `192.168.0.1`

![Playa Guest 2 ping router](https://user-images.githubusercontent.com/31746937/73801204-8ca7c000-476e-11ea-92b7-e5c4c52d27ba.png)

3. One of the DNS: `209.18.47.63`

![Playa Guest 2 ping DNS](https://user-images.githubusercontent.com/31746937/73801222-9cbf9f80-476e-11ea-995f-299cc569fe31.png)

4. `www.lmu.edu`

![Playa Guest 2 ping lmu](https://user-images.githubusercontent.com/31746937/73801245-b660e700-476e-11ea-8b15-efa1d0e29f2f.png)

5. `dondi.lmu.build`

![Playa Guest 2 ping dondi](https://user-images.githubusercontent.com/31746937/73801268-cc6ea780-476e-11ea-8ecf-23e35bc295a0.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `192.168.0.6`

![Playa Guest 2 traceroute host](https://user-images.githubusercontent.com/31746937/73801281-da242d00-476e-11ea-8ca9-9be76e63db28.png)

2. Default router: `192.168.0.1`

![Playa Guest 2 traceroute router](https://user-images.githubusercontent.com/31746937/73801290-e27c6800-476e-11ea-8134-779d0157f703.png)

3. One of the DNS: `209.18.47.63`

![Playa Guest 2 traceroute DNS](https://user-images.githubusercontent.com/31746937/73801309-ead4a300-476e-11ea-8372-c1c99c3332a3.png)

4. `www.lmu.edu`

![Playa Guest 2 traceroute lmu](https://user-images.githubusercontent.com/31746937/73801325-f3c57480-476e-11ea-8da3-171ae8867942.png)

5. `dondi.lmu.build`

![Playa Guest 2 traceroute dondi](https://user-images.githubusercontent.com/31746937/73801338-fcb64600-476e-11ea-9fb9-557704d58b3f.png)

_____________________________

dig:

1. `www.lmu.edu`

![Playa Guest 2 dig lmu](https://user-images.githubusercontent.com/31746937/73801353-050e8100-476f-11ea-8f3a-92625a685827.png)

2. `dondi.lmu.build`

![Playa Guest 2 dig dondi](https://user-images.githubusercontent.com/31746937/73801364-0c358f00-476f-11ea-8246-0f68b9f47e53.png)

______________________________

nmap:

1. `www.lmu.edu`

![Playa Guest 2 nmap lmu](https://user-images.githubusercontent.com/31746937/73801372-15266080-476f-11ea-8f69-d09eaa021c8f.png)

2. `dondi.lmu.build`

![Playa Guest 2 nmap dondi](https://user-images.githubusercontent.com/31746937/73801389-1f485f00-476f-11ea-97b3-294285c9a756.png)

The above screenshot shows the status updates on the progress of the `nmap` command. It was taking a very long time so I ended up quitting out of it; I wonder if the WiFi wasn't as strong which is why this took longer than it did on other explorations.

3. A stop discovered by traceroute: `142.254.237.45`

![Playa Guest 2 nmap stop](https://user-images.githubusercontent.com/31746937/73801405-2cfde480-476f-11ea-8dd1-ef190d613511.png)

_____________________________

### LMU
#### Exploration 1
_______________________________________

IP Address: `10.27.185.191`

Subnet Mask: `255.255.0.0`

Router: `10.27.0.4`

DNS: `10.0.100.16` & `10.0.100.17`

I think it is significant to note that the subnet mask at LMU is `255.255.0.0` where the subnet mask for the coffee shop I went to and for my home network was `255.255.255.0`.
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

2. Default router: `10.27.0.4`

![LMU 1 ping router](https://user-images.githubusercontent.com/31746937/73721947-430d9580-46da-11ea-8bd3-d402d59e840c.png)

3. One of the DNS: `10.0.100.16`

![LMU 1 ping DNS](https://user-images.githubusercontent.com/31746937/73721973-4d2f9400-46da-11ea-8162-c9ef05c47031.png)

4. `www.lmu.edu`

![LMU 1 ping lmu](https://user-images.githubusercontent.com/31746937/73721992-5882bf80-46da-11ea-8ee8-5df2f7698732.png)

5. `dondi.lmu.build`

![LMU 1 ping dondi](https://user-images.githubusercontent.com/31746937/73722010-620c2780-46da-11ea-9739-a0763b440f42.png)

___________________________________

traceroute:

1. Host discovered by *arp*: `10.27.200.253`

![LMU 1 traceroute host](https://user-images.githubusercontent.com/31746937/73722137-ad263a80-46da-11ea-927c-82993c652415.png)

2. Default router: `10.27.0.4`

![LMU 1 traceroute router](https://user-images.githubusercontent.com/31746937/73722145-b57e7580-46da-11ea-8ac3-d18e45dcd45b.png)

3. One of the DNS: `10.0.100.16`

![LMU 1 traceroute DNS](https://user-images.githubusercontent.com/31746937/73722163-bfa07400-46da-11ea-8689-983fb559fdd8.png)

4. `www.lmu.edu`

![LMU 1 traceroute lmu](https://user-images.githubusercontent.com/31746937/73722181-c8914580-46da-11ea-9049-bae1f88782da.png)

Doing `traceroute www.lmu.edu` on LMU's network took a lot more hops than on the other networks. I believe this is because the pathway to reach it changes when you are trying to access it internally (from the WiFi on LMU's campus).

5. `dondi.lmu.build`

![LMU 1 traceroute dondi](https://user-images.githubusercontent.com/31746937/73722209-d34bda80-46da-11ea-8a5d-f0d14821e077.png)

_____________________________

dig:

1. `www.lmu.edu`

![LMU 1 dig lmu](https://user-images.githubusercontent.com/31746937/73722226-de066f80-46da-11ea-9a71-4cebe69bd530.png)

2. `dondi.lmu.build`

![LMU 1 dig dondi](https://user-images.githubusercontent.com/31746937/73722248-e8c10480-46da-11ea-8e6f-63f521ab2bc4.png)
![LMU 1 dig dondi pt2](https://user-images.githubusercontent.com/31746937/73722260-efe81280-46da-11ea-86ff-a1a1deb260d9.png)

This response was a lot longer than usual. I believe this was because `dondi.lmu.build` started to get suspicious of my actions (like all of the pinging) and thought that I was a bot. The `AUTHORITY SECTION` and `ADDITIONAL SECTION` were both very long, especially compared to the results of the `dig` command in other explorations.

______________________________

nmap:

1. `www.lmu.edu`

![LMU 1 nmap lmu](https://user-images.githubusercontent.com/31746937/73722276-ff675b80-46da-11ea-91f9-6af51c74b236.png)

2. `dondi.lmu.build`

![LMU 1 nmap dondi](https://user-images.githubusercontent.com/31746937/73722314-0db57780-46db-11ea-85bc-c91451760c9d.png)
![LMU 1 nmap dondi pt2](https://user-images.githubusercontent.com/31746937/73722327-15751c00-46db-11ea-9e14-cd2b4a715cdb.png)

3. A stop discovered by traceroute: `10.8.255.1`

![LMU 1 nmap stop](https://user-images.githubusercontent.com/31746937/73722336-1d34c080-46db-11ea-9085-c7df2d73cf8a.png)

I tried a lot of different stops to ping (including `10.8.255.1`) and all of them gave me the same response: the host seems down but it might be up blocking ping probes.

____________________________________

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

1. Host discovered by *arp*: `224.0.0.251`

![LMU 2 ping host](https://user-images.githubusercontent.com/31746937/73799754-b1e6ff00-476b-11ea-85ab-e98404b6fda6.png)

2. Default router: `10.27.0.4`

![LMU 2 ping router](https://user-images.githubusercontent.com/31746937/73799782-c2977500-476b-11ea-8887-42da3a6e3ea7.png)

3. One of the DNS: `10.0.100.16`

![LMU 2 ping DNS](https://user-images.githubusercontent.com/31746937/73799796-ce833700-476b-11ea-9a22-a23e7e0375b9.png)

4. `www.lmu.edu`

![LMU 2 ping lmu](https://user-images.githubusercontent.com/31746937/73799809-d93dcc00-476b-11ea-8761-a0170db651a8.png)

5. `dondi.lmu.build`

![LMU 2 ping dondi blocked](https://user-images.githubusercontent.com/31746937/73799824-e35fca80-476b-11ea-8b14-6991a8fbae78.png)
![LMU 2 ping dondi](https://user-images.githubusercontent.com/31746937/73799838-ea86d880-476b-11ea-86c5-f014b86548b7.png)

The first screenshot here shows my request timing out multiple times. I was confused by this so I went to the website on my browser and it told me I had been blocked for security reasons and I had to verify that I was not a bot. It was actually pretty funny! I then tried the command again once I had verified that I wasn't a bot and it worked perfectly fine.

___________________________________

traceroute:

1. Host discovered by *arp*: `224.0.0.251`

![LMU 2 traceroute host](https://user-images.githubusercontent.com/31746937/73799942-389bdc00-476c-11ea-8348-5322d199c8a0.png)

This was interesting because the `ping` worked with this address really well with 0.0% packet loss, but nothing it traceroute seemed to show up/load and instead I was shown 12 lines of `***` before I quit out of the command.

2. Default router: `10.27.0.4`

![LMU 2 traceroute router](https://user-images.githubusercontent.com/31746937/73800166-c4156d00-476c-11ea-891f-f8cf1c0ba235.png)

3. One of the DNS: `10.0.100.16`

![LMU 2 traceroute DNS](https://user-images.githubusercontent.com/31746937/73800179-d0012f00-476c-11ea-929d-d433d12ff5ec.png)

4. `www.lmu.edu`

![LMU 2 traceroute lmu](https://user-images.githubusercontent.com/31746937/73800203-dbecf100-476c-11ea-9e14-e1afd5630e11.png)

5. `dondi.lmu.build`

![LMU 2 traceroute dondi](https://user-images.githubusercontent.com/31746937/73800219-e4ddc280-476c-11ea-8639-0aee80b06e68.png)

_____________________________

dig:

1. `www.lmu.edu`

![LMU 2 dig lmu](https://user-images.githubusercontent.com/31746937/73800255-00e16400-476d-11ea-94ce-2d3ee05552b7.png)

2. `dondi.lmu.build`

![LMU 2 dig dondi](https://user-images.githubusercontent.com/31746937/73800266-0c348f80-476d-11ea-9c2e-e78e3143fa58.png)

______________________________

nmap:

1. `www.lmu.edu`

![LMU 2 nmap lmu](https://user-images.githubusercontent.com/31746937/73800335-3f771e80-476d-11ea-826d-abc47d7d3f63.png)

This is interesting to me because when on LMU's network, you can see a lot more ports listed than from the other explorations, but still only two are open (`http` and `https`).

2. `dondi.lmu.build`

![LMU 2 nmap dondi](https://user-images.githubusercontent.com/31746937/73800371-4aca4a00-476d-11ea-9dcb-d6a151bbf943.png)

3. A stop discovered by traceroute: `157.242.254.82`

![LMU 2 nmap stop](https://user-images.githubusercontent.com/31746937/73800382-53bb1b80-476d-11ea-8ee0-8cb0af0de732.png)

____________________________________

