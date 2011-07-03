#!/usr/bin/env python
# coding=utf-8
from pymongo import Connection

from mongo_models import *
from query_json.db import city_by_name, children_of



origin = Connection(host='204.62.14.55').dianping
origin.authenticate('dianping','crawler')

def null_handler(record): pass

def hotel_handler(record): pass

def restraunt_handler(record):
    if Restraunt.objects(name=record['name']) \
       or record.get('rating',0) < 2 \
       or record.get('n_rating',0) < 2:
        return

    r = Restraunt(name = record['name'])

    # transport every attribute that has same name
    for key in dict(record).keys():
        if key in r.__dict__['_data'].keys() and key not in ['category']:
            r.__dict__['_data'][key] = record[key]

    city = record['city']
    city_attrs = city_by_name(city)
    children = children_of(city_attrs['id'])

    # find city in admin-division database and tag restraunt with locality
    districts = dict([(c['name'],c) for c in children])
    bread_crumb = record['bread_crumb'].split(u'\xbb')
    for item in bread_crumb:
        if item in districts.keys():
            for tag in districts[item]['fname'].split(','):
                r.locality_tags.append(tag)
                
    # recommended course
    for recommend,count in record.get('recommend_list',[]):
        if count > 1:
            r.specialties.append(Tag(value=recommend, count=count))
        
    r._src = 'dianping.com'
    r.save()

def import_site(site_name):
    for record in origin.shops.find({'city':site_name}):
        bread_crumb = record['bread_crumb'].split(u'\xbb')
        c = bread_crumb[0].replace(cname, '')

        # correct city by replacing '站' with '市'
        city = record['city']
        if city.endswith('站'.decode('utf-8')):
            city = city[:-1]+'市'.decode('utf-8')
        record['city'] = city

        handle = classification_dict.get(c.encode('utf-8'), null_handler)
        handle(record)

classification_dict = {
    '生活服务': null_handler,
    '酒店': hotel_handler,
    '餐厅': restraunt_handler,
    '休闲娱乐': null_handler,
    '运动健身':null_handler,
    '购物':null_handler,
    '丽人':null_handler
}

if __name__=="__main__":
    site_name = '无锡站'.decode('utf-8')
    cname = '无锡'.decode('utf-8')
    import_site(site_name)
