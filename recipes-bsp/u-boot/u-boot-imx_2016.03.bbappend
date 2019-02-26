FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
FILESPATH_prepend := "${TOPDIR}/../srcs/u-boot-imx/oe-local-files:"

inherit externalsrc
EXTERNALSRC_pn-u-boot-imx = "${TOPDIR}/../srcs/u-boot-imx"
EXTERNALSRC_BUILD_pn-u-boot-imx = "${TOPDIR}/../srcs/u-boot-imx"

UBOOT_CONFIG = "nand"

