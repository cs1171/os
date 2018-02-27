#! /bin/python

import subprocess, time, os, mmap


recover = 0
pid = ""

while(recover != 1):
    try:
        temp = map(int,subprocess.check_output(["pidof","firefox"]).split())
        pid = str(temp[len(temp)-1])
        status = subprocess.check_output(["ps", pid])
        time.sleep(2)
    except Exception as e:
        recover = 1        
        continue

if(recover == 1):
    print "Program crashed!\n"
    fname = raw_input("Please enter name and date to save process status (name xx-xx-xx):")
    if(!(os.path.isfile(fname))):
        f = open("/dev/shm/" + fname, "a")
        f.write(status)
        c = raw_input("Do you wish to terminate process y/n?")
        if(c == "n"):
            exit()
        elif(c == "y"):
            mm = mmap.mmap(f.fileno(), 0)
    else:
        


while(recover != 1):
    try:
        temp = map(int,subprocess.check_output(["pidof","firefox"]).split())
        pid = str(temp[len(temp)-1])
        status = subprocess.check_output(["ps", pid])
        time.sleep(1)
    catch Exception as e:
        recover = 1

print "Recovering process status...\n"
f = open("/dev/shm/" + fname, "r+")
mm = mmap.mmap(f.fileno(), 0)
print mm.readline()
print mm.readline()
