import os, sys, subprocess

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    print(f)
    fnew = "{0:06}".format(int(f))
    print(fnew)
    command = "mv "+f+e+" "+fnew+e
    print("command ", command)
    subprocess.call(command,shell=True)
