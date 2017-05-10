#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():
    #define file as var that cisco conf parse can read
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    #find all parents that start with crypto map CRYPTO and the child of set pfs group2 and define them as a var to print
    pfs2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r'set pfs group2')

    #print description of what's to come
    print "\nAll cryptomaps that use PFS2"    

    #print each instance of cryptomap with pfs2
    for i in pfs2:
        print ' {0}'.format(i.text)

if __name__ == "__main__":
    main()
