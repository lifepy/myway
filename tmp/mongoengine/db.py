#!/usr/bin/python
# coding=utf-8
import sys
from mongoengine import *

class Shops(Document):
    meta = {
        'collection':'shops',
        'allow_inheritance':False,
    }

class Shop(Document):
    name = StringField()
    rating = FloatField()
    n_rating = IntField()
    avg_cost = IntField()
    city = StringField()
    transport = StringField()
    status = StringField()

    tel = StringField()
    description = StringField()
    hours = StringField()
    address = StringField()

    taste_rating = IntField()
    service_rating = IntField()
    atmosphere_rating = IntField()

    landmark_bread_crumb = StringField()
    bread_crumb = StringField()

    link_url = URLField()
    url = URLField()

    category = ListField(StringField())
    feature_list = ListField(StringField())
    atmosphere_list = ListField(StringField())

class Restraunt(Shop):
    location_tag = ListField(StringField())

connect('dianping',host='204.62.14.55', username='dianping',password='crawler')
#for ss in Shops.objects:#city__startswith='无锡')[:10]:
    #print ss.city,
    # if ss.city.startswith("无锡".decode('utf-8')):
        # print ss.name, "XX!"
#r = Restraunt(name='无锡市'.decode('utf-8'))
#r.save()
#s = Shop(name="abc")
#s.save()
sub_category_dict = {}
city = '无锡'
districts = [d.decode('utf-8') for d in ['惠山区','锡山区','滨湖区','崇安区','南长区','北塘区', '江阴市','宜兴市','新区']]
count_not_found = 0
count_found = 0
for shop in Shop.objects(city__startswith=city.decode('utf-8')):
    items = shop['bread_crumb'].split(u'\xbb')
    '''
    for item in items:
        if item in districts:
            #print shop.name, item
            count_found += 1
            break
    else:
        print shop.name, "NOT FOUND", shop.bread_crumb
        count_not_found += 1
        '''
    category = items[0]
    sub_category = items[1]
    sub_category_set = sub_category_dict.get(category, set())
    sub_category_set.add(sub_category)
    sub_category_dict[category] = sub_category_set
    #print category, sub_category
    #r = raw_input('press any key to continue')
'''
print "FOUND:", count_found
print "NOT FOUND:", count_not_found
'''
for k,v in sub_category_dict.items():
    print "CATEGORY:", k
    for sub_category in v:
        print sub_category,
    print ''
