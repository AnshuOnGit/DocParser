import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

def get_root_tag(param_tree):
    return tree.getroot().tag

if __name__ == '__main__':
    print(get_root_tag(tree))
