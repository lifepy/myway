# coding=utf-8
import sys; sys.path.append('../')
from pymongo import Connection

from mongo_models import *
from query_json.db import cities_in, subareas_in

origin = Connection(host='204.62.14.55').dianping
origin.authenticate('dianping','crawler')

target_provinces = ['江苏省','浙江省','山东省','安徽省','广西省','福建省','广东省','四川省','云南省']

target_munilipalities = ['北京','天津','上海','重庆']

char_shi='市'.decode('utf-8')

def null_handler(record, subareas): pass

def hotel_handler(record, subareas): pass

def restraunt_handler(record, subareas):
    if Restraunt.objects(name=record['name']) \
       or record.get('rating',0) < 2 \
       or record.get('n_rating',0) < 2:
        return

    r = Restraunt(name = record['name'])

    # transport every attribute that has same name
    for key in dict(record).keys():
        if key in r.__dict__['_data'].keys() and key not in ['category']:
            r.__dict__['_data'][key] = record[key]

    # find city in admin-division database and tag restraunt with locality
    districts = dict([(s['name'],s) for s in subareas])
    bread_crumb = record['bread_crumb'].split(u'\xbb')
    for item in bread_crumb:
        if item in districts.keys():
            for tag in districts[item]['fullname'].split(','):
                r.locality_tags.append(tag)
                
    # recommended course
    for recommend,count in record.get('recommend_list',[]):
        if count > 1:
            r.specialties.append(Tag(value=recommend, count=count))
        
    r.save()

classification_dict = {
    '生活服务': null_handler,
    '酒店': hotel_handler,
    '餐厅': restraunt_handler,
    '休闲娱乐': null_handler,
    '运动健身':null_handler,
    '购物':null_handler,
    '丽人':null_handler
}
'''
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
'''
def clean_city(city_name):
    print "CITY: " + city_name
    if type(city_name) != unicode:
        city_name = city_name.decode('utf-8')
    # remove trailing '市'
    if city_name.endswith(char_shi):
        city_name = city_name.replace(char_shi, '')

    site_name = city_name + '站'.decode('utf-8')
    subareas = subareas_in(city_name)
    for s in subareas:
        print "    subarea: ", s['name']

    for record in origin.shops.find({'city':site_name}):
        bread_crumb = record['bread_crumb']
        if bread_crumb is None: 
            continue
        bread_crumb = bread_crumb.split(u'\xbb')
        c = bread_crumb[0].replace(city_name, '')

        record['city'] = city_name

        handle = classification_dict.get(c.encode('utf-8'), null_handler)
        handle(record, subareas)

def clean_target_province():
    for province in target_provinces:
        cities = cities_in(province)
        for city in cities:
            clean_city(city['name'])

def clean_target_municipality():
    for city in target_munilipalities:
        clean_city(city)
        
def stat_by_city():    
    for province in target_provinces:
        print province
        counts = []
        cities = cities_in(province)
        for city in cities:
            count = Restraunt.objects(city=city['name']).count()
            counts.append(count)
            print '%10s : %d' %(city['name'],count)
        print "共计:", sum(counts),'\n'

    for city_name in target_munilipalities:
        count = Restraunt.objects(city=city_name).count()
        print "%s : %d" %(city_name, count)

if __name__=="__main__":
    #clean_target_province()
    clean_target_municipality()
    stat_by_city()
