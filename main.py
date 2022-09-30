# Written 5/11/22, Python V = 3.9.12, Author = Jordan McGrath

from scapy.layers.l2 import *

import HTMLHelper

pdsts = []  # All Protocol Destinations for searching via ARP
response_data = {}  # Hold all data for generating our HTML Report.

user_input = input("Enter IP Addresses and Subnets (delimiter = ','): ")

for pdst in user_input.split(","):
    pdsts.append(pdst.strip())  # Scapy doesn't appreciate extra spaces

ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Const: This is how we broadcast our request on the network!

for pdst in pdsts:
    try:
        arp = ARP(pdst=pdst)  # Craft an ARP Packet with the IP in question as the protocol destination.

        responses = srp(ether/arp, verbose=0, timeout=3)[0]

        if responses: response_data[pdst] = []

        for response in responses:
            response_data[pdst].append(response[1].psrc + "|" + response[1].hwsrc)  # [1] is necessary as srp() returns a Tuple object containing the orig. query and the answer.

    except KeyboardInterrupt:
        print("Terminated Via Keyboard Input")

filename = input("Name of HTML Report: ")

HTMLHelper.generateHTMLReport(filename, response_data)
