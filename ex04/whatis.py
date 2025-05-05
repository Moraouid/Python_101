import sys

args = sys.argv

if len(sys.argv) == 1:
    exit(0)
if len(sys.argv) > 2:
    print ("AssertionError: more than one argument is provided")
    exit(0)
try:
    if int(args[1]) % 2 == 0:
        print("I'm Even.")
    if int(args[1]) % 2 == 1:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not a valid integer")
    