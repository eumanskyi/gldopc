#!/usr/bin/python3

import psutil

cpu=psutil.cpu_times()

def cpu_metrics():
    print ('system.cpu.idle' + ' ' + str(cpu.idle))
    print ('system.cpu.user' + ' ' + str(cpu.user))
    print ('system.cpu.guest' + ' ' + str(cpu.guest))
    print ('system.cpu.iowait' + ' ' + str(cpu.iowait))
    print ('system.cpu.steal' + ' ' + str(cpu.steal))
    print ('system.cpu.system' + ' ' + str(cpu.system))

cpu_metrics()
