FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

do_install_append(){
    install -m 0755 ${WORKDIR}/init-server ${D}${sysconfdir}/init.d/dhcp-server
    install -m 0644 ${WORKDIR}/default-server ${D}${sysconfdir}/default/dhcp-server
    install -m 0644 ${WORKDIR}/dhcpd.conf ${D}${sysconfdir}/dhcp/dhcpd.conf
}
