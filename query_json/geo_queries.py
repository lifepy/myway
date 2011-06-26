# coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson

import logging
logger = logging.getLogger('console.views')

from query_json.db import children_of, attrs_of
from mongo_models import *

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
        subarea = {
            'id':c['id'],
            'name': c['name'],
            'ename':c['ename'],
        }
        ret.append(subarea)

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)

def get_restraunt_list(request, area_id):
    area = attrs_of(area_id)
    min_locality_tag = area['fname'].split(',')[-1]
    print min_locality_tag
    
    restraunts = Restraunt.objects(locality_tags=min_locality_tag).all()
    for r in restraunts:
        print r
    ret = [r.name for r in restraunts]

    ret = simplejson.dumps(ret)
    return HttpResponse(ret)
