FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
FILESPATH_prepend := "${TOPDIR}/../srcs/linux-imx/oe-local-files:"

inherit externalsrc
EXTERNALSRC_pn-linux-imx = "${TOPDIR}/../srcs/linux-imx"
SRCTREECOVEREDTASKS = "do_validate_branches do_kernel_checkout do_fetch do_unpack do_patch do_kernel_configme do_kernel_configcheck"

do_configure_append() {
    mkdir -p ${STAGING_KERNEL_DIR}
    oe_runmake -C ${S} O=${B} imx_v7_defconfig
}

