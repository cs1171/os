#! /bin/python

import subprocess, time, os, mmap

recover = 0

fname = raw_input("Please enter name and date to save process status (name xx-xx-xx):")
c = raw_input("Do you wish to terminate process y/n?")
if(c == "n"):
    exit()
elif(c == "y"):
    try:
        temp = fname.split()
        proc = temp[0]
        temp = map(int,subprocess.check_output(["pidof",proc]).split())
        pid = str(temp[len(temp)-1])
        status = subprocess.check_output(["ps", pid])
        f = open("/dev/shm/" + fname, "a")
        f.write(status)
        f.close()
    except Exception as e:
        print "Process does not exist."

while(map(int,subprocess.check_output(["pidof","firefox"])):
    print "Waiting for user to kill process..."
    time.sleep(3)

while not(map(int,subprocess.check_output(["pidof","firefox"])):
    print "Waiting for process to restart..."
    time.sleep(3)

print "Recovering process status...\n"
f = open("/dev/shm/" + fname, "r+")
mm = mmap.mmap(f.fileno(), 0)
print mm.readline()
print mm.readline()
#aware of security hazard, please don't inject silly commands like rm -rf /
subprocess.call("rm /dev/shm/" + fname, shell = True)

