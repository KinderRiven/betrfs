#!/usr/bin/python

from __future__ import print_function
import sys, os, string, fileinput

def isYes(configLine) :
    return "=y" in configLine

def checkConfig(fileName,configOpt):
    with open(fileName) as f:
        for line in f:
            if configOpt in line:
                return isYes(line)

outputFile = "pthread_union_config_options.h"
options = ["CONFIG_LOCK_STAT", "CONFIG_GENERIC_LOCKBREAK", "CONFIG_DEBUG_SPINLOCK", "CONFIG_DEBUG_LOCK_ALLOC", "CONFIG_DEBUG_MUTEXES", "CONFIG_SMP", "CONFIG_MUTEX_SPIN_ON_OWNER", "CONFIG_RWSEM_GENERIC_SPINLOCK"]

try:
    os.unlink(outputFile)
except OSError:
    pass

output = open(outputFile, 'w')

print("// This file is automatically generated.", file=output)
print("// Please run pthread_union_check.py", file=output)
print("// when making kernel config changes", file=output)
print("", file=output)
print("#ifndef FTFS_KERN_CONFIG_H", file=output)
print("#define FTFS_KERN_CONFIG_H", file=output)
print("", file=output)
print("", file=output)

for opt in options :
    if checkConfig(".config", opt) :
        print("#define " + opt, file=output)
    else :
        print("//#define " + opt, file=output)

print("", file=output)
print("", file=output)
print("#endif //FTFS_KERN_CONFIG_H", file=output)