# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "%s to %s copy" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#indata = (open(from_file)).read()

print "input file %d bytes" % len(indata)

print "output file exists? %r" % exists(to_file)
print "ready! continue(enter), cancel(CTRL-C)"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "finish"

out_file.close()
in_file.close()

