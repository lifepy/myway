# coding=utf-8
import pymongo

db = pymongo.Connection().areas
db.authenticate('myway','sharemyway2u')

provinces = []
municipality = ['北京市','天津市','上海市','重庆市']
cities = {}
with open('china_cities.txt','r') as f:
    for line in f.readlines():
        if line.strip() == '':
            continue
        items = line.strip().split(',')
        name = items[1][1:-1]
        pid = int(items[2]) -1
        layer = int(items[4])
        if layer == 1:
            provinces.append(name)
        if layer == 2:
            city_list = cities.setdefault(provinces[pid], [])
            city_list.append(name)
            cities[provinces[pid]] = city_list

for name in provinces:
    obj = {}
    obj['name'] = name
    if name not in municipality:
        obj['type'] = 'province'
        obj['city_list'] = cities.get(name, [])
        print "PROVINCE: %s"%name
        for c in cities.get(name,[]):
            print c,
        print '-'*30
    else:
        obj['type'] = 'municipality'
        if cities.get(name, []):
            obj['area_list'] = cities[name]
    db.districts.save(obj)
