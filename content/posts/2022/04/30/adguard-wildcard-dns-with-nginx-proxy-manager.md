+++
title = "AdGuard Wildcard DNS with Nginx Proxy Manager"
slug = "adguard-wildcard-dns-with-nginx-proxy-manager"
date = 2022-04-30 20:59:42-06:00
tags = ['adguard', 'dns', 'tutorial']
+++

I started using Nginx Proxy Manger at home recently and found a fast and easy way to add internal domains to it. Here is a simple walkthrough.

### Prerequisites

- You need to be using [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) for DNS
- You want to quickly add new domains to [Nginx Proxy Manager](https://nginxproxymanager.com/)

### AdGuard Home setup

In the AdGuard Home web interface, go to Filters->DNS rewrites.

![Screenshot of DNS rewrite options on AdGuard Home](/images/adguard-1.png "Screenshot of DNS rewrite options on AdGuard Home")

Click **Add DNS rewrite** and enter something like *\*.home* in the domain name field.

Enter the IP address of your NPM host and click **Save**.

### Nginx Proxy Manager

![Screenshot of Nginx Proxy Manager](/images/nginx-1.png "Screenshot of Nginx Proxy Manager")

There really isn't anything special to do in NPM. Just add a Proxy Host and in the domain names field you can enter anything as long as it ends in .home (or whatever you chose for a wildcard). www.home even works!

Another little feature I discovered while setting this up is that I can add multiple domain names for each proxy host. So *adguard.home* and *dns.home* can both get me to the same place. This helps when I can't remember the name of a service, or when you change software you can keep using something like *dashboard.home* for your [dashboard of choice](https://github.com/bastienwirtz/homer).


