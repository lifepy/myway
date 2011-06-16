# coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson

import logging
logger = logging.getLogger('console.views')
city_dict = {
    ('江苏省','jiangsu'): ['南京市','无锡市','常州市','苏州市',],
    ('浙江省','zhejiang'): ['杭州市','金华市','嘉兴市','绍兴市',],
}

area_dict = {
    '无锡市': ['锡山区','滨湖区',],
}

def get_city_list(request, province):
    # province = request.GET["province"]
    key_dict = dict([(pinyin, (pname, pinyin),) for pname, pinyin in city_dict.keys()])
    city_list = city_dict[key_dict[province]]
    ret = simplejson.dumps({"cities":city_list})
    return HttpResponse(ret)

def get_area_list(request, city):
    area_list = area_dict[city.encode('utf-8')]
    ret = simplejson.dumps({'areas':area_list})
    return HttpResponse(ret)
