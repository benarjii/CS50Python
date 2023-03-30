import sys

if len(sys.argv) < 2:
	print("too few arguments")
for arg in sys.argv[1:]:
	print(arg)