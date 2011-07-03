#!/usr/bin/python
# coding=utf-8
from lxml import etree
from xpinyin import xpinyin

pinyin = xpinyin.Pinyin()
xtree = etree.parse('new_region.xml')
'''
Add full name to each node
'''
root = xtree.getroot()
for node in xtree.iter():
    _name = node.get('name')
    _type = node.get('type')

    #canonical name
    if _name.rfind(_type)>0:
        _cname = _name[:_name.rfind(_type)] 
    else:
        _cname = _name
    parent = node.getparent()

    # fullname
    if parent is not None and 'fullname' in parent.attrib:
        fullname = parent.get('fullname')+',' + _name
    else:
        fullname = _name
    node.attrib['fullname'] = fullname

xtree.write('china_regions.xml',encoding='utf-8',pretty_print=True,xml_declaration=True)
