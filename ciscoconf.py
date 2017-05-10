#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():
    #define file as var that cisco conf parse can read
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    #find crypto maps in cisco_cfg and define as variable
    crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    #find all the crypto maps and print them
    for crypto_map in crypto:
        print crypto_map.text
        #find the children and print them for each crypto map found
        for child in crypto_map.all_children:
            print child.text

if __name__ == "__main__":
    main()
