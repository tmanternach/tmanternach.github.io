import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv
load_dotenv()

'''
url and authText need to be defined in your .env file
url = "https://[FreshRSS URL]/api/greader.php/reader/api/0/subscription/export"
authText = "GoogleLogin auth=username/hash"
'''

def send_request():
    # Request (2)
    # GET https://rss.home/api/greader.php/reader/api/0/subscription/export

    try:
        response = requests.get(
            url=os.getenv('url'),
            headers={
                "Authorization": os.getenv('authText'),
            }, verify=False
        )
        #print('Response HTTP Status Code: {status_code}'.format( status_code=response.status_code))
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

opmlExport = send_request().decode("utf-8")

# Load the OPML file
tree = ET.ElementTree(ET.fromstring(opmlExport))
root = tree.getroot()

categories = {}
for category in root.findall(".//outline[@text]"):
    category_name = category.get("text")
    entries = []

    for outline in category.findall(".//outline[@type='rss']"):
        text = outline.get("text")
        html_url = outline.get("htmlUrl")
        xml_url = outline.get("xmlUrl")
        entries.append(f"- [{text}]({html_url}) ([feed]({xml_url}))")

    if entries:
        categories[category_name] = entries

for idx, (category, entries) in enumerate(categories.items(), start=1):
    print(f"## {category}\n")
    print("\n".join(entries) + "\n\n")
