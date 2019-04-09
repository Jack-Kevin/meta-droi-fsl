DESCRIPTION = "8167s GVA feture auto-test"
LICENSE = "CLOSED"

INSANE_SKIP_${PN} = "already-stripped"

SRC_URI += "file://poweron-mt8183.sh \
	file://droi-shell.sh \
	file://uart-deamon.py \
	file://droidApp.py \
	file://gen-dhcp.sh \
	file://auto-gen-dhcp.py \
	file://fw_env.config \
	file://fw_printenv \
	file://fw_setenv \
	file://update.sh \
	file://reset-env.sh \
"

do_install_append () {
        install -d ${D}${sysconfdir}/init.d
        install -m 0755 ${WORKDIR}/droi-shell.sh ${D}${sysconfdir}/init.d/droi-shell.sh
	install -m 0755 ${WORKDIR}/poweron-mt8183.sh ${D}${sysconfdir}/init.d/poweron-mt8183.sh
        install -m 0755 ${WORKDIR}/uart-deamon.py ${D}${sysconfdir}/init.d/uart-deamon.py
        install -m 0755 ${WORKDIR}/droidApp.py ${D}${sysconfdir}/init.d/droidApp.py
        install -m 0755 ${WORKDIR}/gen-dhcp.sh ${D}${sysconfdir}/init.d/gen-dhcp.sh
        install -m 0755 ${WORKDIR}/auto-gen-dhcp.py ${D}${sysconfdir}/init.d/auto-gen-dhcp.py

	install -m 0755 ${WORKDIR}/update.sh ${D}${sysconfdir}/init.d/update.sh
	install -m 0755 ${WORKDIR}/reset-env.sh ${D}${sysconfdir}/init.d/reset-env.sh

	install -d ${D}${base_sbindir}
	install -d ${D}${sysconfdir}
	install -m 755 ${WORKDIR}/fw_printenv ${D}${base_sbindir}/fw_printenv
	install -m 755 ${WORKDIR}/fw_printenv ${D}${base_sbindir}/fw_setenv
	install -m 0644 ${WORKDIR}/fw_env.config ${D}${sysconfdir}/fw_env.config

        update-rc.d -r ${D} droi-shell.sh start 03 S .
}
