# DHCPCap
Provide customers using DHCP with a "screenshot" of their network at the time of a vulnerability assessment. 

This tool uses the Scapy (2.4.5) library to query devices MAC Addresses from their logical addresses via ARP requests. 
Since MAC addresses don't change, customers using dynamic addressing methods can cross-reference their results and their report from
DHCPCap to accurately find their vulnerabilities. 
