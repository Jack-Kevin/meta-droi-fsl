
cat>/etc/dhcp/dhcpd.conf<<EOF

ddns-update-style none;

option domain-name "example.org";
option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;

subnet 192.168.$1.0 netmask 255.255.255.0 {
    range 192.168.$1.100 192.168.$1.254;
    option routers 192.168.$1.1;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.$1.255;
    #option domain-name-servier 192.168.$1.1;
    option ntp-servers 192.168.$1.1;
    option netbios-name-servers 192.168.$1.1;
    option netbios-node-type 8;
}

#host debian {
#  hardware ethernet $2;
#  fixed-address 192.168.$1.200;
#}
EOF

cat>/etc/network/interfaces<<EOF
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 192.168.$1.20
    netmask 255.255.255.0
    broadcast 192.168.$1.255
    gateway 192.168.$1.1
EOF


rm -rf /var/lib/dhcp/dhcpd.leases

/etc/init.d/networking restart
