DESCRIPTION = "8167s GVA feture auto-test"
LICENSE = "CLOSED"

SRC_URI += "file://poweron-mt8183.sh file://droi-shell.sh "

do_install_append () {
        install -d ${D}${sysconfdir}/init.d
        install -m 0755 ${WORKDIR}/droi-shell.sh ${D}${sysconfdir}/init.d/droi-shell.sh
	install -m 0755 ${WORKDIR}/poweron-mt8183.sh ${D}${sysconfdir}/init.d/poweron-mt8183.sh

        update-rc.d -r ${D} droi-shell.sh start 03 S .
}
