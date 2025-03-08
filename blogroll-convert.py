import xml.etree.ElementTree as ET

# Load the OPML file
tree = ET.parse("/Users/trevormanternach/Documents/Subscriptions-FreshRSS.opml")
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



# Format and write to Markdown
for idx, (category, entries) in enumerate(categories.items(), start=1):
    print(f"## {category}\n")
    print("\n".join(entries) + "\n\n")


#print("\n".join(markdown_list))

#print("Markdown list successfully created as 'feeds_list.md'")