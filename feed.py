import yaml
import xml.etree.ElementTree as xml_tree

# This script reads a YAML file containing podcast feed information and generates an RSS XML file for the podcast. 
# The YAML file is expected to have a structure that includes at least a 'title' field for the podcast. 
# The generated RSS XML will include the necessary namespaces for iTunes and content modules, and it will create a basic structure 
# for the RSS feed with the channel title.


with open('feed.yaml', 'r') as file:
    feed_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    })    

    channel_element = xml_tree.SubElement(rss_element, 'channel')

    link_prefix = feed_data['link']

    xml_tree.SubElement(channel_element, 'title').text = feed_data['title']
    xml_tree.SubElement(channel_element, 'format').text = feed_data['format']
    xml_tree.SubElement(channel_element, 'description').text = feed_data['description']
    xml_tree.SubElement(channel_element, 'subtitle').text = feed_data['subtitle']
    xml_tree.SubElement(channel_element, 'itunes:author').text = feed_data['author']
    # xml_tree.SubElement(channel_element, 'itunes:image').text = feed_data['image']
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + feed_data['image']})
    xml_tree.SubElement(channel_element, 'language').text = feed_data['language']
    xml_tree.SubElement(channel_element, 'link').text = link_prefix

    xml_tree.SubElement(channel_element, 'itunes:category', {'text': feed_data['category']})

    for item in feed_data['item']:
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item['title']
        xml_tree.SubElement(item_element, 'description').text = item['description']

    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)

    