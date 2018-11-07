# encoding: utf8
from optparse import OptionParser

parser = OptionParser()



parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")
args = ["-f", "foo.txt"]
(options, args) = parser.parse_args(args)
print options.filename