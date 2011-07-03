#!/usr/bin/python
# coding=utf-8
from lxml import etree
from os.path import join,dirname

DATA_DIR='xml-data'

china_regions = etree.parse(join(dirname(__file__), DATA_DIR, 'china_regions.xml'))
province_list = [p.attrib for p in china_regions.xpath('/*/*/*')]

def node_of(region_code):
    regions = china_regions.xpath('//*[@region-code='+region_code+']')
    if len(regions):
        return regions[0]
    else:
        return None

def attrs_of(region_code):
    elem = node_of(region_code)
    if elem:
        return elem.attrib
    else:
        return None

def children_of(region_code):
    ret = []
    elem = node_of(region_code)
    if elem:
        for child in elem.getchildren():
            ret.append(child.attrib)
    return ret
        
def city_by_name(name):
    elem = china_regions.xpath('//*[@name="'+name+'"]')[0]
    return elem.attrib

# for p in children_of('12'):
    # print p['name'],p['id'],p['layer']
