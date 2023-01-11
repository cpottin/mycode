#!/usr/bin/env python3

#standard library imports
import shutil
import os

def main():
    #called at runtime
    #move into this working directory
    os.chdir('/home/student/mycode/')

    # try moving the file raynor.obj into ceph_storage/ dir
    shutil.move('raynor.obj', 'ceph_storage/')

#program will pause while we accept input 
#collect a string from user 
    xname = input('What is the new name for kerrigan.obj? ')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
