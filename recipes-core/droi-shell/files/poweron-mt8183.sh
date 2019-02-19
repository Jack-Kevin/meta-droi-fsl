#!/bin/sh

. /etc/default/rcS

#
# power on mt8183
# 
# 
#
test "$VERBOSE" != no && echo -n "Power on MT8183..."
echo -n "Power on MT8183 (1-4)..."
echo 0x000F > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 30s
echo -n "Power on MT8183 (5-8)..."
echo 0x00F0 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
: exit 0

