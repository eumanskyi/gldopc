#!/usr/bin/python3

import psutil

mem=psutil.virtual_memory()
msw=psutil.swap_memory()

def mem_metrics():
    print ('virtual total' + ' ' + str(mem.total))
    print ('virtual used' + ' ' + str(mem.used))
    print ('virtual free' + ' ' + str(mem.free))
    print ('virtual shared' + ' ' + str(mem.shared))
    print ('swap total' + ' ' + str(msw.total))
    print ('swap used' + ' ' + str(msw.used))
    print ('swap free' + ' ' + str(msw.free))

mem_metrics()
