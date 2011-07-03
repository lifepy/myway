#!/usr/bin/python
# coding=utf-8
from lxml import etree
from os.path import join,dirname

DATA_DIR='xml-data'
CHAR_SHI = '市'.decode('utf-8')

china_regions = etree.parse(join(dirname(__file__), DATA_DIR, 'china_regions.xml'))
province_list = [p.attrib for p in china_regions.xpath('/*/*/*')]

def node_of(region_code):
    ''' 
    Returns a node with given region code.
    If region not found, return None
    '''
    try:
        return china_regions.xpath('//*[@region-code='+region_code+']')[0]
    except IndexError:
        return None

def attrs_of(region_code):
    '''
    Returns attributes of the region with given region code.
    If region not found, returns None. '''
    elem = node_of(region_code)
    if elem is not None:
        return elem.attrib
    return None

def children_of(region_code):
    ''' 
    Returns an attribute list of children of the region with given region code.
    If region not found, returns None
    '''
    elem = node_of(region_code)
    if elem is not None:
        return [ child.attrib for child in elem.getchildren() ] 
    return None
        
def cities_in(province_name):
    ''' 
    Returns an attribute list of cities within the province.
    If province not found, return an empty list [].
    '''
    if type(province_name) != unicode:
        province_name = province_name.decode('utf-8')
    cities = china_regions.xpath('//*[@name="%s"]/*[@type="%s"]' %(province_name, CHAR_SHI))
    return [ c.attrib for c in cities ]

def subareas_in(city_name):
    '''
    Returns an attribute list of subareas within the city.
    If city not found, return an empty list []
    '''
    if type(city_name) != unicode:
        city_name = city_name.decode('utf-8')
    subareas = china_regions.xpath('//*[(@name="%s") and (type="%s")]'%(city_name,CHAR_SHI))
    return [ s.attrib for s in subareas ]
