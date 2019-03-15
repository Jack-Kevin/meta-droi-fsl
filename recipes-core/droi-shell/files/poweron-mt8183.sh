#!/bin/sh

. /etc/default/rcS

#
# power on mt8183
# 
# 
#
test "$VERBOSE" != no && echo -n "Power on MT8183..."
echo -n "Power on MT8183 (1-4)..."
#echo 0x0002 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo 0x0004 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo 0x0008 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo -n "Power on MT8183 (5-8)..."
#echo 0x0010 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo 0x0020 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo 0x0040 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
#echo 0x0080 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 20s
echo 0x000e > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 20s
echo 0x00f0 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
: exit 0

