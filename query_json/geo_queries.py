# coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson

import logging
logger = logging.getLogger('console.views')

from query_json.db import children_of

'''
NOT USED
def get_city_list(request, province):
    # province = request.GET["province"]
    children_of(province) 
    key_dict = dict([(pinyin, (pname, pinyin),) for pname, pinyin in city_dict.keys()])
    city_list = city_dict[key_dict[province]]
    ret = simplejson.dumps({"cities":city_list})
    return HttpResponse(ret)
'''

def get_area_list(request, parent_area_id):
    children = children_of(parent_area_id) 
    ret = []
    for c in children:
        subarea = {}
        subarea['name'] = c['name']
        subarea['ename'] = c['ename']
        subarea['id'] = c['id']
        ret.append(subarea)

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)

def get_spot_list(request, area_id):
    ret = ["地区1","地区2"]
    if (area_id == "851"):
        ret = ["南禅寺","城中公园"]
    if (area_id == "894"):
        ret = ["虎丘","枫桥景区"]

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)