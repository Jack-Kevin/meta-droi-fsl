
cat>>/etc/dhcp/dhcpd.conf<<EOF
host debian {
  hardware ethernet $2;
  fixed-address 192.168.$1.200;
}
EOF
