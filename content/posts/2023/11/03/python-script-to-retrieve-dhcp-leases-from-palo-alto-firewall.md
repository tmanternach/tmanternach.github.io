+++
title = "Python script to retrieve DHCP leases from Palo Alto firewall"
slug = "python-script-to-retrieve-dhcp-leases-from-palo-alto-firewall"
date = 2023-11-03 16:50:34-06:00

+++

I have been using a Palo Alto PA-220 firewall for my home router for years. It is my DHCP server for my LAN. I often find myself needing to view the DHCP leases to see what IP address some random device (WLED, ESPHome devices, etc.) has. The web interface for the PA-220 is unbearably slow and the SSH CLI takes 30+ seconds after login to give me a prompt.

To speed up this task, I wrote this fairly simple script using python3. It uses the REST API that PAN-OS has to retrieve the DHCP leases. This script completes for me in less than 1 second. It outputs a JSON object. This works best for me as I find JSON to be humanly-readable and also allows me to pipe it to a utility like `jq` to filter it quickly.

Here is the code:

```
import requests
import json
from xmltodict import parse, ParsingInterrupted
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

host = "192.168.2.1" # IP of Palo-Alto firewall goes here.
key = "KEY_GOES_HERE" # Run `curl -X GET 'https://<host>/api/?type=keygen&user=<username>&password=<password>'` to create API key.
interface = "ethernet1/2" # can also use "all"

def get_dhcp_leases(host, key, interface):
	url = "https://{host}/api/?type=op&cmd=<show><dhcp><server><lease><interface>{interface}</interface></lease></server></dhcp></show>&key={key}".format(host=host, key=key, interface=interface)
	response = requests.get(url,verify=False)
	return response

if __name__ == "__main__":
	dhcp_leases = get_dhcp_leases(host, key, interface)
	data = parse(dhcp_leases.content)
	entries = data['response']['result']
	print(json.dumps(entries, indent=4))
```

I also have this hosted as a [gist](https://gist.github.com/tmanternach/21e3bba23261cbd5bacba2e50588acf6) on github. Any changes I make to it are more likely to end up there than here. Comments are welcome over there, too!