import sys
print("Started!!");
s = raw_input()
while s!="c":
    print("Received",s);
    sys.stdout.flush()
    s = raw_input()

