#!/bin/sh

. /etc/default/rcS

echo droi,slave_nxpinfo 0x2e > /sys/bus/i2c/devices/i2c-2/new_device

. /etc/init.d/poweron-mt8183.sh &

/usr/bin/python /etc/init.d/uart-deamon.py 0 &
/usr/bin/python /etc/init.d/uart-deamon.py 1 &
/usr/bin/python /etc/init.d/uart-deamon.py 2 &
/usr/bin/python /etc/init.d/uart-deamon.py 3 &
/usr/bin/python /etc/init.d/uart-deamon.py 4 &
/usr/bin/python /etc/init.d/uart-deamon.py 5 &
/usr/bin/python /etc/init.d/uart-deamon.py 6 &
/usr/bin/python /etc/init.d/uart-deamon.py 7 &


/usr/bin/python /etc/init.d/droidApp.py &

: exit 0

