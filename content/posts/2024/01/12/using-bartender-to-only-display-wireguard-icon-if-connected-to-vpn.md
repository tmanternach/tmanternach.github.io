+++
title = "Using Bartender to only display Wireguard icon if connected to VPN"
slug = "using-bartender-to-only-display-wireguard-icon-if-connected-to-vpn"
date = 2024-01-12 19:13:44-07:00
+++

### Intro

I don't remember if I figured this out myself or found the suggestion elsewhere, but I just searched and couldn't find anything online so I decided to document this neat trick.

I use [Bartender](https://www.macbartender.com/) on all my Macs to clean up my Menu Bar. However I missed being able to glance up and look at the [Wireguard](https://www.wireguard.com/) icon to tell if I was connected to a Wireguard VPN or not. Bartender has a "Triggers" feature that makes it possible to show certain menu bar icons based on the output of a shell script.

### Setup
Open Bartender settings and visit the Triggers menu. Click Add Trigger. Name your Trigger and leave the "Activate a Preset" alone. Choose your Wireguard icon from the "Select menu bar items". Click Add Trigger Condition and choose Script. Paste the following script:

```scutil --nc list | grep -c -e "\(Connected\).*wireguard"```

This script uses the built-in `scutil` command to list all VPN connections configured on your Mac. It then uses `grep` to filter for only the Wireguard connections that have a status of Connected. The `-c` flag on `grep` counts the number of lines instead of outputting them. Bartender's Triggers expect a script result of `1`, `yes`, or `true` to activate the Trigger. As far as I know, Wireguard does not allow you to connect to more than one endpoint at a time, so this script should only ever output a `0` or `1`.

I have mine set to run every 1 minute. This means that after you connect to a VPN with Wireguard, it could take the icon up to 1 minute to appear in your Menu Bar. Same thing after you disconnect.

That's it! Click Done and your new Trigger is live and ready to use.

### Troubleshooting

If this isn't working for you, my best suggestion would be to connect to a VPN with Wireguard and run the script above in your Terminal and verify that it is outputting `1`. 