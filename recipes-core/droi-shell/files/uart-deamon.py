#! /usr/bin/env python

import os
import sys
import serial
from time import sleep
from datetime import datetime
from threading import Timer
import time
import json

TASK_TIME = 1

serial

def timedTask():
    Timer(TASK_TIME, task, ()).start()


# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def task():
    send_request(serial, 'get \n')
    timedTask()


def send_request(serial, data):
    if serial.isOpen:
        #print(" send ", data)
        serial.flushInput()
        serial.flushOutput()
        serial.write(data)
        #sleep(.1)


def recv(serial):
    while True:
        data = serial.readline()
        if data == '':
            print(" nonono!")
            continue
        else:
            break
        sleep(0.02)
    return data


if __name__ == '__main__':
    b=0
    serial = serial.Serial('/dev/ttymxc' + sys.argv[1], 115200)
    if serial.isOpen:
        b=1
        print(" open success!")
    else:
        b=0
        print(" open error !")

    timedTask()

    while True:
        if b == 0:
            serial = serial.Serial('/dev/ttymxc' + sys.argv[1], 115200)
            if serial.isOpen:
                b=1
            else:
                b=0
                break
        try:
            data = recv(serial)
            if data != b'':
                #print("receive : ", data)
                temp = json.loads(data)
                cpu_temp = temp["cpu_temp"]
                print(cpu_temp)
                os.environ['cpu_24']=str((cpu_temp&0xff000000)/2**24)
                os.environ['cpu_16']=str((cpu_temp&0xff0000)/2**16)
                os.environ['cpu_8']=str((cpu_temp&0xff00)/2**8)
                os.environ['cpu_0']=str((cpu_temp&0xff))
                os.environ['id']=str(4 * int(sys.argv[1]) + 0)
                os.system('echo $id $cpu_24 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id']=str(4 * int(sys.argv[1]) + 1)
                os.system('echo $id $cpu_16 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id']=str(4 * int(sys.argv[1]) + 2)
                os.system('echo $id $cpu_8 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id']=str(4 * int(sys.argv[1]) + 3)
                os.system('echo $id $cpu_0 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                ap_temp = temp["ap_temp"]
                #os.environ['ap']=str(ap_temp)
                #os.environ['id_2']=str(int(sys.argv[1]) + 40)
                os.environ['ap_24']=str((ap_temp&0xff000000)/2**24)
                os.environ['ap_16']=str((ap_temp&0xff0000)/2**16)
                os.environ['ap_8']=str((ap_temp&0xff00)/2**8)
                os.environ['ap_0']=str((ap_temp&0xff))
                os.environ['id_2']=str(40 + 4 * int(sys.argv[1]) + 0)
                os.system('echo $id_2 $ap_24 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id_2']=str(40 + 4 * int(sys.argv[1]) + 1)
                os.system('echo $id_2 $ap_16 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id_2']=str(40 + 4 * int(sys.argv[1]) + 2)
                os.system('echo $id_2 $ap_8 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                os.environ['id_2']=str(40 + 4 * int(sys.argv[1]) + 3)
                os.system('echo $id_2 $ap_0 > /sys/bus/i2c/devices/2-002e/slave_nxpinfo')
                #os.environ['data']=data
                #os.environ['path']='/tmp/temp' + sys.argv[1]
                #os.system('echo $data > $path')
                with open('/tmp/temp'+sys.argv[1], 'w') as f:
                    f.write(data)
        except Exception as e:
            print e
        sleep(.2)
