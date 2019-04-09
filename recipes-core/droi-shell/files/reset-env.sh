#!/bin/sh
sleep 30s
for ((i=1; i<=3; i++))
do
/sbin/fw_setenv bootcmd
/sbin/fw_setenv bootcmd 'nand read ${loadaddr} 0x4000000 0x800000;nand read ${fdt_addr} 0x5000000 0x100000;bootz ${loadaddr} - ${fdt_addr}'
/sbin/fw_setenv saveenv
sleep 10s
done

: exit 0

