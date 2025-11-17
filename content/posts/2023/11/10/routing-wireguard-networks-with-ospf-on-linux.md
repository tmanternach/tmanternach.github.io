+++
title = "Routing Wireguard networks with OSPF on Linux"
slug = "routing-wireguard-networks-with-ospf-on-linux"
date = 2023-11-10 16:46:25-07:00
+++

I have a couple of Linux servers whose main purpose is to serve as a [Wireguard]( https://en.wikipedia.org/wiki/WireGuard) server. The peers on these servers are a combination of pure clients (like a mobile phone or laptop) and more traditional site-to-site tunnel connections (like a router at a remote location). The site-to-site connections usually are routing a remote network over the wireguard tunnel, something like a /24 network so you can access the far site's local network.

Wireguard makes this easy to do, you just add the /24 network as an "AllowedIP" for that peer. Wireguard does the work of adding that route to the routing table on the Linux server itself. If this Wireguard server is part of a more complex network, though, you need to be sending these remote networks to your Wireguard server so everyone can access them, not just those using Wireguard. I have been forced to add static routes on my main router to point those networks to my Wireguard servers.

Enter OSPF! If you are reading this, I am going to assume you know what OSPF is and why it's preferred over static routing. What follows is the steps I took to get my Wireguard "AllowedIPs" network automatically advertised to my main router using OSPF.

Install FRR
-----------

[FRR](https://en.wikipedia.org/wiki/FRRouting) is a Linux package that implements a lot of networking routing protocols. On your server running Wireguard (I'm assuming Debian/Ubuntu), running  `apt get install -y frr`  gets everything you need installed. This includes a `vtysh` command that dumps you into a Cisco IOS-like terminal to configure your OSPF routing.


Enable OSPF daemon
------------------

Before configuring OSPF, you must enable the ospfd daemon in the FRR config. Edit `/etc/frr/daemons` and change the `ospfd=no` line to read `ospfd=yes`. Then `systemctl restart frr` is needed to restart FRR with OSPF enabled.

Configure OSPF inside FRR
-------------------------

Run `vtysh` to enter the FRR VTY interface. `config terminal` to enter configuration mode. Here is the simplest configuration required to enable OSPF:

```
interface ens160
	  ip ospf network point-to-point
!
router ospf
	  ospf router-id 192.168.0.0
	  redistribute kernel
	  redistribute connected
	  network 192.168.0.0/31 area 0
```
Here is the same config with my comments explaining the important parts:

```
interface ens160 # this is your linux interface that is facing your main router.
  ip ospf network point-to-point # I am using a point-to-point style OSPF network, yours might be a broadcast type.
!
router ospf
  ospf router-id 192.168.0.0 # this could be anything, but traditionally this is your LAN IP of this wireguard server
  redistribute kernel # this was the tricky part. This is required to insert the Wireguard "AllowedIPs" networks into OSPF
  redistribute connected # this is required to insert your wg0 (and other) networks in OSPF
  network 192.168.0.0/31 area 0 # this is your LAN network for this wireguard server. Whatever is assigned to ens160 in my case. This is required to establish a neighbor relationship with my router.
```

This guide doesn't cover any of the OSPF configuration on your main router. There are far too many different routers out there to even attempt to cover. The main trick to getting all of this working was stumbling across the `redistribute kernel` command. I was familiar with the `redisribute static` and `redistribute connected` commands from administering Cisco IOS, but the way that Wireguard inserts these routes into the routing table requires use of this `redistribute kernel` command.

Save your changes
-----------------

That's it! You can `end` and then `write memory` to save your configuration to `/etc/frr/frr.conf`. If you miss this part, all of this configuration will be erased when FRR is restarted.

Troubleshooting
---------------

Here are a couple of commands I used in the `vtysh` interface to verify my configuration.

- `show ip ospf neighbor` - this should return a record showing your neighbor relationship with your main router
- `show ip route kernel` - this should return all of your AllowedIPs networks that you have configured in Wireguard. These are the networks we are redistributing over OSPF.
- `show ip ospf interface` - this should return a record indicating `ens160 is up`, or whatever your LAN interface on your Wireguard server is. You can also see neighbor count here, which should be 1 in a point-to-point OSPF network.
