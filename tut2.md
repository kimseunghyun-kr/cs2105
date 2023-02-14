1a) http://index.html HTTP/1.1 1b) 1.1 1c) persistent, connection : keep-alive 1d) not possible to get ip

2a) yes -> 200ok response 2b) Wed, 23 Jan 2019 13:50:31 GMT 2c) 606 bytes 2d) yes

3a) False, you can only download 1 object per request.
3b) true 
3c) false 3d) false -> 204

4

non persistent. each object need call sysack 

Rtt 1 trip = Sum(Ddns) + Dweb = nDdns + Dweb
Rtt m trips = nDdns + 2(m+1)Dweb

5a)
n = 3
m = 5
3Ddns + 2(5 + 1)Dweb

5b)
3Ddns + 2Dweb -> (sysack html and get html) + 2Dweb(sysack 5 obj + get 5 obj)

5c)
3Dns + 2Dweb{this is for the html and 5 object} + Dweb{this is for the sysack}

6
DNS cache poisoning is the act of entering false information into a DNS cache, so that DNS queries return an incorrect response and users are directed to the wrong websites.

irl example
```
A famous example of this type of attack happened in 2018 when hackers compromised Amazon's Route 53 DNS server and public Google DNS servers. After gaining access, they rerouted roughly 1,300 IP addresses to malicious phishing websites designed to steal user information.
```

8
1. 200 ok
2. not mentioned. only responded with Etag