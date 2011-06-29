#!/usr/bin/python
# coding=utf-8
from lxml import etree
from xpinyin import xpinyin

pinyin = xpinyin.Pinyin()
xtree = etree.parse('new_region.xml')
'''
Add english name to each node
'''
for node in xtree.iter():
    _name = node.get('name')
    _type = node.get('type')
    if _name.endswith(_type):
        index = _name.rfind(_type)
        ename = pinyin.get_pinyin(_name[:index].encode('utf-8'))
        node.attrib['ename'] = ename

xtree.write('china_regions.xml',encoding='utf-8',pretty_print=True,xml_declaration=True)
