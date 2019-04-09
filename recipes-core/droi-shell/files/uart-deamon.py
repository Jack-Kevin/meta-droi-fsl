#! /usr/bin/env python

import os
import sys
import serial
from time import sleep
from datetime import datetime
from subprocess import Popen, PIPE
from threading import Timer
import time
import json

TASK_TIME = 1

serial

def timedTask():
    Timer(TASK_TIME, task, ()).start()


# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def task():
    if os.path.exists('/tmp/mac' + str(sys.argv[1])):
        with open('/tmp/mac' + str(sys.argv[1]), 'rw+') as mac_f:
            mac = mac_f.readline()
            send_request(serial, mac)
            os.remove('/tmp/mac' + str(sys.argv[1]))
    else:
        ipaddress = ''
        try:
            ipconfig = getIP()
            nics = genIP(ipconfig)
            ipaddress = parseIP(nics).split('.')[2]
        except Exception as e:
            print e
        send_request(serial, 'get>' + ipaddress + '>' + str(int(sys.argv[1]) + 1) + '\n')
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


def getIP():
    p = Popen(['ifconfig'], stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()
    data = [i for i in stdout.split('\n') if i]
    return data

def genIP(data):
    new_line = ''
    lines = []
    for line in data:
        if line[0].strip():
            lines.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    lines.append(new_line)
    return [i for i in lines if i and not i.startswith('lo')]

def parseIP(data):
    ipaddr = '00:00:00:00'
    for devs in data:
        lines = devs.split('\n')
        ipaddr  = lines[1].split()[1].split(':')[1]
    return ipaddr


def parseMac(data):
    #dic = {}
    macaddr = ''
    for devs in data:
        lines = devs.split('\n')
        macaddr = lines[0].split()[-1]
    return macaddr


if __name__ == '__main__':
    bIsopen = 0
    serial = serial.Serial('/dev/ttymxc' + sys.argv[1], 115200)
    if serial.isOpen:
        bIsopen = 1
        print(" open success!")
    else:
        bIsopen = 0
        print(" open error !")

    timedTask()

    while True:
        if bIsopen == 0:
            serial = serial.Serial('/dev/ttymxc' + sys.argv[1], 115200)
            if serial.isOpen:
                bIsopen = 1
            else:
                bIsopen = 0
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

                with open('/tmp/temp'+sys.argv[1], 'w') as f:
                    f.write(data)

                ##sava temp
                #os.environ['data']= datetime.now().strftime("%Y-%m-%d %H:%M:%S") + data
                #os.environ['path']= '/home/root/temp' + sys.argv[1]
                #os.system('echo $data >> $path')
        except Exception as e:
            print e
        sleep(.2)
