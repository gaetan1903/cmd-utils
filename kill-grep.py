#!/usr/bin/python 
 
import os, re

v = os.popen("ps -eo pid,command |grep " + sys.argv[]).read().split("\n")

for u in v:
    uu = re.findall(r"[0-9]{3,}", u)
    if len(uu) > 0:
        os.system("kill -9 " + uu[0])
        print("processus :" + u + " x")