#!/usr/bin/env python

TELNET_TIMEOUT = 6

def tlogin(remote_con, username, password):
    output = remote_con.read_until("sername:", TELNET_TIMEOUT)
    remote_con.write(username + "\n")
    output = remote_con.read_until("assword:", TELNET_TIMEOUT)
    remote_con.write(password + "\n")
    return output
