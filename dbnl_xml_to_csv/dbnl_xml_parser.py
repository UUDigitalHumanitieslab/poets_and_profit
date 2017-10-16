from my_helpers import remove_tabs_and_newlines
import xml.etree.ElementTree as ET
import re

def set_used_copy(root, parsedFile):
    for node in root.iter('idno'):
        if node.get('type') and node.get('type').lower() == 'usedcopy':
            parsedFile.used_copy = node.text
            return

    editionStmt = root.find('.//editionStmt')
    if editionStmt and editionStmt[0].text and editionStmt[0].text.upper() == "GEBRUIKT EXEMPLAAR":
        parsedFile.used_copy = editionStmt[1].text
        return

    sourceDesc = root.find('.//sourceDesc')
    parsedFile.used_copy = extract_text_without_html(sourceDesc)
     
def set_title(root, parsedFile):
    title_node = root.find('.//titleStmt/title')     
    if len(title_node.findall('*')) > 0:
        parsedFile.title = extract_text_without_html(title_node)
    else:
        parsedFile.title = title_node.text

def set_author(root, parsedFile):
    parsedFile.author = get_simple_text_content(root, './/titleStmt/author')

def set_publication_idno(root, parsedFile):
    parsedFile.publication_idno = get_simple_text_content(root, './/publicationStmt/idno')

def set_publisher(root, parsedFile):
    node = root.find('.//sourceDesc/p')
    publisher = remove_hi_elements(node)
    parsedFile.publisher = remove_tabs_and_newlines(publisher)    

def set_year_published(parsedFile):
    if parsedFile.publisher:        
        found = re.search('1\d{3}|2\d{3}', parsedFile.publisher) 
        parsedFile.year_published = found.group(0) if found is not None else '0'
    else:
        raise Exception('set_year_published requires a ParsedFile instance with publisher set')

def set_text(root, parsedFile):
    chapters = []
    
    cf_chapter_node = root.find(".//text/body/cf/div[@type='chapter']")
    if cf_chapter_node:
        chapters.append(extract_text_without_html(cf_chapter_node))
    
    for chapter_node in root.findall(".//text/body/div[@type='chapter']"):        
        chapters.append(extract_text_without_html(chapter_node))

    parsedFile.chapters = chapters
             

def remove_hi_elements(node):
    node_string = ET.tostring(node, encoding='unicode', method='xml')
    return re.sub('<p>|<hi rend=".*">|<hi>|</hi>|</p>', '', node_string)

def extract_text_without_html(node_containing_text):    
    collected_strings = []
    get_text_recursive(node_containing_text, collected_strings)
    return (' '.join(collected_strings))

def get_text_recursive(node, collected_strings):
    if node.tag != "note" and node.text and not (node.tag == "hi" and len(node.text) < 3):       
        text = node.text
        text = remove_tabs_and_newlines(text).strip()
        collected_strings.append(text)

    for child in node:
        get_text_recursive(child, collected_strings)

def get_simple_text_content(root, xpath):
    node = root.find(xpath)
    if not node is None and node.text:
        return remove_tabs_and_newlines(node.text)
    else:
        return ''
