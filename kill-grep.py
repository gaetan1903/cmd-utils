#!/usr/bin/python

import os, re, sys

v = os.popen("ps -eo pid,command |grep -v grep|grep " + sys.argv[1]).read().split("\n")

print len(v)-1, "processus trouvee"
print
print
for u in v:
    uu = re.findall(r"[0-9]{3,}", u)
    if len(uu) > 0 and str(os.getpid()) != uu[0]:
        if os.system("kill -9 " + uu[0]+ " > /dev/null") == 0:
            print "processus :" + u + " arreter"
            print
