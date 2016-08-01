#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import time



if os.geteuid() != 0: # Comprueba privilegios root
    print "You must be root to change the MAC address\n"
    sys.exit(1)


def macchanger():
   '''Returns a random MAC''' 
   # El primer octeto debe ser par 
   MAC = random.choice('0123456789ABCDEF') + random.choice('02468ACE') + ':'
   for i in xrange(5):
      MAC += ''.join(random.choice('0123456789ABCDEF')  for n in xrange(2)) + ':'
   return MAC[:-1]

def whichEth():
    '''Returns the interface to change the MAC to'''
    # show interfaces list
    cmd = "ifconfig | grep Ethernet | awk '{print  $5, $1}'"
    os.system(cmd)
    return raw_input("Which interface do you want to change the MAC address to?\n")
    
eth = whichEth()
mac = macchanger()
cmd = []
cmd.append( "ifconfig %s down" % eth )
cmd.append( "ifconfig %s hw ether %s " % ( eth, mac) )
cmd.append( "ifconfig %s up" % eth )
print "Running:\n" 
for command in cmd:
    os.system(command)
    time.sleep(3)

