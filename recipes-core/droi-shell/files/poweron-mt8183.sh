#!/bin/sh

. /etc/default/rcS

#
# power on mt8183
# 
# 
#
test "$VERBOSE" != no && echo -n "Power on MT8183..."
#echo -n "Power on MT8183 (1)..."
#sleep 20s
#echo 0x0001 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 30s
echo -n "Power on MT8183 (2)..."
echo 0x0002 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 5s
echo -n "Power on MT8183 (3)..."
echo 0x0004 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 5s
echo -n "Power on MT8183 (4)..."
echo 0x0008 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 30s
echo -n "Power on MT8183 (5)..."
echo 0x0010 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
sleep 5s
echo -n "Power on MT8183 (6)..."
echo 0x0020 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 5s
#echo -n "Power on MT8183 (7)..."
#echo 0x0040 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access
#sleep 5s
#echo -n "Power on MT8183 (8)..."
#echo 0x0080 > /sys/devices/platform/power_rst_gpio/droi_power_rst_access


: exit 0

