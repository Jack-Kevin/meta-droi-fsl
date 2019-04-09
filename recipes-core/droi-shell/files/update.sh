#!/bin/sh

mac=$1
ip=$2
serip=$3

fw_setenv bootcmd
fw_setenv bootcmd_normal
fw_setenv bootcmd_normal 'nand read ${loadaddr} 0x4000000 0x800000;nand read ${fdt_addr} 0x5000000 0x100000;bootz ${loadaddr} - ${fdt_addr}'
fw_setenv bootcmd 'setenv ethaddr '$mac'; setenv ipaddr '$ip'; setenv serverip '$serip'; tftp ubi.img; nand erase 0x06100000 0x09f00000; nand write 0x80800000 0x06100000 $filesize; run bootcmd_normal'
fw_setenv saveenv

reboot
