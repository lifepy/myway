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
aset = set()
bset = set()
cset = set()
dset = set()
eset = set()
fset = set()
gset = set()

sub_category_dict = {}
city = '无锡'
for br in Shop.objects(city__startswith=city.decode('utf-8')):
    items = br['bread_crumb'].split(u'\xbb')
    category = items[0].replace(city,'')
    sub_category = items[1]
    sub_category_set = sub_category_dict.get(category, set())
    sub_category_dict.add(sub_category)
    sub_category_dict[category] = sub_category_set
    print category, sub_category
    r = raw_input('press any key to continue')

for k,v in sub_category_dict:
    print "CATEGORY:", k
    for sub_category in v:
        print item,
