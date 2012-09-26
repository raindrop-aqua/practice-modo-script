#python

import urllib2

# Standard
lx.out("Hello modo!")

# Concat
lx.out("Python version:", sys.version)
lx.out("abc" + sys.version)

# Dir
lx.out("lx:", dir(lx))
lx.out("sys:", dir(sys))
lx.out("urllib2:", dir(urllib2))

# Format specifications
lx.out("%s is strings" % "abcde")
lx.out("%d %%" % 50)
lx.out("% 3.2f" % 5.5)
lx.out("Format {1} {0}".format("abcde", "specifications"))

# Use sys.stdout
sys.stdout.write("Hello!\n") # modo don't output.
