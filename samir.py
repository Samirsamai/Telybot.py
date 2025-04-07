print "ping -a -s 1000 -w 1 https://mujhekyutoda.ct.ws/"
 print "ping -a -s 100 -w 100 mujhekyutoda.ct.ws
PING mujhekyutoda.ct.ws (185.27.134.204) 100(128) bytes of data.

--- mujhekyutoda.ct.ws ping statistics ---
98 packets transmitted, 0 received, 100% packet loss, time 99313ms"
print"
No mirror or mirror group selected. You might want to select one by running 'termux-change-repo'
Checking availability of current mirror:
[*] https://packages-cf.termux.dev/apt/termux-main/: ok
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  krb5 ldns libdb libedit libresolv-wrapper openssh
  openssh-sftp-server termux-auth
Suggested packages:
  perl
The following NEW packages will be installed:
  git krb5 ldns libdb libedit libresolv-wrapper openssh
  openssh-sftp-server termux-auth
0 upgraded, 9 newly installed, 0 to remove and 49 not upgraded.
Need to get 6918 kB of archives.
After this operation, 39.7 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 git aarch64 2.49.0 [4208 kB]
Get:2 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 libresolv-wrapper aarch64 1.1.7-4 [11.5 kB]
Get:3 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 libdb aarch64 18.1.40-4 [495 kB]
Get:4 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 krb5 aarch64 1.21.3 [900 kB]
Get:5 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 ldns aarch64 1.8.4 [303 kB]
Get:6 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 libedit aarch64 20240517-3.1-0 [79.2 kB]
Get:7 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 openssh-sftp-server aarch64 9.9p2 [49.2 kB]
Get:8 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 termux-auth aarch64 1.5.0 [6980 B]
Get:9 https://packages-cf.termux.dev/apt/termux-main stable/main aarch64 openssh aarch64 9.9p2 [867 kB]
Fetched 6918 kB in 1s (5824 kB/s)
Selecting previously unselected package git.
(Reading database ... 15473 files and directories currently installed.)
Preparing to unpack .../0-git_2.49.0_aarch64.deb ...
Unpacking git (2.49.0) ...
Selecting previously unselected package libresolv-wrapper.
Preparing to unpack .../1-libresolv-wrapper_1.1.7-4_aarch64.deb ...
Unpacking libresolv-wrapper (1.1.7-4) ...
Selecting previously unselected package libdb.
Preparing to unpack .../2-libdb_18.1.40-4_aarch64.deb ...
Unpacking libdb (18.1.40-4) ...
Selecting previously unselected package krb5.
Preparing to unpack .../3-krb5_1.21.3_aarch64.deb ...
Unpacking krb5 (1.21.3) ...
Selecting previously unselected package ldns.
Preparing to unpack .../4-ldns_1.8.4_aarch64.deb ...
Unpacking ldns (1.8.4) ...
Selecting previously unselected package libedit.
Preparing to unpack .../5-libedit_20240517-3.1-0_aarch64.deb ...
Unpacking libedit (20240517-3.1-0) ...
Selecting previously unselected package openssh-sftp-server.
Preparing to unpack .../6-openssh-sftp-server_9.9p2_aarch64.deb ...
Unpacking openssh-sftp-server (9.9p2) ...
Selecting previously unselected package termux-auth.
Preparing to unpack .../7-termux-auth_1.5.0_aarch64.deb ...
Unpacking termux-auth (1.5.0) ...
Selecting previously unselected package openssh.
Preparing to unpack .../8-openssh_9.9p2_aarch64.deb ...
Unpacking openssh (9.9p2) ...
Setting up libedit (20240517-3.1-0) ...
Setting up openssh-sftp-server (9.9p2) ...
Setting up ldns (1.8.4) ...
Setting up git (2.49.0) ...
Setting up libresolv-wrapper (1.1.7-4) ...
Setting up termux-auth (1.5.0) ...
Setting up libdb (18.1.40-4) ...
Setting up krb5 (1.21.3) ...
Setting up openssh (9.9p2) ...
Generating public/private rsa key pair.
Your identification has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_rsa_key
Your public key has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_rsa_key.pub
The key fingerprint is:
SHA256:ohXVkNngubkKtvCGepP2nmr42oJPmYVx7lLFWAp3jNg u0_a545@localhost
The key's randomart image is:
+---[RSA 3072]----+
|  .o.oo +B       |
|  .oE*.oo.o      |
|  . + + o        |
|   = . . o       |
|  . + o S        |
|   * o . .       |
|..*o=   .        |
|+oB=.+ .         |
|oX=** .          |
+----[SHA256]-----+
Generating public/private ecdsa key pair.
Your identification has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_ecdsa_key
Your public key has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_ecdsa_key.pub
The key fingerprint is:
SHA256:LHPaI/+bPm8DmeyqYw/h6iwA/n8j+fBPvUdOL1nl5x4 u0_a545@localhost
The key's randomart image is:
+---[ECDSA 256]---+
|                 |
|                 |
|                 |
|.      .        .|
|o     + S. o   ..|
|..   . B  *  o .o|
| ..  .* oo o+ +E.|
|  .o +=*..o.+= .o|
|   o=o=**==*o....|
+----[SHA256]-----+
Generating public/private ed25519 key pair.
Your identification has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_ed25519_key
Your public key has been saved in /data/data/com.termux/files/usr/etc/ssh/ssh_host_ed25519_key.pub
The key fingerprint is:
SHA256:clocBGmBTN/ex/HlxQ7zk63Na54+4L/MYc3AZNMEM7k u0_a545@localhost
The key's randomart image is:
+--[ED25519 256]--+
|   o..o+.     +o.|
|    o.oo      .* |
|     .. o   . *.=|
|       o o . *EO+|
|      . S . o +o=|
|       =   . . *o|
|      .     . oo=|
|             .+o+|
|              =Xo|
+----[SHA256]-----+ )"
print " 98 packets transmitted, 0 received, 100% packet loss, time 99313ms"
