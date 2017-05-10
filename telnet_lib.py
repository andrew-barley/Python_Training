#!/usr/bin/env python
import time
import telnetlib
import socket
import sys

from tlogin import tlogin


TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")

def send_command(remote_con, cmd):
    cmd = cmd.rstrip()
    remote_con.write(cmd + '\n')
    time.sleep(1)
    return remote_con.read_very_eager()

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_con = telnet_connect(ip_addr)
    output = tlogin(remote_con, username, password)
    output = send_command(remote_con, "terminal length 0")
    output = send_command(remote_con, "show version")
    print output
    remote_con.close()
if __name__ == "__main__":
    main()
