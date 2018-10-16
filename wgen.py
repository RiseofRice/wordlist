import os
import sys
import time
import string
import argparse
import itertools


min_lenght = 8
max_lenght = 8

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!§$%&/()=?*+#-_.:,;"
output = "output/wordlist.txt"

chrs = lower + digits + special

def create_wordlist(chrs, min_lenght, max_lenght, output):
     
    if min_lenght > max_lenght:
       print("max_lenght needs to be greater than min_lenght")

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print('[+] Creating wordlist at `%s`...' % output)
    print('[i] Starting time: %s' % time.strftime('%H:%M:%S'))
    output = open(output, "w")
    for n in range(min_lenght, max_lenght+1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()
    output.close()
    
    
    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))


create_wordlist(chrs, min_lenght, max_lenght, output)
