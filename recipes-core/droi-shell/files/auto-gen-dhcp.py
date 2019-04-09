import sys
import os
import re
from time import sleep

#lease_file = '/mnt/one/PythonProject/test/dhcpd.leases'
#interfaces = '/mnt/one/PythonProject/tools/interfaces'
lease_file = '/var/lib/dhcp/dhcpd.leases'
interfaces = '/etc/network/interfaces'

re_start = 'lease 192'
re_end = '}'

def is_need_gen_dhcp(ip):
    if os.path.exists(interfaces):
        with open(interfaces) as interfacesfile:
            content = interfacesfile.readlines()
            for line in content:
                if 'address' in line:
                    ipaddr =  line.split(' ')[-1].strip('\n').split('.')[2]
                    if ip == ipaddr:
                        return False
    return True


if __name__ == '__main__':
    while True:
        ip = ''
        mac = ''
        try:
            if os.path.exists(lease_file):
                print "hhh"
                with open(lease_file) as cnf:
                    content = cnf.read()
                    pat = re.compile(re_start+'(.*?)'+re_end,re.S)
                    result = pat.findall(content)
                    target = []
                    for buf in result:
                        if 'client-hostname \"enp' in buf:
                            target.append(buf)
                    if len(target) > 0:
                        lines = target[-1].split('\n')
                        for line in lines:
                            if 'client-hostname \"enp' in line:
                                enp =  line.split(' ')[-1].strip(';')
                                ret = re.findall(".*enp(.*)s.*",enp)
                                if len(ret) == 1:
                                    ip = ret[0]
                            if 'hardware ethernet' in line:
                                mac = line.split(' ')[-1].strip(';')
                    if ip != '':
                        if is_need_gen_dhcp(ip):
                            os.environ['ip'] = ip
                            os.environ['mac'] = mac
                            os.system('sh /etc/init.d/gen-dhcp.sh $ip $mac &')

        except Exception as e:
            print e
        sleep(3)
