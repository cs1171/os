#! /bin/python

import subprocess, time, os, mmap

recover = 0

fname = raw_input("Please enter name and date to save process status (name xx-xx-xx):")
c = raw_input("Do you wish to terminate process y/n?")
if(c == "n"):
    exit()
elif(c == "y"):
    try: # code to find pid of process from given process name
        temp = fname.split()
        proc = temp[0]
        temp = map(int,subprocess.check_output(["pidof",proc]).split())
        pid = str(temp[len(temp)-1])
        status = subprocess.check_output(["ps", pid]) # var for status
        f = open("/dev/shm/" + fname, "a") #/dev/shm/ shared memory location
        f.write(status) #write status to file
        f.close()
    except Exception as e:
        print "Process does not exist."

while(recover == 0):
    try: # checks if process still running
        tpid = int(pid)
        os.kill(tpid, 0)
        print "Waiting for user to kill process..."
        time.sleep(2)
    except Exception as e: # process killed, exit while loop
        print "Process killed."
        recover = 1

while(recover == 1):
    try: # checks if process is running again
        temp = fname.split()
        proc = temp[0]
        temp = map(int,subprocess.check_output(["pidof",proc]).split())
        recover = 0
    except Exception as e: # waits until process starts again
        print "Waiting for process to restart..."
        time.sleep(2)

# code block to recover and print status when process was previously running
print "Recovering process status...\n"
f = open("/dev/shm/" + fname, "r+")
mm = mmap.mmap(f.fileno(), 0)
print mm.readline()
print mm.readline()
os.remove("/dev/shm/" + fname)
