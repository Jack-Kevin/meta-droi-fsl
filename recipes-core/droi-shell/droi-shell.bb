DESCRIPTION = "8167s GVA feture auto-test"
LICENSE = "CLOSED"

SRC_URI += "file://poweron-mt8183.sh file://droi-shell.sh file://uart-deamon.py file://droidApp.py file://gen-dhcp.sh "

do_install_append () {
        install -d ${D}${sysconfdir}/init.d
        install -m 0755 ${WORKDIR}/droi-shell.sh ${D}${sysconfdir}/init.d/droi-shell.sh
	install -m 0755 ${WORKDIR}/poweron-mt8183.sh ${D}${sysconfdir}/init.d/poweron-mt8183.sh
        install -m 0755 ${WORKDIR}/uart-deamon.py ${D}${sysconfdir}/init.d/uart-deamon.py
        install -m 0755 ${WORKDIR}/droidApp.py ${D}${sysconfdir}/init.d/droidApp.py
        install -m 0755 ${WORKDIR}/gen-dhcp.sh ${D}${sysconfdir}/init.d/gen-dhcp.sh

        update-rc.d -r ${D} droi-shell.sh start 03 S .
}
