#!/usr/bin/python
# coding=utf-8
from lxml import etree
from os.path import join,dirname

DATA_DIR='xml-data'

china_cities = etree.parse(join(dirname(__file__), DATA_DIR, 'china.xml'))
province_list = [p.attrib for p in china_cities.xpath('//*[@layer=1]')]

def node_of(id):
    elem = china_cities.xpath('//*[@id='+id+']')[0]
    return elem.attrib

def children_of(id):
    ret = []
    for elem in china_cities.xpath('//*[@pid='+id+']'):
        ret.append(elem.attrib)
    return ret
        
# for p in children_of('12'):
    # print p['name'],p['id'],p['layer']
